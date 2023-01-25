from . import lesson_bp
from flask import request, jsonify


@lesson_bp.route('/lesson')
def get_lesson():
    lesson_list = [
        {
            "id": 100,
            "title": "恋爱速成课，可咨询客服获取相关资料",
            "contact": "Anyinchashe",
            "count": "48",
            "students": "7876"
        },
        {
            "id": 101,
            "title": "恋爱心理学教程，可咨询客服获取相关资料",
            "contact": "Anyinchashe",
            "count": "33",
            "students": "4309"
        },
        {
            "id": 102,
            "title": "社交情商吸引力训练课程，可咨询客服获取相关资料",
            "contact": "Anyinchashe",
            "count": "42",
            "students": "9876"
        },
        {
            "id": 103,
            "title": "形象打造课程，可咨询客服获取相关资料",
            "contact": "Anyinchashe",
            "count": "23",
            "students": "20876"
        },
        {
            "id": 104,
            "title": "搭讪的艺术课程，可咨询客服获取相关资料",
            "contact": "Anyinchashe",
            "count": "50",
            "students": "7205"
        },
        {
            "id": 105,
            "title": "恋商特训课程，可咨询客服获取相关资料",
            "contact": "Anyinchashe",
            "count": "66",
            "students": "6276"
        }
    ]
    return jsonify(lesson_list)