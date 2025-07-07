import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.db.database import engine, Base, SessionLocal
from app.models.models import Product

def init():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

    # DB セッションを作成
    db = SessionLocal()

    # 初期データ（例: 商品マスター）
    products = [
        Product(prd_id=1, code="4901991707212", name="モノポケット（ホワイト）", price=220, image_url=None),
        Product(prd_id=2, code="4901991707229", name="モノポケット（ブラック）", price=220, image_url=None),
        Product(prd_id=3, code="4901991707236", name="モノポケット（ブルー）", price=220, image_url=None),
        Product(prd_id=4, code="4901991707243", name="モノポケット（ピンク）", price=220, image_url=None),
        Product(prd_id=5, code="4901991707250", name="モノポケット（パープル）", price=220, image_url=None),
    ]

    # 既存データがない場合のみ追加（重複防止）
    if db.query(Product).count() == 0:
        db.add_all(products)
        db.commit()
        print("Initial products inserted.")
    else:
        print("Products already exist. Skipping insert.")

    db.close()
    print("Done.")

if __name__ == "__main__":
    init()