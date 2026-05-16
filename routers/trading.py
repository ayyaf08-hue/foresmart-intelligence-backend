from fastapi import APIRouter

router = APIRouter(prefix="/trading", tags=["Trading"])

@router.get("/execute")
def execute_trade(asset: str, amount: float, action: str):
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
    return {
        "total_balance": "12,450 SAR",
        "today_profit": "+2.5%",
        "open_trades": 15,
        "subscription": "PRO"
    }
