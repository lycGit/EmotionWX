from . import lesson_bp
from flask import request, jsonify


@lesson_bp.route('/lesson')
def get_lesson():
    lesson_list = [
        {
            "id": 100,
            "title": "因敏感因素暂停板块，可咨询客服获取相关资料",
            "contact": "12345678",
            "count": "23",
            "students": "876"
        },
        {
            "id": 101,
            "title": "因敏感因素暂停板块，可咨询客服获取相关资料",
            "contact": "12345678",
            "count": "23",
            "students": "876"
        },
        {
            "id": 102,
            "title": "因敏感因素暂停板块，可咨询客服获取相关资料",
            "contact": "12345678",
            "count": "23",
            "students": "876"
        },
        {
            "id": 103,
            "title": "因敏感因素暂停板块，可咨询客服获取相关资料",
            "contact": "12345678",
            "count": "23",
            "students": "876"
        },
        {
            "id": 104,
            "title": "因敏感因素暂停板块，可咨询客服获取相关资料",
            "contact": "12345678",
            "count": "23",
            "students": "876"
        },
        {
            "id": 105,
            "title": "因敏感因素暂停板块，可咨询客服获取相关资料",
            "contact": "12345678",
            "count": "23",
            "students": "876"
        }
    ]
    return jsonify(lesson_list)