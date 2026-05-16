from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Optional
import random
import math
from datetime import datetime, timedelta

app = FastAPI(title="ForeSmart Investment Platform", version="3.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# السوق الأمريكي - 20 شركة كاملة
# ============================================
US_MARKET = [
    {"symbol": "AAPL", "name": "Apple Inc.", "sector": "Technology", "price": 30233, "marketCap": 2850000000000, "pe": 28.5, "eps": 6.16, "dividend": 0.52},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "sector": "Technology", "price": 21912, "marketCap": 2350000000000, "pe": 33.2, "eps": 9.68, "dividend": 0.75},
    {"symbol": "NVDA", "name": "NVIDIA Corp.", "sector": "Semiconductors", "price": 270271, "marketCap": 1850000000000, "pe": 68.5, "eps": 12.34, "dividend": 0.16},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "sector": "Technology", "price": 391784, "marketCap": 1750000000000, "pe": 25.8, "eps": 5.92, "dividend": 0.00},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "sector": "E-commerce", "price": 18950, "marketCap": 1650000000000, "pe": 42.3, "eps": 2.94, "dividend": 0.00},
    {"symbol": "META", "name": "Meta Platforms", "sector": "Social Media", "price": 52340, "marketCap": 1250000000000, "pe": 28.1, "eps": 14.87, "dividend": 0.00},
    {"symbol": "TSLA", "name": "Tesla Inc.", "sector": "Automotive", "price": 17890, "marketCap": 850000000000, "pe": 58.2, "eps": 3.21, "dividend": 0.00},
    {"symbol": "JPM", "name": "JPMorgan Chase", "sector": "Financial", "price": 19850, "marketCap": 580000000000, "pe": 11.5, "eps": 16.23, "dividend": 4.20},
    {"symbol": "V", "name": "Visa Inc.", "sector": "Financial", "price": 27580, "marketCap": 560000000000, "pe": 29.8, "eps": 8.92, "dividend": 0.78},
    {"symbol": "WMT", "name": "Walmart Inc.", "sector": "Retail", "price": 16850, "marketCap": 450000000000, "pe": 28.5, "eps": 6.45, "dividend": 1.45},
    {"symbol": "JNJ", "name": "Johnson & Johnson", "sector": "Healthcare", "price": 15670, "marketCap": 420000000000, "pe": 22.3, "eps": 7.12, "dividend": 2.85},
    {"symbol": "PG", "name": "Procter & Gamble", "sector": "Consumer", "price": 16230, "marketCap": 400000000000, "pe": 25.6, "eps": 6.28, "dividend": 2.35},
    {"symbol": "XOM", "name": "Exxon Mobil", "sector": "Energy", "price": 11240, "marketCap": 450000000000, "pe": 12.8, "eps": 9.45, "dividend": 3.65},
    {"symbol": "CVX", "name": "Chevron Corp.", "sector": "Energy", "price": 15890, "marketCap": 310000000000, "pe": 11.2, "eps": 14.23, "dividend": 3.95},
    {"symbol": "HD", "name": "Home Depot", "sector": "Retail", "price": 34820, "marketCap": 350000000000, "pe": 21.5, "eps": 16.34, "dividend": 2.35},
    {"symbol": "MA", "name": "Mastercard", "sector": "Financial", "price": 45670, "marketCap": 430000000000, "pe": 36.8, "eps": 11.87, "dividend": 0.58},
    {"symbol": "UNH", "name": "UnitedHealth", "sector": "Healthcare", "price": 48760, "marketCap": 450000000000, "pe": 23.4, "eps": 20.89, "dividend": 1.45},
    {"symbol": "BAC", "name": "Bank of America", "sector": "Financial", "price": 3520, "marketCap": 280000000000, "pe": 11.8, "eps": 3.24, "dividend": 2.45},
    {"symbol": "NFLX", "name": "Netflix", "sector": "Entertainment", "price": 64520, "marketCap": 280000000000, "pe": 35.2, "eps": 18.45, "dividend": 0.00},
    {"symbol": "ADBE", "name": "Adobe", "sector": "Software", "price": 58980, "marketCap": 265000000000, "pe": 42.5, "eps": 13.88, "dividend": 0.00},
]

# السوق السعودي
SAUDI_MARKET = [
    {"symbol": "2222", "name": "أرامكو السعودية", "sector": "طاقة", "price": 30.95, "marketCap": 7500000000000, "pe": 15.2, "eps": 2.03, "dividend": 4.50},
    {"symbol": "1120", "name": "الراجحي", "sector": "مصارف", "price": 88.40, "marketCap": 350000000000, "pe": 18.5, "eps": 4.78, "dividend": 2.85},
    {"symbol": "2010", "name": "سابك", "sector": "بتروكيماويات", "price": 76.30, "marketCap": 230000000000, "pe": 12.3, "eps": 6.20, "dividend": 3.20},
    {"symbol": "7010", "name": "STC", "sector": "اتصالات", "price": 38.20, "marketCap": 190000000000, "pe": 16.8, "eps": 2.27, "dividend": 4.15},
    {"symbol": "1180", "name": "الأهلي", "sector": "مصارف", "price": 42.15, "marketCap": 85000000000, "pe": 14.5, "eps": 2.91, "dividend": 3.45},
]

# السوق البريطاني
UK_MARKET = [
    {"symbol": "HSBA", "name": "HSBC Holdings", "sector": "Banking", "price": 6.85, "marketCap": 135000000000, "pe": 7.5, "eps": 0.91, "dividend": 5.80},
    {"symbol": "BP", "name": "BP PLC", "sector": "Energy", "price": 5.12, "marketCap": 98000000000, "pe": 8.2, "eps": 0.62, "dividend": 4.65},
    {"symbol": "SHEL", "name": "Shell PLC", "sector": "Energy", "price": 27.85, "marketCap": 210000000000, "pe": 9.8, "eps": 2.84, "dividend": 3.85},
    {"symbol": "ULVR", "name": "Unilever", "sector": "Consumer", "price": 48.50, "marketCap": 120000000000, "pe": 18.5, "eps": 2.62, "dividend": 3.45},
]

# السوق الإماراتي
UAE_MARKET = [
    {"symbol": "EMAAR", "name": "إعمار العقارية", "sector": "عقارات", "price": 8.15, "marketCap": 68000000000, "pe": 12.5, "eps": 0.65, "dividend": 4.20},
    {"symbol": "EAND", "name": "اتصالات", "sector": "اتصالات", "price": 16.40, "marketCap": 72000000000, "pe": 14.8, "eps": 1.11, "dividend": 3.85},
    {"symbol": "DIB", "name": "بنك دبي الإسلامي", "sector": "مصارف", "price": 5.85, "marketCap": 45000000000, "pe": 10.2, "eps": 0.57, "dividend": 5.25},
]

# السوق الصيني
CHINA_MARKET = [
    {"symbol": "0700", "name": "Tencent Holdings", "sector": "Technology", "price": 42.15, "marketCap": 400000000000, "pe": 18.5, "eps": 2.28, "dividend": 0.85},
    {"symbol": "BABA", "name": "Alibaba Group", "sector": "E-commerce", "price": 9.45, "marketCap": 240000000000, "pe": 14.2, "eps": 0.67, "dividend": 1.25},
    {"symbol": "1211", "name": "BYD Company", "sector": "Automotive", "price": 28.30, "marketCap": 82000000000, "pe": 22.8, "eps": 1.24, "dividend": 0.00},
]

# السوق الأوروبي
EUROPE_MARKET = [
    {"symbol": "SAP", "name": "SAP SE", "sector": "Software", "price": 168.50, "marketCap": 195000000000, "pe": 28.5, "eps": 5.91, "dividend": 1.45},
    {"symbol": "VOW3", "name": "Volkswagen", "sector": "Automotive", "price": 112.30, "marketCap": 65000000000, "pe": 4.8, "eps": 23.40, "dividend": 5.85},
    {"symbol": "NESN", "name": "Nestlé", "sector": "Food", "price": 98.45, "marketCap": 260000000000, "pe": 22.3, "eps": 4.42, "dividend": 2.85},
]

# السوق الياباني
JAPAN_MARKET = [
    {"symbol": "7203", "name": "Toyota Motor", "sector": "Automotive", "price": 3520.00, "marketCap": 280000000000, "pe": 10.5, "eps": 335.00, "dividend": 2.45},
    {"symbol": "6758", "name": "Sony Group", "sector": "Technology", "price": 13850.00, "marketCap": 120000000000, "pe": 18.2, "eps": 761.00, "dividend": 0.65},
]

# العملات الرقمية
CRYPTO_MARKET = [
    {"symbol": "BTC", "name": "Bitcoin", "price": 64213, "change24h": 2.3, "volume": 28500000000, "marketCap": 1260000000000},
    {"symbol": "ETH", "name": "Ethereum", "price": 3482, "change24h": 1.1, "volume": 12800000000, "marketCap": 418000000000},
    {"symbol": "SOL", "name": "Solana", "price": 142, "change24h": -0.5, "volume": 2800000000, "marketCap": 62000000000},
    {"symbol": "BNB", "name": "BNB", "price": 612, "change24h": 0.8, "volume": 1500000000, "marketCap": 94000000000},
]

# المعادن
METALS_MARKET = [
    {"symbol": "XAU", "name": "الذهب", "price": 2345.50, "change24h": 0.42, "volume": 45000000000},
    {"symbol": "XAG", "name": "الفضة", "price": 28.15, "change24h": 0.35, "volume": 8500000000},
    {"symbol": "COPPER", "name": "النحاس", "price": 4.65, "change24h": -0.22, "volume": 12000000000},
]

# السندات
BONDS_MARKET = [
    {"symbol": "US10Y", "name": "الخزانة الأمريكية 10 سنوات", "price": 98.45, "yield": 4.35, "change": -0.15},
    {"symbol": "US30Y", "name": "الخزانة الأمريكية 30 سنة", "price": 96.20, "yield": 4.55, "change": -0.22},
    {"symbol": "SAUDI", "name": "السندات السعودية", "price": 101.30, "yield": 5.10, "change": 0.12},
]

# ============================================
# دوال حساب المؤشرات الفنية
# ============================================

def generate_historical_prices(base_price, years=3):
    """توليد بيانات تاريخية لمدة 3 سنوات"""
    historical = []
    current = base_price
    for year in range(2022, 2025):
        year_data = []
        for month in range(1, 13):
            change = random.uniform(-0.12, 0.15)
            current = current * (1 + change)
            year_data.append({
                "month": month,
                "price": round(current, 2),
                "volume": random.randint(1000000, 50000000),
                "high": round(current * random.uniform(1.01, 1.08), 2),
                "low": round(current * random.uniform(0.94, 0.99), 2),
                "change_percent": round(change * 100, 2)
            })
        historical.append({"year": year, "data": year_data})
    return historical

def calculate_indicators(prices):
    """حساب RSI, MACD, بولينجر باند, متوسطات متحركة"""
    if len(prices) < 20:
        return {}
    
    sma_20 = sum(prices[-20:]) / 20
    sma_50 = sum(prices[-50:]) / 50 if len(prices) >= 50 else sma_20
    sma_200 = sum(prices[-200:]) / 200 if len(prices) >= 200 else sma_50
    
    # RSI
    gains, losses = [], []
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))
    
    avg_gain = sum(gains[-14:]) / 14 if len(gains) >= 14 else sum(gains) / len(gains) if gains else 0
    avg_loss = sum(losses[-14:]) / 14 if len(losses) >= 14 else sum(losses) / len(losses) if losses else 0
    
    rsi = 100 - (100 / (1 + (avg_gain / avg_loss))) if avg_loss > 0 else 100
    
    # بولينجر باند
    std_dev = math.sqrt(sum([(p - sma_20)**2 for p in prices[-20:]]) / 20)
    upper_band = sma_20 + (std_dev * 2)
    lower_band = sma_20 - (std_dev * 2)
    
    # MACD
    ema_12 = sum(prices[-12:]) / 12
    ema_26 = sum(prices[-26:]) / 26 if len(prices) >= 26 else sma_20
    macd = ema_12 - ema_26
    signal = macd * 0.9
    
    return {
        "sma_20": round(sma_20, 2),
        "sma_50": round(sma_50, 2),
        "sma_200": round(sma_200, 2),
        "rsi": round(rsi, 2),
        "upper_band": round(upper_band, 2),
        "lower_band": round(lower_band, 2),
        "macd": round(macd, 4),
        "signal": round(signal, 4),
        "histogram": round(macd - signal, 4)
    }

# ============================================
# API Endpoints
# ============================================

@app.get("/")
def root():
    return {"status": "ForeSmart Investment Platform Active", "version": "3.0"}

@app.get("/api/markets/{market}")
def get_market(market: str):
    markets = {
        "us": US_MARKET, "saudi": SAUDI_MARKET, "uk": UK_MARKET,
        "uae": UAE_MARKET, "china": CHINA_MARKET, "europe": EUROPE_MARKET,
        "japan": JAPAN_MARKET, "crypto": CRYPTO_MARKET,
        "metals": METALS_MARKET, "bonds": BONDS_MARKET
    }
    if market not in markets:
        raise HTTPException(404, "Market not found")
    return {"market": market, "data": markets[market]}

@app.get("/api/markets/all")
def get_all_markets():
    return {
        "us": US_MARKET, "saudi": SAUDI_MARKET, "uk": UK_MARKET,
        "uae": UAE_MARKET, "china": CHINA_MARKET, "europe": EUROPE_MARKET,
        "japan": JAPAN_MARKET, "crypto": CRYPTO_MARKET,
        "metals": METALS_MARKET, "bonds": BONDS_MARKET
    }

@app.get("/api/indicators/{symbol}")
def get_indicators(symbol: str):
    all_stocks = US_MARKET + SAUDI_MARKET + UK_MARKET + UAE_MARKET + CHINA_MARKET + EUROPE_MARKET + JAPAN_MARKET
    stock = next((s for s in all_stocks if s["symbol"] == symbol), None)
    if not stock:
        raise HTTPException(404, "Stock not found")
    
    prices = [stock["price"] * random.uniform(0.85, 1.15) for _ in range(200)]
    indicators = calculate_indicators(prices)
    
    return {"symbol": symbol, "name": stock["name"], "indicators": indicators}

@app.get("/api/scanner")
def get_scanner():
    """سكانر الفرص الاستثمارية"""
    all_stocks = US_MARKET + SAUDI_MARKET + UK_MARKET + UAE_MARKET + CHINA_MARKET + EUROPE_MARKET + JAPAN_MARKET
    opportunities = []
    
    for stock in all_stocks:
        prices = [stock["price"] * random.uniform(0.85, 1.15) for _ in range(200)]
        indicators = calculate_indicators(prices)
        
        score = 0
        reasons = []
        
        if indicators["rsi"] < 30:
            score += 30
            reasons.append(f"RSI منخفض ({indicators['rsi']}) - منطقة ذروة بيع")
        elif indicators["rsi"] > 70:
            score -= 25
            reasons.append(f"RSI مرتفع ({indicators['rsi']}) - منطقة ذروة شراء")
        
        if indicators["macd"] > indicators["signal"]:
            score += 25
            reasons.append("MACD أعلى من خط الإشارة - إشارة شراء")
        else:
            score -= 15
            reasons.append("MACD أقل من خط الإشارة - إشارة بيع")
        
        if prices[-1] < indicators["lower_band"]:
            score += 20
            reasons.append("السعر تحت النطاق السفلي لبولينجر - فرصة شراء")
        
        if score >= 40:
            recommendation = "شراء قوي"
        elif score >= 20:
            recommendation = "شراء"
        elif score <= -30:
            recommendation = "بيع قوي"
        elif score <= -10:
            recommendation = "بيع"
        else:
            recommendation = "احتفاظ"
        
        opportunities.append({
            "symbol": stock["symbol"],
            "name": stock["name"],
            "sector": stock["sector"],
            "price": stock["price"],
            "score": score,
            "recommendation": recommendation,
            "reasons": reasons,
            "rsi": indicators["rsi"]
        })
    
    opportunities.sort(key=lambda x: x["score"], reverse=True)
    return {"opportunities": opportunities[:30]}

@app.get("/api/archive/{market}/{year}")
def get_archive(market: str, year: int):
    markets_map = {
        "us": US_MARKET, "saudi": SAUDI_MARKET, "uk": UK_MARKET,
        "uae": UAE_MARKET, "china": CHINA_MARKET, "europe": EUROPE_MARKET, "japan": JAPAN_MARKET
    }
    if market not in markets_map:
        raise HTTPException(404, "Market not found")
    
    archive_data = []
    for stock in markets_map[market]:
        historical = generate_historical_prices(stock["price"])
        year_data = next((y for y in historical if y["year"] == year), None)
        
        if year_data:
            prices = [m["price"] for m in year_data["data"]]
            yearly_return = ((prices[-1] - prices[0]) / prices[0]) * 100
            archive_data.append({
                "symbol": stock["symbol"],
                "name": stock["name"],
                "start_price": prices[0],
                "end_price": prices[-1],
                "yearly_return": round(yearly_return, 2),
                "high": max(prices),
                "low": min(prices)
            })
    
    return {"market": market, "year": year, "data": archive_data}

@app.get("/api/ai/analysis/{symbol}")
def get_ai_analysis(symbol: str):
    all_stocks = US_MARKET + SAUDI_MARKET + UK_MARKET + UAE_MARKET + CHINA_MARKET + EUROPE_MARKET + JAPAN_MARKET
    stock = next((s for s in all_stocks if s["symbol"] == symbol), None)
    if not stock:
        raise HTTPException(404, "Stock not found")
    
    prices = [stock["price"] * random.uniform(0.85, 1.15) for _ in range(200)]
    indicators = calculate_indicators(prices)
    
    tech_score = 0
    if indicators["rsi"] < 30:
        tech_score += 35
    if indicators["macd"] > indicators["signal"]:
        tech_score += 30
    if prices[-1] < indicators["lower_band"]:
        tech_score += 25
    
    if tech_score >= 60:
        recommendation = "شراء قوي"
    elif tech_score >= 35:
        recommendation = "شراء"
    elif tech_score <= -30:
        recommendation = "بيع قوي"
    elif tech_score <= -10:
        recommendation = "بيع"
    else:
        recommendation = "احتفاظ"
    
    return {
        "symbol": stock["symbol"],
        "name": stock["name"],
        "price": stock["price"],
        "sector": stock["sector"],
        "indicators": indicators,
        "recommendation": recommendation,
        "tech_score": tech_score,
        "risk_level": "عالي" if stock.get("pe", 0) > 30 else "متوسط" if stock.get("pe", 0) > 15 else "منخفض"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
