# 🎬 CineVerse: AI Entertainment Hub

A comprehensive **AI-powered entertainment platform** featuring movie recommendations, an intelligent chatbot assistant, and a professional-grade screenplay generator.

---

## 📌 Project Information

| Field                 | Details                         |
| --------------------- | ------------------------------- |
| **Division**          | D6                              |
| **Group**             | Group 03D6                      |
| **Project No**        | GAI-14                          |
| **Subject**           | Gen AI                          |
| **Problem Statement** | Entertainment Content Generator |
| **Tools Used**        | Python, Vector DB, LLM API      |

---

## 📝 Project Description

CineVerse is a specialized **GenAI content generation tool** designed for entertainment professionals. Using advanced **Prompt Engineering** techniques, the platform transforms basic ideas into **high-quality professional outputs** such as screenplay scenes.

The system ensures:

* Consistency in tone and formatting
* Industry-standard storytelling structure
* Reduced manual effort in drafting scripts and creative content

---

## 🌟 Key Features

### 🎬 CineVerse Dashboard

* **Personalized Recommendations**: AI-driven movie suggestions based on user preferences
* **Sentiment Analysis**: Real-time classification (Positive, Neutral, Negative)
* **Interactive Movie Exploration**: Trailers, cast details, and insights
* **Category Tabs**: Bollywood, Hollywood, Tollywood, K-Drama, Anime

---

### 💬 CineVerse Assistant (ChatBot)

* **AI Movie Expert**: Ask about movies, directors, genres
* **Natural Language Understanding**: Powered by Google Gemini AI
* **Contextual Suggestions**: Smart recommendations within chat

---

### ✍️ Professional Script Generator

* **Multi-Genre Support**: Hollywood, Bollywood, K-Drama, Anime

* **Customizable Inputs**:

  * Scene ideas
  * Language (Hindi, English, Hinglish, etc.)
  * Characters, setting, tone

* **AI Iteration Tools**:

  * **Intense** → Boost drama and stakes
  * **Humorous** → Add comedy and wit
  * **Dialogue Only** → Refine character conversations

* **RAG-Powered System**:

  * Uses FAISS for retrieval
  * Matches professional screenplay patterns

---

## 🛠️ Tech Stack

### Backend

* **Framework**: FastAPI (Python)
* **AI Model**: Google Gemini AI
* **Vector Store**: FAISS
* **Embeddings**: Sentence-Transformers
* **Environment**: Python 3.10+

---

### Frontend

* **Framework**: React + Vite
* **Styling**: Tailwind CSS
* **Animations**: Framer Motion
* **Icons**: Lucide-React
* **UI Components**: Radix UI / Shadcn UI

---

## 🚀 Getting Started

### 1. Prerequisites

* Python 3.10+
* Node.js 18+ and npm
* Google Gemini API Key

---

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Add API key
echo "GOOGLE_API_KEY='your_api_key_here'" > .env

# Run server
python server.py
```

Backend runs at:
👉 [http://localhost:8000](http://localhost:8000)

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
👉 [http://localhost:5173](http://localhost:5173)

---

## 📂 Project Structure

```text
Entertainment-Script-Generator/
├── backend/
│   ├── pipeline.py
│   ├── server.py
│   ├── prompts.py
│   ├── rag_manager.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   ├── services/
│   │   │   └── pages/
│   └── package.json
│
└── README.md
```

---

## 👥 Team Members

| # | Name              | Enrollment No |
| - | ----------------- | ------------- |
| 1 | Maitry Banduke    | EN22CS301571  |
| 2 | Mohd Quasim       | EN22CS301603  |
| 3 | Mrunali Kamerikar | EN22CS301618  |
| 4 | Muskan Asija      | EN22CS301623  |

---

## 📝 License

This project is developed for **educational purposes** as part of the **B.Tech 8th Semester GenAI coursework**.
