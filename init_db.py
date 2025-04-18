from app import app, db
from app import Post  # 确保Post模型在app.py中定义

with app.app_context():
    db.create_all()
    print("数据库表已成功创建")
