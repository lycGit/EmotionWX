from . import lesson_bp
from flask import request, jsonify
from utils import  emotion_db_manager
import json

@lesson_bp.route('/lesson')
def get_lesson():
    return 'lesson'


@lesson_bp.route('/lessonlist', methods=['POST'])
def post_lesson_list():
   categary = request.form.get('categary')
   res = emotion_db_manager.get_chat_detail(categary, 1, 20)
   list = []
   for item in res:
       list.append(item[4])
   return jsonify(list)