"""
🚀 DAX Training Project - Main Application (CSV Version)

🎯 SYFTE:
FastAPI app som exponerar DAX measures via REST API
Data laddas från CSV-filer i app/data/raw/

🔄 ÅTERANVÄNDBAR: Hela FastAPI-strukturen
🆕 UNIK: Routern är kopplad till vård-specifika endpoints
"""
from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router

app = FastAPI(title="DAX Training Project - CSV Version{Minimal Kod}")

app.include_router(v1_router, prefix="/v1")

@app.get("/")
def root():
    return {"message": "DAX Training API is running. Try /v1/raw/clients or /v1/measures/total_minutes"}
