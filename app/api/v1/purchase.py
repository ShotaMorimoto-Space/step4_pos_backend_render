# backend/app/api/v1/purchase.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud import transaction as transaction_crud
from app.schemas.purchase import PurchaseRequest, PurchaseResponse

router = APIRouter(prefix="/api/v1/purchase", tags=["Purchase"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PurchaseResponse)
def create_purchase(request: PurchaseRequest, db: Session = Depends(get_db)):
    try:
        total_ex, total_tax, total = transaction_crud.create_transaction(db, request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
        "success": True,
        "total_amt_ex_tax": total_ex,
        "total_tax_amt": total_tax,
        "total_amt": total,
    }
