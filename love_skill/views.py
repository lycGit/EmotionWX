from . import love_skill_bp
from flask import request, jsonify
from utils import  emotion_db_manager
import json


@love_skill_bp.route('/loveskill', methods=['POST'])
def get_love_skill():
    pageNO = request.form.get('pageNO')
    pageSize = request.form.get('pageSize')
    pageNO = int(pageNO)
    pageSize = int(pageSize)
    res = emotion_db_manager.get_love_lesson_title_table(pageNO, pageSize)
    list = []
    for item in res:
        dic = {
            'artid': item[1],
            'title': item[2],
            'date': item[3]
        }
        list.append(dic)
    return jsonify(list)


