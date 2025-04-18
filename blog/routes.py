from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from ..models import Post
from .. import db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    """显示所有博客文章"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/post/<int:post_id>')
def post(post_id):
    """显示单篇博客文章"""
    post = Post.query.get_or_404(post_id)
    return render_template('blog/post.html', post=post)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    """创建新文章"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('标题和内容不能为空', 'error')
            return redirect(url_for('blog.create'))
            
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        flash('文章创建成功', 'success')
        return redirect(url_for('blog.index'))
        
    return render_template('blog/create.html')

@bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    """编辑文章"""
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.updated_at = datetime.utcnow()
        db.session.commit()
        flash('文章更新成功', 'success')
        return redirect(url_for('blog.post', post_id=post.id))
        
    return render_template('blog/edit.html', post=post)

@bp.route('/about')
def about():
    """关于页面"""
    return render_template('blog/about.html')

@bp.route('/contact')
def contact():
    """联系页面"""
    return render_template('blog/contact.html')
