# 📚 AI Research Paper Assistant using RAG

An intelligent Research Paper Question-Answering System built using Retrieval-Augmented Generation (RAG), FAISS Vector Database, Sentence Transformers, LangChain, and Google Gemini 2.5 Flash.

The application allows users to upload multiple research papers and ask natural language questions. Instead of relying solely on the language model's knowledge, the system retrieves the most relevant information from the uploaded papers and generates accurate context-aware answers.

---

## 🚀 Features

* 📄 Upload and process multiple research papers (PDFs)
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 AI-powered question answering with Gemini 2.5 Flash
* ⚡ Fast document retrieval using FAISS
* 💬 Interactive Gradio chatbot interface
* 📚 Context-aware responses generated from uploaded papers
* 🌐 Shareable public demo link via Gradio

---

## 🏗️ System Architecture

User Question
↓
FAISS Vector Search
↓
Retrieve Relevant Chunks
↓
Construct Context
↓
Gemini 2.5 Flash
↓
Generated Answer

---

## 🛠️ Tech Stack

### Languages

* Python

### AI & Machine Learning

* Google Gemini 2.5 Flash
* Sentence Transformers
* LangChain

### Vector Database

* FAISS (Facebook AI Similarity Search)

### Document Processing

* PyPDF

### Frontend

* Gradio

---

## 📂 Project Workflow

### Step 1: Load Research Papers

Research papers are uploaded in PDF format and loaded into the system.

### Step 2: Split Documents

Large documents are divided into smaller chunks for efficient retrieval.

### Step 3: Generate Embeddings

Sentence Transformers convert text chunks into dense vector embeddings.

### Step 4: Store in FAISS

All embeddings are stored in a FAISS vector database for similarity search.

### Step 5: Retrieve Relevant Context

When a user asks a question, the most relevant document chunks are retrieved.

### Step 6: Generate Response

The retrieved context is provided to Gemini 2.5 Flash, which generates a final answer.

---

## 📸 Demo

### Example Question

What is BERT?

### Example Response

BERT is a multi-layer bidirectional Transformer encoder that learns contextual representations from both left and right contexts simultaneously. It is pre-trained using Masked Language Modeling and fine-tuned for downstream NLP tasks.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Research-Paper-Assistant.git
cd AI-Research-Paper-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a Gemini API Key from Google AI Studio.

Set your API key:

```python
from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)
```

---

## ▶️ Run the Application

```bash
python app.py
```

or run the notebook in Google Colab.

---

## 📁 Project Structure

```text
AI-Research-Paper-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── ResearchPaper1.pdf
├── ResearchPaper2.pdf
├── ResearchPaper3.pdf
└── screenshots/
```

---

## 🎯 Future Improvements

* Upload PDFs directly through the UI
* Source citations and page references
* Chat history memory
* Multi-document summarization
* Support for DOCX and TXT files
* Deployment on Hugging Face Spaces
* User authentication and document management

---

## 📈 Learning Outcomes

Through this project, I gained hands-on experience with:

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Vector Databases
* Semantic Search
* Prompt Engineering
* LangChain Framework
* Document Question Answering
* AI Application Deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Tanmay Agarwal

B.Tech Student | AI & Machine Learning Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
