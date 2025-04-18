from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import markdown2
from flask import Markup
import os

def create_app():
    """应用工厂函数"""
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
    app.config.from_object(Config)
    
    # 初始化数据库
    db = SQLAlchemy(app)
    db.init_app(app)
    
    # 注册蓝图
    from blog.routes import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/')
    
    # 注册模板过滤器
    @app.template_filter('markdown')
    def markdown_filter(text):
        """Markdown转HTML过滤器"""
        if not text:
            return ""
        html = markdown2.markdown(text, extras=["fenced-code-blocks", "tables"])
        return Markup(html)
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
