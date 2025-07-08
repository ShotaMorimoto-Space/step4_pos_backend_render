# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import product, purchase

app = FastAPI()

# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                   "https://step4-pos-frontend-render.onrender.com"],  # Next.js 開発サーバー
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターを登録
app.include_router(product.router)
app.include_router(purchase.router)

@app.get("/")
def read_root():
    return {"message": "OK"}
