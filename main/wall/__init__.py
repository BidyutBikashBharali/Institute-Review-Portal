from flask import Blueprint
from ..review import templates as b_t 
from ..review import static as b_s
bt = b_t
bs = b_s
wall_bp = Blueprint('wall', __name__, template_folder='bt', static_folder='bs',  static_url_path='/wall/static')

from .views import *
