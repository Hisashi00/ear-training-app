import { useState, useEffect } from "react";

export default function Practice() {
  const [question, setQuestion] = useState(null);
  const API_URL = "http://127.0.0.1:8000/generate-question?difficulty=medium";  // ✅ クエリパラメータを追加

  const fetchQuestion = async () => {
    try {
      const response = await fetch(API_URL, { mode: "cors" }); // ✅ CORS対応
      if (!response.ok) throw new Error("Failed to fetch");
      const data = await response.json();
      setQuestion(data.question);
    } catch (error) {
      console.error("Error fetching question:", error);
    }
  };

  useEffect(() => {
    fetchQuestion();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-2xl font-bold mb-4">Practice Mode</h1>
      {question ? (
        <p className="text-xl mb-4">Root Note: {question.root} - Interval: {question.interval}</p>
      ) : (
        <p>Loading...</p>
      )}
      <button className="px-4 py-2 bg-blue-500 text-white rounded" onClick={fetchQuestion}>
        Next Question
      </button>
    </div>
  );
}
