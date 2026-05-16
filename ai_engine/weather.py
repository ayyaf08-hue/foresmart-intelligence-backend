  import random

def weather_impact(asset):
    """Weather Impact Analysis - Affects commodities mainly"""
    weather_sensitivity = {
        "Bitcoin": 0.75,  # Crypto unaffected by weather
        "Ethereum": 0.74,
        "Gold": 0.68,
        "Oil": 0.45,      # Weather affects oil production
        "NASDAQ": 0.65,
        "S&P500": 0.63
    }
    
    base_score = weather_sensitivity.get(asset, 0.60)
    weather_factor = random.uniform(-0.10, 0.15)
    
    return round(max(0.30, min(0.85, base_score + weather_factor)), 3)
