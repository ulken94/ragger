"""This is the main module for the ragger package.

-Author: ulken94
-Contact: bestwook7@gmail.com
"""

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

print("Loading environment variables...")
loader = TextLoader("res/data.txt", encoding="utf-8")
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

splits = text_splitter.split_documents(documents)

print("Creating embeddings...")
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    persist_directory="./chroma_db",
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2},
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
)

query = "한얼이 현재 구상중인 프로젝트 이름이 뭐야?"
print(f"\n? {query}")

result = qa_chain.invoke({"query": query})

print("\nA:", result["result"])
print("\nSource Documents:")
for document in result["source_documents"]:
    print(f"- {document.metadata['source']}")
