from . import my_bp
from flask import request
from flask import redirect
from flask import jsonify
import random


# 填写激活码
@my_bp.route('/activecode', methods=['POST'])
def post_activeCode():
    code = request.args.get('code')
    return code


# 投诉建议
@my_bp.route('/suggestion', methods=['POST'])
def post_suggestion():
    contact = request.args.get('contact')
    content = request.args.get('content')
    return contact


@my_bp.route('/version', methods=['POST'])
def post_version():
    return '1.0.0'


# @my_bp.route('/phoneNum/<mobile:phoneNum>')
# def get_phoneNum(phoneNum):
#     return 'phone num is: '.format(phoneNum)


# http://127.0.0.1:5000/my/upload
@my_bp.route('/upload', methods=['POST'])
def post_upload():
    f = request.files['pic']
    with open('../my/images/image.png', 'wb') as new_file:
        new_file.write(f.read())
    return 'success'


# 用户协议
@my_bp.route('/redirect')
def get_agreement():
    return redirect('http://www.baidu.com')


@my_bp.route('/pricelist')
def get_pricelist():
    pricelist = [
        {
            "name": '7天会员',
            "price": '18.8元',
            "oldprice": '58.8元'
        },
        {
            "name": '年卡会员',
            "price": '38.8元',
            "oldprice": '298.8元'
        },
        {
            "name": '终身会员',
            "price": '68.8元',
            "oldprice": '488.8元'
        }
    ]
    return jsonify(pricelist)


@my_bp.route('/scollerlist')
def get_scollerlist():
    # usableName_char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/"  # 可作为用户名的字符
    # e_userName = []  # 定义一个临时List变量,使用list.append添加字符
    # scollerlist = []
    # for i in range(100):
    #
    #     for j in range(8):
    #         e_userName.append(random.choice(usableName_char))
    #     userName = ''.join(e_userName)
    #     scollerlist.append(userName)
    scollerlist = []
    nikenames = get_wxnikename()
    for i in range(len(nikenames)):
        nikename = nikenames[i]
        num = random.randrange(1, 6, 1)
        if num == 1:
            nikename = nikename + '刚刚购买了7天会员'
        elif num == 2 | num == 3:
            nikename = nikename + '刚刚购买了年卡会员'
        else:
            nikename = nikename + '刚刚购买了终身会员'
        scollerlist.append(nikename)
    return jsonify(scollerlist)


def get_wxnikename():
    nikenames = [
        "花重月数",
        "旧梦如风",
        "蝶舞庄周",
        "绿逾初夏",
        "余笙南吟",
        "陈情匿旧酒",
        "白桃乌龙",
        "清浅ˋ旧时光",
        "荒碎梦残",
        "无梦相赠",
        "离人泪",
        "伊人在水一方",
        "与我共梦",
        "挽弦暮笙",
        "开始厌倦",
        "仙女收纳盒",
        "華燈初上",
        "袖手今生",
        "ら道不清的忧伤",
        "凉生",
        "墨香九歌",
        "暖栀",
        "等待许了苍老",
        "此昵称不存在",
        "长风",
        "残阳暮雪",
        "点到为止",
        "素衣风尘叹",
        "半心人",
        "笑低了眉眼",
        "明媚殇",
        "暖梦旧歌",
        "偏爱",
        "剑魄琴心",
        "凉笙墨染",
        "男医",
        "不谙世事",
        "纯净的眸子",
        "橘子风车",
        "醉过无痕",
        "悠悠我心",
        "只倾心不倾城",
        "心安是归处",
        "天凝",
        "心思爆甜",
        "若羽ぬ",
        "旧念何挽",
        "静已思之愈脓",
        "白鹿",
        "歌满长安"
    ]
    return nikenames


@my_bp.route('/profilelist')
def get_profilelist():
    profilelist = [
        {
            "icon": 'tianxiejihuoma.png',
            "title": '版本',
            "discribe": '1.0.1'
        },
        {
            "icon": 'aichat.png',
            "title": '投诉建议',
            "discribe": '微信号码：充会员可获取'
        },
        {
            "icon": 'lianxikefu.png',
            "title": '联系客服',
            "discribe": '微信号码：充会员可获取'
        }
    ]
    return jsonify(profilelist)


# 恋爱蜜语
@my_bp.route('/validversion')
def get_validversion():
    return "1.0.5"
    # version = request.args.get('version')
    # print(version)
    # if int(version) > 1:
    #     return 'True'
    # else:
    #     return "False"
