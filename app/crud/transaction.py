# backend/app/crud/transaction.py

from sqlalchemy.orm import Session
from app.models.models import Transaction, TransactionDetail
from app.schemas.purchase import PurchaseRequest
from app.utils.tax import calculate_tax

def create_transaction(db: Session, purchase: PurchaseRequest):
    # 取引ヘッダを仮登録（合計0円で登録）
    trd = Transaction(
        emp_cd=purchase.emp_cd or "9999999999",
        store_cd=purchase.store_cd or "30",
        pos_no=purchase.pos_no or "90",
        payment_method=purchase.payment_method,
    )
    db.add(trd)
    db.flush()  # trd_id を取得するため

    # 明細を登録しながら合計を計算
    total_ex = 0
    for item in purchase.items:
        subtotal = item.price * item.qty
        detail = TransactionDetail(
            trd_id=trd.trd_id,
            prd_id=item.prd_id,
            prd_code=item.code,
            prd_name=item.name,
            prd_price=item.price,
            qty=item.qty,
            tax_cd="10"
        )
        db.add(detail)
        total_ex += subtotal

    total_tax = calculate_tax(total_ex)
    total_amt = total_ex + total_tax

    # 取引ヘッダを更新
    trd.total_amt_ex_tax = total_ex
    trd.total_tax_amt = total_tax
    trd.total_amt = total_amt

    db.commit()
    return total_ex, total_tax, total_amt
