from flask import Blueprint

speak_skill_bp = Blueprint('speakskill', __name__, static_folder='images', static_url_path='/img')


from . import views
