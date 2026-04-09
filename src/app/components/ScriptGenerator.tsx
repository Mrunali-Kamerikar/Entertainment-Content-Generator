"use client";

import { useState } from "react";

export default function ScriptGenerator() {
  const [topic, setTopic] = useState("");
  const [genre, setGenre] = useState("hollywood");
  const [tone, setTone] = useState("");
  const [characters, setCharacters] = useState("");
  const [scenes, setScenes] = useState<string[]>([]);

  const generateScene = async () => {
    const res = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ topic, genre, tone, characters }),
    });

    const data = await res.json();

    setScenes((prev) => [...prev, data.scene]);
    setTopic("");
  };

  return (
    <div className="p-6 bg-black text-white rounded-xl">
      <h2 className="text-xl font-bold mb-4">🎬 Story Generator</h2>

      <select
        value={genre}
        onChange={(e) => setGenre(e.target.value)}
        className="w-full p-2 mb-2 text-black"
      >
        <option value="hollywood">Hollywood</option>
        <option value="bollywood">Bollywood</option>
        <option value="kdrama">K-Drama</option>
        <option value="anime">Anime</option>
      </select>

      <input
        placeholder="Tone"
        value={tone}
        onChange={(e) => setTone(e.target.value)}
        className="w-full p-2 mb-2 text-black"
      />

      <textarea
        placeholder="Characters"
        value={characters}
        onChange={(e) => setCharacters(e.target.value)}
        className="w-full p-2 mb-2 text-black"
      />

      <input
        placeholder="Next scene idea..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        className="w-full p-2 mb-2 text-black"
      />

      <button
        onClick={generateScene}
        className="bg-purple-600 px-4 py-2 rounded"
      >
        Generate Next Scene
      </button>

      <div className="mt-6 space-y-6">
        {scenes.map((scene, index) => (
          <pre key={index} className="whitespace-pre-wrap border p-4">
            {scene}
          </pre>
        ))}
      </div>
    </div>
  );
}