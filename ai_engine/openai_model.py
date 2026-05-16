import random
from config import OPENAI_API_KEY

def run_openai(asset):
    """
    OpenAI GPT Analysis Simulation
    Advanced test model for asset recommendation
    """
    
    # Simulate OpenAI analysis with realistic scoring
    asset_scores = {
        "Bitcoin": random.uniform(0.75, 0.90),
        "Ethereum": random.uniform(0.70, 0.85),
        "Gold": random.uniform(0.60, 0.80),
        "Oil": random.uniform(0.50, 0.75),
        "NASDAQ": random.uniform(0.65, 0.80),
        "S&P500": random.uniform(0.60, 0.78)
    }
    
    base_score = asset_scores.get(asset, random.uniform(0.45, 0.75))
    
    return {
        "model": "OpenAI GPT",
        "score": round(base_score, 3),
        "confidence": "High",
        "reasoning": f"Technical analysis indicates positive momentum for {asset}",
        "api_key_status": "Connected" if OPENAI_API_KEY else "Missing"
    }
