from ai_engine.openai_model import run_openai
from ai_engine.gemini_model import run_gemini
from ai_engine.claude_model import run_claude
from ai_engine.sentiment import sentiment_score
from ai_engine.weather import weather_impact
from ai_engine.geopolitical import geopolitics_score

def ai_decision(asset):
    """
    Multi-Model AI Decision Engine
    Combines OpenAI, Gemini, Claude + market factors
    """
    # Get AI model outputs
    oai = run_openai(asset)
    gem = run_gemini(asset)
    cla = run_claude(asset)
    
    # Get market factors
    sent = sentiment_score(asset)
    weather = weather_impact(asset)
    geo = geopolitics_score(asset)
    
    # Weighted ensemble calculation
    final_score = (
        oai["score"] * 0.35 +
        gem["score"] * 0.25 +
        cla["score"] * 0.20 +
        sent * 0.10 +
        weather * 0.05 +
        geo * 0.05
    )
    
    # Determine recommendation
    if final_score >= 0.7:
        recommendation = "BUY"
    elif final_score <= 0.3:
        recommendation = "SELL"
    else:
        recommendation = "HOLD"
    
    return {
        "asset": asset,
        "score": round(final_score, 3),
        "recommendation": recommendation,
        "details": {
            "openai": oai,
            "gemini": gem,
            "claude": cla,
            "sentiment": sent,
            "weather": weather,
            "geopolitics": geo
        }
    }
