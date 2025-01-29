from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.generate import generate_interval  # `generate.py` にある関数をインポート

app = FastAPI()

# CORS を許可（フロントエンドからのリクエストを受け取れるようにする）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発用に全て許可（本番では制限する）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ear Training API"}

@app.get("/generate-question")
def get_question(difficulty: str = Query("medium", description="Difficulty level: easy, medium, hard")):
    """ フロントエンドから `difficulty` を受け取るように変更 """
    return {"question": generate_interval(difficulty)}
