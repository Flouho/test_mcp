from flask import Flask
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
import markdown2
from flask import Markup

db = SQLAlchemy()
from config import Config
import markdown2
from flask import Markup
import os
from extensions import db

def create_app():
    """应用工厂函数"""
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 初始化数据库
    db.init_app(app)
    
    # 注册蓝图
    from blog import bp as blog_bp
    app.register_blueprint(blog_bp)
    
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
    app.run(host='0.0.0.0', port=5000, debug=True)
