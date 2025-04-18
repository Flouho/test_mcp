from app import create_app
from models import Post

app = create_app()
with app.app_context():
    post = Post.query.first()
    if post:
        print("=== Database Content ===")
        print(post.content)
        print("\n=== Rendered Markdown ===")
        import markdown
        md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite'])
        print(md.convert(post.content))
    else:
        print("No posts found in database")
