# backend/app/schemas/product.py

from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    code: str


class ProductResponse(BaseModel):
    prd_id: int
    code: str
    name: str
    price: int
    image_url: Optional[str]

    class Config:
        orm_mode = True
