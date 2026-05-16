import random
from config import GEMINI_API_KEY

def run_gemini(asset):
    """
    Google Gemini Analysis Simulation
    Multi-modal AI analysis for trading decisions
    """
    
    # Simulate Gemini analysis with different scoring pattern
    asset_analysis = {
        "Bitcoin": {"base": 0.78, "volatility": 0.15},
        "Ethereum": {"base": 0.72, "volatility": 0.12},
        "Gold": {"base": 0.68, "volatility": 0.08},
        "Oil": {"base": 0.55, "volatility": 0.18},
        "NASDAQ": {"base": 0.70, "volatility": 0.10},
        "S&P500": {"base": 0.65, "volatility": 0.08}
    }
    
    analysis = asset_analysis.get(asset, {"base": 0.60, "volatility": 0.12})
    
    # Add some market noise
    score = analysis["base"] + random.uniform(-analysis["volatility"], analysis["volatility"])
    score = max(0.1, min(0.95, score))  # Keep within bounds
    
    return {
        "model": "Google Gemini",
        "score": round(score, 3),
        "confidence": "Medium-High",
        "reasoning": f"Multi-modal analysis suggests {asset} shows balanced risk-reward profile",
        "market_sentiment": "Cautiously optimistic",
        "api_key_status": "Connected" if GEMINI_API_KEY else "Missing"
    }
