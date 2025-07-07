# backend/app/crud/product.py

from sqlalchemy.orm import Session
from app.models.models import Product

def get_product_by_code(db: Session, code: str):
    return db.query(Product).filter(Product.code == code).first()
