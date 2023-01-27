from . import lesson_bp
from flask import request, jsonify


@lesson_bp.route('/lesson')
def get_lesson():
    lesson_list = [
        {
            "id": 100,
            "title": "形象打造的重要性",
            "contact": "会员加微信免费获取",
            "count": "4",
            "students": "7876"
        },
        {
            "id": 101,
            "title": "教你30天打造高品质朋友圈",
            "contact": "会员加微信免费获取",
            "count": "5",
            "students": "4309"
        },
        {
            "id": 102,
            "title": "搭讪的艺术",
            "contact": "会员加微信免费获取",
            "count": "9",
            "students": "9876"
        },
        {
            "id": 103,
            "title": "聊天技巧课",
            "contact": "会员加微信免费获取",
            "count": "16",
            "students": "20876"
        },
        {
            "id": 104,
            "title": "恋爱术-吸引力构建",
            "contact": "会员加微信免费获取",
            "count": "12",
            "students": "7205"
        },
        {
            "id": 105,
            "title": "把控女生心理",
            "contact": "会员加微信免费获取",
            "count": "66",
            "students": "6276"
        },
        {
            "id": 106,
            "title": "约会的技巧",
            "contact": "会员加微信免费获取",
            "count": "14",
            "students": "8539"
        },
        {
            "id": 107,
            "title": "私房建设",
            "contact": "会员加微信免费获取",
            "count": "8",
            "students": "5801"
        },
        {
            "id": 108,
            "title": "长期关系相处",
            "contact": "会员加微信免费获取",
            "count": "6",
            "students": "4290"
        },
        {
            "id": 109,
            "title": "找个好老婆",
            "contact": "会员加微信免费获取",
            "count": "11",
            "students": "7652"
        },
        {
            "id": 110,
            "title": "这样聊更吸引她",
            "contact": "会员加微信免费获取",
            "count": "30",
            "students": "9341"
        },
        {
            "id": 111,
            "title": "掌握爱情主动权",
            "contact": "会员加微信免费获取",
            "count": "8",
            "students": "6305"
        },
        {
            "id": 112,
            "title": "恋商特训",
            "contact": "会员加微信免费获取",
            "count": "11",
            "students": "8953"
        },
        {
            "id": 113,
            "title": "聊天精品课",
            "contact": "会员加微信免费获取",
            "count": "11",
            "students": "9531"
        },
        {
            "id": 114,
            "title": "挽回爱情秘籍",
            "contact": "会员加微信免费获取",
            "count": "20",
            "students": "7438"
        },
        {
            "id": 115,
            "title": "恋爱心理学",
            "contact": "会员加微信免费获取",
            "count": "38",
            "students": "7548"
        },
        {
            "id": 116,
            "title": "女士形象课程",
            "contact": "会员加微信免费获取",
            "count": "22",
            "students": "9328"
        },
        {
            "id": 117,
            "title": "男士形象",
            "contact": "会员加微信免费获取",
            "count": "10",
            "students": "6793"
        }
    ]
    return jsonify(lesson_list)