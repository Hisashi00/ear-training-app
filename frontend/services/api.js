export async function fetchQuestion() {
    const response = await fetch("http://localhost:8000/generate-question");
    const data = await response.json();
    return data.question;
  }
  