from fastapi import APIRouter
from ai_engine.decision import ai_decision

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/recommend")
def get_recommendation(asset: str):
    """
    Get AI recommendation for trading asset
    Example: /ai/recommend?asset=Bitcoin
    """
    result = ai_decision(asset)
    return result

@router.get("/full-analysis")
def get_full_analysis(asset: str):
    """
    Get comprehensive AI analysis
    """
    result = ai_decision(asset)
    return {
        "asset": asset,
        "recommendation": result["recommendation"],
        "confidence": result["score"],
        "analysis": "Advanced multi-model AI analysis complete",
        "company": "Ranim ForeSmart Investment Corporation"
    }
