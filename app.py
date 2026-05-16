import os
from fastapi import FastAPI
from routers import ai, trading, risk

PORT = int(os.environ.get("PORT", 8000))

app = FastAPI(
    title="foresmart-intelligence",
    description="Ranim ForeSmart Investment Corporation - AI Engine",
    version="1.0"
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=PORT,
        reload=False
    )
