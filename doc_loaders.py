from langchain_community.document_loaders import TextLoader, PyMuPDFLoader, UnstructuredPDFLoader, WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash-lite")
parser = StrOutputParser()

# text_loader = TextLoader("content.txt", encoding= "utf-8")
# pdf_loader = PyMuPDFLoader(file_path= "Atomic habits.pdf")
# unstruc_pdf_loader = UnstructuredPDFLoader(file_path="Biology_9_E_Part_1.pdf")
web_loader = WebBaseLoader("https://currentaffairs.adda247.com/")


# text_docs = text_loader.load()
# pdf_docs = pdf_loader.load()
# unstruc_pdf_docs = unstruc_pdf_loader.load()
web_docs = web_loader.load()
# print(text_docs)
# print(pdf_docs)
print(web_docs)