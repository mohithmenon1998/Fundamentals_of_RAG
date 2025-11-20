# RAG Fundamentals: Retrieval Augmented Generation with LangChain

Welcome to the RAG Fundamentals Repository! This project is dedicated to understanding and building Retrieval Augmented Generation (RAG). RAG is a powerful technique that helps Large Language Models (LLMs) provide smarter, more factual answers by looking up information from external documents before responding.

### Project Goal

The main goal is to learn RAG by dissecting the process and building the system component-by-component using the LangChain framework. This approach allows us to focus on the modular nature of RAG—exploring Document Loaders, Text Splitters, Embedding Models, and various Retrieval strategies—while leveraging LangChain's powerful abstractions.

### Prerequisites

To run the examples and notebooks in this repository, you'll need the following installed:

1. Python 3.13+ (We aim to stay compatible with the latest Python versions, including Python 3.13, by using up-to-date dependencies.)

2. LangChain and other Required Libraries: Install the dependencies listed in requirements.txt.

### Key RAG Components Explained

RAG connects an LLM to your knowledge base (documents). Think of it as giving the LLM the ability to "search its own library" before answering. The LangChain framework provides specific modules to handle each of these steps:

##### 1. Indexing

Reading & Splitting (LangChain Loaders/Splitters): We load all our documents (PDFs, reports, etc.) and break them into small, bite-sized pieces, called "chunks."

Turning Text into Numbers (LangChain Embeddings): We use a specialized AI model (the Embedding Model) to convert every chunk of text into a unique list of numbers (a vector). These vectors capture the meaning of the text.

Storing (LangChain VectorStores): We save all these meaning-vectors in a special database called a Vector Store, which is designed for very fast searching.

##### 2. Retrieval (Search Phase)

Query Conversion: When a user asks a question, we convert that question into its own meaning-vector using the exact same Embedding Model.

Finding the Best Chunks (LangChain Retrievers): We quickly compare the question-vector to all the stored document vectors in the Vector Store. This finds the top few chunks that are most relevant to the user's question.

##### 3. Generation (Answer Phase)

Prompt Building (LangChain PromptTemplates): We take the original user question and add the relevant chunks we just found. This creates a powerful, combined prompt: "Answer this question based ONLY on the following context: [Retrieved Chunks] + [Original Question]."

LLM Answers: The Large Language Model reads this augmented prompt and uses the provided chunks as facts to generate a grounded, accurate, and up-to-date answer.