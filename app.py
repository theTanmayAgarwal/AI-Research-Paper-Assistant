import os
import time
import gradio as gr

from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# ==========================================
# GEMINI CLIENT
# ==========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ==========================================
# LOAD PDFs
# ==========================================

pdf_files = [
    "ResearchPaper1.pdf",
    "ResearchPaper2.pdf",
    "ResearchPaper3.pdf"
]

documents = []

for pdf in pdf_files:
    loader = PyPDFLoader(pdf)
    documents.extend(loader.load())


# ==========================================
# TEXT SPLITTING
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)


# ==========================================
# EMBEDDINGS
# ==========================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==========================================
# VECTOR DATABASE
# ==========================================

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

print("✅ Vectorstore created successfully")


# ==========================================
# RAG FUNCTION
# ==========================================

def answer_question(question):

    start = time.time()

    try:

        docs = vectorstore.similarity_search(
            question,
            k=5
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are a research assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:

"I could not find that information in the uploaded papers."

Context:
{context}

Question:
{question}
"""
        )

        sources = "\n\n".join([
            f"📄 Source {i+1}\n{doc.page_content[:200]}..."
            for i, doc in enumerate(docs)
        ])

        elapsed = round(
            time.time() - start,
            2
        )

        return f"""
ANSWER:

{response.text}

⏱ Response Time: {elapsed} sec

------------------------------------

SOURCES USED:

{sources}
"""

    except Exception as e:

        return f"""
⚠️ Error

{str(e)}

Possible reasons:
• Gemini API quota exceeded
• Invalid API key
• Network issue
• Temporary Google service issue
"""


# ==========================================
# CHAT FUNCTION
# ==========================================

def chat(message, history):
    return answer_question(message)


# ==========================================
# GRADIO UI
# ==========================================

demo = gr.ChatInterface(
    fn=chat,
    title="📚 AI Research Paper Assistant",
    description="""
Ask questions about uploaded research papers.

Built using:
• LangChain
• FAISS
• Sentence Transformers
• Gemini 2.5 Flash
• Retrieval-Augmented Generation (RAG)
""",
    examples=[
        "What is BERT?",
        "How is the model trained?",
        "What datasets were used?",
        "What are the limitations?"
    ],
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch()