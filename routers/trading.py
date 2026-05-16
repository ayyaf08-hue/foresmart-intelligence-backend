from fastapi import APIRouter

router = APIRouter(prefix="/trading", tags=["Trading"])

@router.get("/execute")
def execute_trade(asset: str, amount: float, action: str):
    """
    Execute trading simulation
    Example: /trading/execute?asset=Bitcoin&amount=1000&action=buy
    """
    return {
        "asset": asset,
        "amount": amount,
        "action": action.upper(),
        "status": "executed (simulation)",
        "timestamp": "2026-05-16T12:00:00Z",
        "company": "Ranim ForeSmart Investment Corporation"
    }

@router.get("/portfolio")
def get_portfolio():
    """Get current portfolio status"""
    return {
        "total_balance": "12,450 SAR",
        "today_profit": "+2.5%",
        "open_trades": 15,
        "subscription": "PRO"
    }
