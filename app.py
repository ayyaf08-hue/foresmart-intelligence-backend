import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import ai, trading, risk

PORT = int(os.environ.get("PORT", 8000))

app = FastAPI(
    title="foresmart-intelligence",
    description="Ranim ForeSmart Investment Corporation - AI Engine",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "[ayyaf08-hue.github.io](https://ayyaf08-hue.github.io)",
        "[ayyaf08-hue.github.io](https://ayyaf08-hue.github.io/foresmart-investment-platform)",
        "[foresmart4.store](https://www.foresmart4.store)",
        "[foresmart4.store](https://foresmart4.store)"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai.router)
app.include_router(trading.router)
app.include_router(risk.router)


@app.get("/")
def home():
    return {
        "status": "foresmart-intelligence active",
        "version": "1.0",
        "company": "Ranim ForeSmart Investment Corporation",
        "endpoints": [
            "/ai/recommend?asset=Bitcoin",
            "/ai/full-analysis?asset=Bitcoin",
            "/trading/portfolio",
            "/risk/score?asset=Bitcoin"
        ]
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "port": PORT
    }
