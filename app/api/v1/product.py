# backend/app/api/v1/product.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud import product as product_crud
from app.schemas.product import ProductResponse

router = APIRouter(prefix="/api/v1/product", tags=["Product"])

# DBセッション取得
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{code}", response_model=ProductResponse)
def read_product(code: str, db: Session = Depends(get_db)):
    product = product_crud.get_product_by_code(db, code)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
