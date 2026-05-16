import os
from fastapi import FastAPI
from routers import ai, trading, risk

# Get port from environment (Railway requirement)
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
        "endpoints": ["/ai/recommend", "/trading/execute", "/risk/score"]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "port": PORT}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
