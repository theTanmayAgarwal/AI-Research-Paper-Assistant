# 📚 AI Research Paper Assistant using RAG

An intelligent Research Paper Question-Answering System built using **Retrieval-Augmented Generation (RAG)**, **FAISS Vector Database**, **Sentence Transformers**, **LangChain**, and **Google Gemini 2.5 Flash**.

The system allows users to ask natural language questions about uploaded research papers and receive context-aware answers generated from the document content.

---

## 🚀 Live Demo

🔗 **Hugging Face Space:**
https://huggingface.co/spaces/thetanmayagarwal/ai-research-paper-assistant

🔗 **GitHub Repository:**
https://github.com/theTanmayAgarwal/AI-Research-Paper-Assistant

---

## 📌 Features

* 📄 Load and process multiple research papers (PDFs)
* ✂️ Intelligent document chunking using LangChain
* 🧠 Semantic embeddings using Sentence Transformers
* 🔍 Fast similarity search with FAISS
* 🤖 Context-aware answer generation using Gemini 2.5 Flash
* 💬 Interactive chatbot interface built with Gradio
* ☁️ Deployed on Hugging Face Spaces
* 📚 Retrieval-Augmented Generation (RAG) pipeline

---

## 🛠️ Tech Stack

### AI / Machine Learning

* Google Gemini 2.5 Flash
* Sentence Transformers
* FAISS
* LangChain

### Backend

* Python

### Frontend

* Gradio

### Deployment

* Hugging Face Spaces

---

## 🏗️ Project Architecture

User Question
↓
FAISS Similarity Search
↓
Relevant Research Paper Chunks Retrieved
↓
Context Sent to Gemini 2.5 Flash
↓
Grounded Answer Generated
↓
Response Displayed in Gradio Chat Interface

---

## 📂 Project Structure

```text
AI-Research-Paper-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── ResearchPaper1.pdf
├── ResearchPaper2.pdf
├── ResearchPaper3.pdf
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/theTanmayAgarwal/AI-Research-Paper-Assistant.git
cd AI-Research-Paper-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set Gemini API Key

Create an environment variable:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Run the application

```bash
python app.py
```

---

## 🧪 Example Questions

Try asking:

* What is BERT?
* How is the model trained?
* What datasets were used?
* What are the limitations of the proposed approach?
* Summarize the main contributions of the paper.
* What future work is suggested?

---

## 📈 Future Improvements

* Upload custom PDFs directly from the UI
* Persistent FAISS index storage
* Citation and page-level source references
* Multi-document comparison
* Conversation memory
* Streaming responses
* Advanced RAG techniques (Hybrid Search, Re-ranking)

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings and Semantic Search
* Large Language Model Integration
* LangChain Framework
* Hugging Face Deployment
* End-to-End AI Application Development

---

## 👨‍💻 Author

**Tanmay Agarwal**

GitHub: https://github.com/theTanmayAgarwal

LinkedIn: [www.linkedin.com/in/thetanmayagarwal](http://www.linkedin.com/in/thetanmayagarwal)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
