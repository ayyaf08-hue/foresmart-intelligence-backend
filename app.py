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

# إعدادات CORS لتمكين واجهة المستخدم من الاتصال
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ayyaf08-hue.github.io",       # ← رابط موقعك الرئيسي
        "https://www.foresmart4.store",        # ← دومينك المستقبلي
        "https://foresmart4.store",            # ← بدون www
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
        "company": "Ranim ForeSmart Investment Corporation"
    }

@app.get("/health")
def healthcheck():
    return {"status": "healthy", "port": PORT}
