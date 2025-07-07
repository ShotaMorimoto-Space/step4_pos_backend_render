# backend/app/models/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

# 商品マスタ
class Product(Base):
    __tablename__ = "product_master"

    prd_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False) 
    price = Column(Integer, nullable=False)     # 税抜価格
    image_url = Column(String(255))             # 商品画像URL（任意）

    details = relationship("TransactionDetail", back_populates="product")


# 取引ヘッダ
class Transaction(Base):
    __tablename__ = "transaction"

    trd_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    emp_cd = Column(CHAR(10), nullable=False, default="9999999999")
    store_cd = Column(CHAR(5), nullable=False, default="30")
    pos_no = Column(CHAR(3), nullable=False, default="90")
    total_amt = Column(Integer, nullable=False, default=0)
    total_amt_ex_tax = Column(Integer, nullable=False, default=0)
    total_tax_amt = Column(Integer, nullable=False, default=0)
    payment_method = Column(String(20), nullable=False)

    details = relationship("TransactionDetail", back_populates="transaction")


# 取引明細
class TransactionDetail(Base):
    __tablename__ = "transaction_detail"

    dtl_id = Column(Integer, primary_key=True, autoincrement=True)
    trd_id = Column(Integer, ForeignKey("transaction.trd_id"), nullable=False)
    prd_id = Column(Integer, ForeignKey("product_master.prd_id"), nullable=False)
    prd_code = Column(CHAR(13), nullable=False)
    prd_name = Column(String(100), nullable=False)  # nameを使うならこちらも100に合わせる
    prd_price = Column(Integer, nullable=False)     # 税抜価格
    qty = Column(Integer, nullable=False)
    tax_cd = Column(CHAR(2), nullable=False, default="10")

    transaction = relationship("Transaction", back_populates="details")
    product = relationship("Product", back_populates="details")
