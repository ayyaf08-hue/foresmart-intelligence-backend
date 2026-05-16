import random

def fetch_market_data(asset):
    """Fetch live market data simulation"""
    return {
        "asset": asset,
        "price": round(random.uniform(100, 1000), 2),
        "volume": round(random.uniform(500, 5000), 2),
        "change_24h": round(random.uniform(-5, 8), 2)
    }
