from app import create_app, db
from models import Post

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    print(f"Database tables created: {db.metadata.tables.keys()}")
