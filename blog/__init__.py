from flask import Blueprint

bp = Blueprint('blog', __name__, template_folder='templates')

from . import views  # Moved import after bp definition to resolve circular dependency
