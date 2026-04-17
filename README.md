# 📘 CineVerse → Entertainment Content Generator

## 🧾 Project Assignment Details

* **Division**: D6
* **Group**: Group 03D6
* **Project No**: GAI-14
* **Subject**: Gen AI
* **Tools Used**: Python, Vector Database, LLM API

---

## 👥 Team Members

| # | Name              | Enrollment No |
| - | ----------------- | ------------- |
| 1 | Maitry Banduke    | EN22CS301571  |
| 2 | Mohd Quasim       | EN22CS301603  |
| 3 | Mrunali Kamerikar | EN22CS301618  |
| 4 | Muskan Asija      | EN22CS301623  |

---

# 🎬 CineVerse: Entertainment Content Generator

A comprehensive AI-powered platform for entertainment professionals, combining intelligent recommendations, conversational AI, and advanced script generation.

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

* **📥 Download Option**: Download generated scripts as `.txt` files

* **🕘 Script History**: View and access all previously generated scripts

---

## 🔄 Application Workflow

1. **Authentication** – Users log in to access personalized features and script history
2. **Exploration** – Browse movies and analyze review sentiments
3. **Consultation** – Interact with the AI chatbot for queries and recommendations
4. **Creation**:

   * Enter script idea
   * Configure preferences (language, genre, tone, etc.)
   * Backend processes using FastAPI, RAG, and Gemini AI
   * Refine output using iteration tools
5. **Management** – Save, revisit, and download scripts

---

## 🛠️ Tech Stack

### 🔙 Backend

* Python 3.10+
* FastAPI
* Google Gemini AI (`google-genai` SDK)
* FAISS (Vector Store for RAG)
* Sentence Transformers (`all-MiniLM-L6-v2`)
* JSON-based storage

### 🎨 Frontend

* React + Vite
* Tailwind CSS
* Radix UI & Shadcn UI
* Framer Motion
* Lucide React Icons

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

* Python 3.10+
* Node.js 18+
* Google Gemini API Key

---

### 2️⃣ Backend Setup

```bash id="b2t9xz"
cd backend
pip install -r requirements.txt

# Add API key
echo "GOOGLE_API_KEY='your_api_key_here'" > .env

python server.py
```

Backend runs at: `http://localhost:8000`

---

### 3️⃣ Frontend Setup

```bash id="p4z8kj"
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 📂 Project Structure

```text id="k7v3nc"
Entertainment-Script-Generator/
├── backend/
│   ├── pipeline.py
│   ├── server.py
│   ├── prompts.py
│   ├── rag_manager.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   ├── services/
│   │   │   └── pages/
│   └── package.json
└── README.md
```

---

## 📝 License

This project is developed for educational purposes as part of B.Tech 8th Semester GenAI coursework.
