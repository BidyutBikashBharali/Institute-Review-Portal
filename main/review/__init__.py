from flask import Blueprint

review_bp = Blueprint('review', __name__, url_prefix='/reviews', template_folder='templates', static_folder='static',  static_url_path='/review/static')

from .views import *
from .form import *
