from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer
import time
import re

app = FastAPI(title="Pressto API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain frontend kamu di production
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Load model sekali saat server start (bukan tiap request!)
print("Loading BART model...")
MODEL_NAME = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
print("Model ready.")


class SummarizeRequest(BaseModel):
    url: str


class SummarizeResponse(BaseModel):
    summary: str
    preview: str
    original_length: int
    summary_length: int
    compression_pct: int
    read_time_saved_sec: int


def extract_text(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Gagal mengambil URL: {e}")

    soup = BeautifulSoup(resp.content, "html.parser")

    # Hapus tag tidak relevan
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text(separator=" ", strip=True) for p in paragraphs)
    text = re.sub(r'\s+', ' ', text).strip()

    if len(text) < 100:
        raise HTTPException(status_code=422, detail="Teks artikel terlalu pendek atau tidak bisa diekstrak.")

    return text


def summarize(text: str) -> str:
    inputs = tokenizer.encode(
        "summarize: " + text,
        return_tensors="pt",
        max_length=1024,
        truncation=True,
    )
    ids = model.generate(
        inputs,
        max_length=180,
        min_length=50,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
    )
    return tokenizer.decode(ids[0], skip_special_tokens=True)


@app.post("/summarize", response_model=SummarizeResponse)
def summarize_article(body: SummarizeRequest):
    article_text = extract_text(body.url)
    summary = summarize(article_text)

    original_len = len(article_text)
    summary_len = len(summary)
    compression = round((1 - summary_len / original_len) * 100)

    # Estimasi waktu baca: rata-rata 200 kata/menit
    words_saved = len(article_text.split()) - len(summary.split())
    time_saved_sec = int((words_saved / 200) * 60)

    return SummarizeResponse(
        summary=summary,
        preview=article_text[:500] + "...",
        original_length=original_len,
        summary_length=summary_len,
        compression_pct=max(0, min(100, compression)),
        read_time_saved_sec=max(0, time_saved_sec),
    )


@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL_NAME}