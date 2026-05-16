import random

def geopolitics_score(asset):
    """
    Geopolitical Risk Analysis Simulation
    Analyzes global tensions, wars, and political stability
    """
    
    # Base geopolitical stability by asset type
    geo_factors = {
        "Bitcoin": 0.60,  # Crypto less affected by traditional geopolitics
        "Ethereum": 0.58,
        "Gold": 0.45,     # Gold inversely affected by geopolitical tensions
        "Oil": 0.35,      # Oil highly sensitive to geopolitics
        "NASDAQ": 0.55,
        "S&P500": 0.52
    }
    
    base_stability = geo_factors.get(asset, 0.50)
    
    # Simulate current global tension factors
    tension_factors = random.uniform(-0.15, 0.10)  # Usually more negative
    
    final_score = max(0.20, min(0.80, base_stability + tension_factors))
    
    return round(final_score, 3)

def get_geopolitical_analysis(asset):
    """Get detailed geopolitical risk assessment"""
    score = geopolitics_score(asset)
    
    risk_factors = [
        "Middle East tensions",
        "US-China trade relations", 
        "European energy security",
        "Global supply chain stability",
        "Currency policy changes"
    ]
    
    if score >= 0.60:
        risk_level = "Low"
        impact = "Minimal geopolitical impact expected"
    elif score >= 0.45:
        risk_level = "Medium"
        impact = "Moderate geopolitical risks present"
    else:
        risk_level = "High"
        impact = "Significant geopolitical tensions affecting markets"
    
    return {
        "score": score,
        "risk_level": risk_level,
        "impact_assessment": impact,
        "key_factors": random.sample(risk_factors, 3),
        "recommendation": "Monitor closely" if score < 0.40 else "Standard monitoring"
    }
