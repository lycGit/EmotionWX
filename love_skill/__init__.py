from flask import Blueprint

love_skill_bp = Blueprint('loveskill', __name__)

from . import views