from flask import Blueprint
# from config.my_regex import MobileConverter

my_bp = Blueprint('my', __name__)

# my_bp.url_map.converters['mobile'] = MobileConverter
from . import views