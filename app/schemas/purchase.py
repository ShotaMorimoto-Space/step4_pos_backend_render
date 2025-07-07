# backend/app/schemas/purchase.py

from pydantic import BaseModel
from typing import List


class PurchaseItem(BaseModel):
    prd_id: int
    code: str
    name: str
    price: int
    qty: int


class PurchaseRequest(BaseModel):
    emp_cd: str
    store_cd: str
    pos_no: str
    payment_method: str
    items: List[PurchaseItem]


class PurchaseResponse(BaseModel):
    success: bool
    total_amt_ex_tax: int
    total_tax_amt: int
    total_amt: int
