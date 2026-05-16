import random
from config import ANTHROPIC_API_KEY

def run_claude(asset):
    """
    Anthropic Claude Analysis Simulation
    Conservative AI analysis focused on risk assessment
    """
    
    # Claude tends to be more conservative in recommendations
    conservative_scores = {
        "Bitcoin": random.uniform(0.65, 0.80),
        "Ethereum": random.uniform(0.60, 0.75),
        "Gold": random.uniform(0.70, 0.85),  # Claude prefers stable assets
        "Oil": random.uniform(0.45, 0.65),
        "NASDAQ": random.uniform(0.55, 0.70),
        "S&P500": random.uniform(0.60, 0.75)
    }
    
    base_score = conservative_scores.get(asset, random.uniform(0.50, 0.70))
    
    # Claude emphasizes risk factors
    risk_adjustment = random.uniform(-0.05, 0.02)
    final_score = max(0.15, min(0.85, base_score + risk_adjustment))
    
    return {
        "model": "Anthropic Claude",
        "score": round(final_score, 3),
        "confidence": "Conservative",
        "reasoning": f"Risk-adjusted analysis for {asset} considers market stability factors",
        "risk_level": "Moderate" if final_score > 0.6 else "Low-Medium",
        "recommendation_note": "Prioritizes capital preservation",
        "api_key_status": "Connected" if ANTHROPIC_API_KEY else "Missing"
    }
