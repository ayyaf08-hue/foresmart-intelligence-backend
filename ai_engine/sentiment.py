import random

def sentiment_score(asset):
    """
    Market Sentiment Analysis Simulation
    Analyzes news sentiment and social media trends
    """
    
    # Different sentiment patterns for different assets
    sentiment_patterns = {
        "Bitcoin": {"positive": 0.70, "neutral": 0.20, "negative": 0.10},
        "Ethereum": {"positive": 0.65, "neutral": 0.25, "negative": 0.10},
        "Gold": {"positive": 0.55, "neutral": 0.35, "negative": 0.10},
        "Oil": {"positive": 0.45, "neutral": 0.30, "negative": 0.25},
        "NASDAQ": {"positive": 0.60, "neutral": 0.30, "negative": 0.10},
        "S&P500": {"positive": 0.58, "neutral": 0.32, "negative": 0.10}
    }
    
    pattern = sentiment_patterns.get(asset, {"positive": 0.50, "neutral": 0.35, "negative": 0.15})
    
    # Generate weighted random sentiment score
    rand = random.random()
    if rand < pattern["positive"]:
        score = random.uniform(0.60, 0.85)
    elif rand < pattern["positive"] + pattern["neutral"]:
        score = random.uniform(0.45, 0.65)
    else:
        score = random.uniform(0.20, 0.45)
    
    return round(score, 3)

def get_sentiment_details(asset):
    """Get detailed sentiment breakdown"""
    score = sentiment_score(asset)
    
    if score >= 0.65:
        sentiment = "Bullish"
        description = "Strong positive market sentiment"
    elif score >= 0.55:
        sentiment = "Optimistic"
        description = "Moderately positive sentiment"
    elif score >= 0.45:
        sentiment = "Neutral"
        description = "Balanced market sentiment"
    elif score >= 0.35:
        sentiment = "Cautious"
        description = "Slightly negative sentiment"
    else:
        sentiment = "Bearish"
        description = "Negative market sentiment"
    
    return {
        "score": score,
        "sentiment": sentiment,
        "description": description,
        "news_sources": "Reuters, Bloomberg, MarketWatch",
        "analysis_date": "2026-05-16"
    }
