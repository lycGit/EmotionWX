
from flask import Flask, redirect, request, url_for

import pymysql
from flask import jsonify
import json

import weixin
from weixin.pay import WeixinPay, WeixinPayError
from weixin.login import WeixinLogin
from datetime import datetime, timedelta
from utils import emotion_db_manager

app = Flask(__name__, static_url_path='/s', static_folder='static_files')
app.config.from_pyfile('./config/setting.py')

from speak_skill import speak_skill_bp
app.register_blueprint(speak_skill_bp, url_prefix='/speakskill')

from speak_case import speak_case_bp
app.register_blueprint(speak_case_bp, url_prefix='/speakcase')

from love_skill import love_skill_bp
app.register_blueprint(love_skill_bp, url_prefix='/loveskill')

from lesson import lesson_bp
app.register_blueprint(lesson_bp, url_prefix='/lesson')

from my import my_bp
app.register_blueprint(my_bp, url_prefix='/my')

# 以下暂时废弃
# # 创建表
# mysql_manager.create_user_table()
# 以上暂时废弃

#emotion_db_manager.get_chat_detail_by_superID('44', 3, 20)
# emotion_db_manager.init_chat_detail_table()
# emotion_db_manager.init_love_lesson_table()
def connect_database():
    conn = pymysql.connect(host="localhost", port=3306, user='root', password='1', database='emotionwx',charset='utf8')
    return conn


@app.route('/idlist')
def getIdlist():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Lyc198901', db='emotionwx')
    cursor = conn.cursor()
    cursor.execute("select * from chat_detail_table where superID = '44'")
    res = cursor.fetchall()
    list = []
    for item in res:
        chat_id = item[0]
        list.append(chat_id)
        print(list)
        
    return jsonify(list)

# 以下暂时废弃
#from spider import crawl_friend_emtion
# crawl_friend_emtion.crawl_gif_image('https:\/\/guanwangimg.hezeyq.com\/images\/1548\/2020\/09\/m7XhcslddHnB46KVNnOL65Roox441Z.gif')
# crawl_friend_emtion.read_crawl_content()
# crawl_friend_emtion.scan_all_files('/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/crawl_gif_images')
# crawl_friend_emtion.crawl_mp3s('https://guanwangimg.hezeyq.com//audios//1548//2020//09//OlQ9lS9J9SLHhTKTTV0DLo9jTlknH9.mp3')

# list_1 = ['name', 'height']
# file_path = '/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/lesson.csv'
# with open(file_path, 'w', encoding='utf-8') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(list_1)
# 以上暂时废弃


@app.route('/')
def entrance():
    return app.config['SECRET_KEY']


app_id = 'wx0d2e888ad62439ce'
app_secret = '32f27b9d55ed2af15834632db0e4708c'
wx_login = WeixinLogin(app_id, app_secret)


@app.route("/login")
def login():
    openid = request.cookies.get("openid")
    next = request.args.get("next") or request.referrer or "/",
    if openid:
        return redirect(next)

    callback = url_for("authorized", next=next, _external=True)
    url = wx_login.authorize(callback, "snsapi_base")
    return redirect(url)


@app.route("/authorized")
def authorized():
    code = request.args.get("code")
    if not code:
        return "ERR_INVALID_CODE", 400
    next = request.args.get("next", "/")
    data = wx_login.access_token(code)
    openid = data.openid
    resp = redirect(next)
    expires = datetime.now() + timedelta(days=1)
    resp.set_cookie("openid", openid, expires=expires, secure=True, httponly=True, samesite='Lax')
    return resp

mch_id = "1630874134"
mch_key = "abc123def456ghi789jkm123nop456qr"
notify_url = "https://www.qgsq.space/pay/notify"
wx_pay = WeixinPay(app_id, mch_id, mch_key, "notify_url")


@app.route("/pay/create", methods=['POST'])
def pay_create():
    openid = request.form.get('openid')
    """
    微信JSAPI创建统一订单，并且生成参数给JS调用
    """
    out_trade_no = wx_pay.nonce_str
    raw = wx_pay.jsapi(openid=openid, body=u"测试", out_trade_no=out_trade_no, total_fee=1)
    return jsonify(raw)

    # try:
    #     out_trade_no = wx_pay.nonce_str
    #     raw = wx_pay.jsapi(openid="openid", body=u"测试", out_trade_no=out_trade_no, total_fee=1)
    #     return jsonify(raw)
    # except WeixinPayError, e:
    #     print e.message
    #     return e.message, 400


@app.route("/pay/notify", methods=["POST"])
def pay_notify():
    """
    微信异步通知
    """
    data = wx_pay.to_dict(request.data)
    if not wx_pay.check(data):
        return wx_pay.reply("签名验证失败", False)
    # 处理业务逻辑
    return wx_pay.reply("OK", True)



if __name__ == '__main__':
    app.run()