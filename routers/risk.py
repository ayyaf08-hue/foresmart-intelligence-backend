from fastapi import APIRouter

router = APIRouter(prefix="/risk", tags=["Risk"])

@router.get("/score")
def get_risk_score(asset: str):
    """
    Get risk assessment for asset
    Example: /risk/score?asset=Bitcoin
    """
    # Simulated risk calculation
    risk_scores = {
        "Bitcoin": 0.65,
        "Ethereum": 0.58, 
        "Gold": 0.25,
        "Oil": 0.45,
        "NASDAQ": 0.40,
        "S&P500": 0.35
    }
    
    score = risk_scores.get(asset, 0.50)
    
    if score <= 0.3:
        level = "Low"
    elif score <= 0.6:
        level = "Medium" 
    else:
        level = "High"
        
    return {
        "asset": asset,
        "risk_score": score,
        "risk_level": level,
        "recommendation": "Consider portfolio diversification" if score > 0.6 else "Acceptable risk level"
    }
