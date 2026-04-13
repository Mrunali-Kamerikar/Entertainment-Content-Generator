# CineVerse: AI Entertainment Hub

A comprehensive AI-powered entertainment platform featuring movie recommendations, an intelligent chatbot assistant, and a professional-grade screenplay generator.

## 🌟 Key Features

### 🎬 CineVerse Dashboard
- **Personalized Recommendations**: AI-driven movie suggestions based on your preferences.
- **Sentiment Analysis**: Real-time review sentiment breakdown (Positive, Neutral, Negative).
- **Interactive Movie Exploration**: Detailed views, trailers, and cast information.
- **Category Tabs**: Seamlessly explore Bollywood, Hollywood, Tollywood, K-Drama, and Anime.

### 💬 CineVerse Assistant (ChatBot)
- **AI Movie Expert**: Ask questions about any film, director, or genre.
- **Natural Language Understanding**: Powered by Google Gemini AI for human-like conversations.
- **Contextual Suggestions**: Get movie ideas directly within the chat interface.

### ✍️ Professional Script Generator
- **Multi-Genre Support**: Generate screenplays for Hollywood, Bollywood, K-Drama, and Anime styles.
- **Customizable Criteria**: Specify scene ideas, languages (Hindi, English, Hinglish, etc.), characters, setting, and tone.
- **AI Iteration Tools**:
  - **Intense**: Amplify the drama and stakes of your scene.
  - **Humorous**: Inject wit and comedic timing.
  - **Dialogue Only**: Refine character voices and subtext without changing the action.
- **RAG-Powered**: Uses Retrieval-Augmented Generation (FAISS) to match professional script patterns.

---

## 🛠️ Tech Stack

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **AI Model**: [Google Gemini AI](https://ai.google.dev/)
- **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss) (for Retrieval-Augmented Generation)
- **Embeddings**: Sentence-Transformers
- **Environment**: Python 3.10+

### Frontend
- **Framework**: [React](https://react.dev/) + [Vite](https://vitejs.dev/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Animations**: [Motion](https://motion.dev/) (framer-motion)
- **Icons**: [Lucide-React](https://lucide.dev/)
- **Components**: Radix UI / Shadcn UI

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ installed
- Node.js 18+ and npm installed
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your Gemini API Key
echo "GOOGLE_API_KEY='your_api_key_here'" > .env

# Start the server
python server.py
```
The backend will be running at `http://localhost:8000`.

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```
The application will be available at `http://localhost:5173`.

---

## 📂 Project Structure

```text
Entertainment-Script-Generator/
├── backend/                # FastAPI Python Server
│   ├── pipeline.py         # AI Script Generation Pipeline
│   ├── server.py           # API Endpoints
│   ├── prompts.py          # AI Prompt Templates
│   ├── rag_manager.py      # Vector search logic
│   └── requirements.txt    # Python dependencies
├── frontend/               # Vite React Application
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/ # UI Components (ChatBot, ScriptGenerator, etc.)
│   │   │   ├── services/   # API Services (backend.ts, tmdb.ts)
│   │   │   └── pages/      # Main Dashboard and Login
│   └── package.json        # Frontend dependencies
└── README.md               # You are here!
```

## 📝 License
This project is for educational purposes as part of the B.Tech 8th Semester GenAI coursework.
