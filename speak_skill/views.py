from . import speak_skill_bp
from flask import request, jsonify
from utils import  emotion_db_manager
import json




# 顶部滚动图
@speak_skill_bp.route('/scrollimages')
def get_scroll_images():
    return 'image1,image2,image3'


# 输入TA说的话
@speak_skill_bp.route('/search', methods=['POST'])
def search():
    return 'result'


# 表情包
@speak_skill_bp.route('/emotions')
def get_emotions():
    return 'emotions'


# 大家都在搜
@speak_skill_bp.route('/allfind/<int:index>')
def get_allfind(index):
    return 'allfind{}'.format(index)


# 每日必用
@speak_skill_bp.route('/everydayuse')
def get_everydayuse():
    return 'everydayuse'


# 开场
@speak_skill_bp.route('/startspeak')
def get_startspeak():
    return 'startspeak'


# 情绪
@speak_skill_bp.route('/emotion')
def get_emotion():
    return 'emotion'


# 聊天
@speak_skill_bp.route('/talk')
def get_talk():
    return 'talk'


# 恋爱蜜语
@speak_skill_bp.route('/lovetalk')
def get_lovetalk():
    return 'lovetalk'


# 约会
@speak_skill_bp.route('/apointment')
def get_apointment():
    return 'apointment'


# 通过频道获取不停类型的话术
@speak_skill_bp.route('/talkskill')
def get_talkskill():
    # channel_id = request.args.get('channel_id')
    # return 'talk skill channel: {}'.format(channel_id)
    talk_list = [
        {
         "id": 100,
         "title": "每日必用",
         "childs": [
                     {
                       "child_id":1001,
                       "child_title": "约会话题"
                     },
                     {
                         "child_id": 1002,
                         "child_title": "聊天开场白"
                     }
           ]
        },
        {
            "id": 200,
            "title": "开场",
            "childs": [
                {
                    "child_id": 2001,
                    "child_title": "搭讪开场"
                },
                {
                    "child_id": 2002,
                    "child_title": "勾起好奇"
                }
            ]
        }
    ]
    return jsonify(talk_list)


# @speak_skill_bp.route('/talkdetail', methods=['POST'])
#@speak_skill_bp.route('/talkdetail')
#def post_talk_detail():
#    res = emotion_db_manager.get_chat_detail_by_superID('44', 3, 20)
#    list = []
#    for item in res:
#        chat_id = item[0]
#        json_data = json.loads(item[2])
#        data = json_data.get('chat')
#        child_list = []
#        for child_item in data:
#            sex = child_item.get('sex')
#            content = child_item.get('content')
#            dic = {'sex': sex, 'content': content}
#            child_list.append(dic)
#        chat_dic = {'chat_id': chat_id, 'data': data}
#        print(chat_dic)
#        list.append(chat_dic)
#    return jsonify(list)

@speak_skill_bp.route('/talkdetail')
def post_talk_detail():
    res = emotion_db_manager.get_chat_detail_by_superID('44', 3, 5)
    list = []
    for item in res:
        chat_id = item[0]
        json_data = json.loads(item[2])
        data = json_data.get('chat')
        child_list = []
        for child_item in data:
            sex = child_item.get('sex')
            content = child_item.get('content')
            dic = {'sex': sex, 'content': content}
            child_list.append(dic)
        chat_dic = {'chat_id': chat_id, 'data': data}
        print(chat_dic)
        list.append(chat_dic)
    return jsonify(list)


