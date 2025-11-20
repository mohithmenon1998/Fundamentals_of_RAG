from current_affairs import web_scraper
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

chunks = web_scraper(url= "https://currentaffairs.adda247.com/")
                     
vector_store = Chroma(embedding_function=embeddings, collection_name= "todays_news", persist_directory= "data/chromadb")

vector_store.add_documents(documents=chunks)