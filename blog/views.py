from flask import render_template, request, redirect, url_for
from . import bp
import markdown
import markdown_katex

@bp.route('/')
def index():
    from models import Post
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            return "标题和内容不能为空", 400
            
        from app import db
        from models import Post
        
        try:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        except Exception as e:
            db.session.rollback()
            return f"保存失败: {str(e)}", 500
    return render_template('create.html')

@bp.route('/post/<int:post_id>')
def post(post_id):
    from models import Post
    post = Post.query.get_or_404(post_id)
    # Process content while preserving math formulas
    content = post.content
    
    # Split content into math and non-math segments
    segments = []
    last_end = 0
    import re
    
    # Match all math blocks
    for match in re.finditer(r'(?s)(\$\$.*?\$\$|\$[^\$].*?[^\$]\$|\\\(.*?\\\)|\\\[.*?\\\])', content):
        # Add preceding non-math content
        if match.start() > last_end:
            non_math = content[last_end:match.start()]
            md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite'])
            segments.append(md.convert(non_math))
        
        # Add math block as-is
        segments.append(match.group(0))
        last_end = match.end()
    
    # Add remaining non-math content
    if last_end < len(content):
        non_math = content[last_end:]
        md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite'])
        segments.append(md.convert(non_math))
    
    # Combine all segments
    post.content = ''.join(segments)
    return render_template('post.html', post=post)

@bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    from models import Post
    from app import db
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        
        if not post.title or not post.content:
            return "标题和内容不能为空", 400
            
        try:
            db.session.commit()
            return redirect(url_for('blog.post', post_id=post.id))
        except Exception as e:
            db.session.rollback()
            return f"更新失败: {str(e)}", 500
    
    return render_template('edit.html', post=post)

@bp.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    from models import Post
    from app import db
    post = Post.query.get_or_404(post_id)
    
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    except Exception as e:
        db.session.rollback()
        return f"删除失败: {str(e)}", 500
