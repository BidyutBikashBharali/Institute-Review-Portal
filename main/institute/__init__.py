from flask import Blueprint
from ..review import templates as tmp
from ..review import static as stc

trget_tmp = tmp
trget_stc = stc
institute_bp = Blueprint('institute', __name__, template_folder='trget_tmp',  static_folder='trget_stc',  static_url_path='/review/static')

from .views import *
from .form import *
from .find_dfi import *
from .okay import *
