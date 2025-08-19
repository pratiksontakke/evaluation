import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
CHROMA_DB_PATH = "backend/app/chroma_db_google"

rag_chain = None
vector_store = None

def load_and_embed_documents():
    global vector_store
    
    embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    vector_store = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_function
    )
    
    if vector_store._collection.count() > 0:
        print("Knowledge base already loaded for Google.")
        return

    loader = JSONLoader(
        file_path='backend/app/kb/knowledge_base.json',
        jq_schema=' .exercises[] | {page_content: ("Exercise: " + .name + ", Category: " + .category + ", Instructions: " + .instructions)}',
        text_content=False
    )
    exercise_docs = loader.load()
    
    loader_nutrition = JSONLoader(
        file_path='backend/app/kb/knowledge_base.json',
        jq_schema=' .nutrition[] | {page_content: ("Topic: " + .topic + ", Info: " + .info)}',
        text_content=False
    )
    nutrition_docs = loader_nutrition.load()

    all_docs = exercise_docs + nutrition_docs
    
    Chroma.from_documents(
        documents=all_docs,
        embedding=embedding_function,
        persist_directory=CHROMA_DB_PATH
    )
    print("Knowledge base loaded and embedded with Google.")


def initialize_rag_chain():
    global rag_chain, vector_store

    if not vector_store:
        load_and_embed_documents()

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    template = """
    Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """
    prompt = PromptTemplate.from_template(template)

    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

def get_rag_chain():
    if not rag_chain:
        initialize_rag_chain()
    return rag_chain