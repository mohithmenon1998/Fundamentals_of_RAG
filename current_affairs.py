from langchain_community.document_loaders import TextLoader, PyMuPDFLoader, UnstructuredPDFLoader, WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash-lite")
parser = StrOutputParser()

web_loader = WebBaseLoader("https://currentaffairs.adda247.com/")

web_docs = web_loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    # Try to split by paragraph, then line, then sentence, then character
    separators=["\n\n", "\n", ".", " "], 
    chunk_size=1000, 
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

prompt = PromptTemplate(template="I have scraped a current affairs website, I want to study for UPSC examination, As an expert can you list todays current affairs and categorize them and make a study note of it, this the data i scraped from the website, data --> {text}")

chunks = text_splitter.create_documents([web_docs[0].page_content])

chain = prompt | model | parser

result = chain.invoke({"text": chunks})


print(chunks)

