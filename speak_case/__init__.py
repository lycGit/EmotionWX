from flask import Blueprint


speak_case_bp = Blueprint('speak_case', __name__)


from . import views