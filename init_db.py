from app import create_app, db
from blog.models import Post

app = create_app()
with app.app_context():
    db.create_all()
    print("数据库表已成功创建")
