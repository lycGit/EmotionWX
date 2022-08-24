from flask import Blueprint

lesson_bp = Blueprint('lesson', __name__)

from . import views