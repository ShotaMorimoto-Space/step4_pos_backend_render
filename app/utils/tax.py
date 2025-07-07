# backend/app/utils/tax.py

def calculate_tax(amount: int) -> int:
    return int(amount * 0.1)  # 切り捨て方式
