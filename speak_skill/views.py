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
    talk_list = [
        {
         "id": 100,
         "title": "话术开场",
         "childs": [
             '恋爱调情',
             '趣味搭讪',
             '话题重新开场',
             '勾起好奇',
             '表情话术',
             '搭讪开场'
           ]
        },
        {
            "id": 101,
            "title": "幽默互动",
            "childs": [
                '自恋类别',
                '调侃类别',
                '打情骂俏',
                '共谋与赞美',
                '名人名言配文',
                '幽默聊天'
            ]
        },
        {
            "id": 102,
            "title": "初聊互动",
            "childs": [
                '情感链接',
                '共鸣故事',
                '废物测试',
                '异议处理',
                '冷读术',
                '框架筛选',
                '联系感建立',
                '话块连情',
                '化解IOD',
                '高价值展示',
                '价值型聊天',
                '初聊互动',
                '设立框架'
            ]
        },
        {
            "id": 103,
            "title": "感情升温",
            "childs": [
                '恋爱调情',
                '情感波动',
                '关系升高',
                '框架与拉升',
                '框架推拉',
                '隐性诱惑',
                '合约恋人',
                '文字进挪',
                '表达兴趣',
                '暧昧套路',
                '真心话大冒险'
            ]
        },
        {
            "id": 104,
            "title": "邀约技巧",
            "childs": [
                '预期建立',
                '邀约话术',
                '速约模板',
                '模糊邀约',
                '促成邀约'
            ]
        },
        {
            "id": 105,
            "title": "见面约会",
            "childs": [
                '聊天模板',
                '颜色星座手相',
                '互动与游戏',
                '现场聊天',
                '约会套路',
                '进挪与升级'
            ]
        }
    ]
    return jsonify(talk_list)


@speak_skill_bp.route('/chatdetail', methods=['POST'])
def post_chat_detail():
   categary = request.form.get('categary')
   pageNO = request.form.get('pageNO')
   pageSize = request.form.get('pageSize')
   pageNO = int(pageNO)
   pageSize = int(pageSize)
   res = emotion_db_manager.get_chat_detail(categary, pageNO, pageSize)
   list = []
   for item in res:
       list.append(item[4])
   return jsonify(list)



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


