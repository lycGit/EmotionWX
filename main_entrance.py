from flask import Flask
import requests
import pymysql
from flask import jsonify
from flask import Flask, redirect, request, url_for
import json
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
# emotion_db_manager.init_love_lesson_title_table()
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



@app.route("/getopenid")
def getopenid():
    code = request.args.get("code")
    # appi与secret,可以将其存入数据库中获取
    appid = app_id
    secret = app_secret
    grant_type = 'authorization_code'
    url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}' \
          f'&secret={secret}&js_code={code}&grant_type={grant_type}'
    res = requests.get(url).json()
    return res


mch_id = "1630874134"
mch_key = "abc123def456ghi789jkm123nop456qr"
notify_url = "https://www.qgsq.space/pay/notify"



import datetime
import random
import string
import time
import requests
import xmltodict



# 生成32位随机字符串
def randomStr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 32))


# 发送xml请求
def send_xml_request(url, param):
    xml = "<xml>{0}</xml>".format("".join(["<{0}>{1}</{0}>".format(k, v) for k, v in param.items()]))
    response = requests.post(url, data=xml.encode('utf-8'))
    msg = response.text
    xmlmsg = xmltodict.parse(msg)
    return xmlmsg


#@app.route("/pay/create", methods=['POST'])
@app.route("/pay/create")
def pay_create():
    openid = request.args.get('openid')
    order_id = request.args.get('orderid')
    # 获取发送请求的ip地址，参数字典中需要使用
    ip = request.args.get('REMOTE_ADDR')
    # try:
    # 获取当前时间
    now_time = datetime.datetime.now()
    # 我这里在小程序端处理，传订单号的判断为之前为支付的订单，没有的表示新建订单
    if not order_id:
        # 根据时间生成订单号这里可自定义
        out_trade_no = now_time.strftime('%Y%m%d%H%M%S') + str(random.randrange(1000, 9999))
        # 数据库存储订单，根据自己的订单字段来，我这里106表示未支付
        # order_obj = OrderTable.objects.create(
        #     openid=openid,
        #     order_time=now_time,
        #     order_num=out_trade_no,
        #     price=3,
        #     order_status='106'
        # )
        # order_obj.save()
    else:
        out_trade_no = order_id

    # 生成随机字符串
    nonce_str = randomStr()
    # 参数字典1存储订单信息
    params = {
        # 小程序的appid, 可将appid与mchid存入数据库中
        'appid': app_id,
        'attach': 'tes',
        'body': 'test',
        # 商户id
        'mch_id': mch_id,
        # 商品描述
        # 'description': '',
        # 随机32位字符串
        'nonce_str': nonce_str,
        # 支付成功后微信官方回复地址, 要求必须为https地址，填写你的接口地址
        'notify_url': 'https://www.qgsq.space/pay/notify',
        # 用户标识
        "openid": openid,
        # 商户订单号
        'out_trade_no': out_trade_no,
        'spbill_create_ip': ip,
        # "amount": {"total": 1, "currency": "CNY"},
        # 订单总金额，单位fen，我这里定义了3元
        "total_fee": '1',
        # "payer": {"openid": openid},
        # 交易类型
        'trade_type': 'JSAPI',
    }
    # 签名(md5加密params)，MCHKEY为商户2级key
    temp = "&".join(
        ["{0}={1}".format(k, params[k]) for k in sorted(params)] + ["{0}={1}".format("key", mch_key, ), ]
    )
    h1 = hashlib.md5()
    h1.update(temp.encode(encoding='utf8'))
    sign = h1.hexdigest().upper()
    # 将密文存入params
    params['sign'] = sign
    # 支付访问微信
    url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
    # url = "https://api.mch.weixin.qq.com/v3/pay/transactions/jsapi"
    # 发送xml请求
    xmlmsg = send_xml_request(url, params)
    # 请求成功
    if xmlmsg['xml']['return_code'] == 'SUCCESS':
        prepay_id = xmlmsg['xml']['prepay_id']
        timeStamp = str(int(time.time()))
        # 再次签名，生成参数字典2
        data = {
            'appId': app_id,
            'nonceStr': nonce_str,
            'package': 'prepay_id=' + prepay_id,
            'signType': 'MD5',
            'timeStamp': timeStamp,
        }
        # 签名，MCHKEY为商户2级key
        temp = "&".join(
            ["{0}={1}".format(k, data[k]) for k in sorted(data)] + [
                "{0}={1}".format("key", mch_key, ), ]
        )
        h2 = hashlib.md5()
        h2.update(temp.encode(encoding='utf8'))
        paySign = h2.hexdigest().upper()
        data['paySign'] = paySign
        return jsonify({'data': data, 'code': 200})
    #     else:
    #         return jsonify({'code': 400})
    # except:
    #     return jsonify({'code': 500})


import hashlib
from xml.etree import ElementTree as ET


@app.route("/pay/notify", methods=["POST"])
def pay_notify():
    """
    微信异步通知
    """
    # 1.获取结果吧XML转换为字典格式
    root = ET.XML(requests.body.decode('utf-8'))
    result = {child.tag: child.text for child in root}

    # 校验签名是否正确防止恶意请求
    sign = result.pop('sign')
    temp = "&".join(
        ["{0}={1}".format(k, result[k]) for k in sorted(result)] + [
            "{0}={1}".format("key", mch_key, ), ]
    )
    h1 = hashlib.md5()
    h1.update(temp.encode(encoding='utf8'))
    local_sign = h1.hexdigest().upper()
    # 签名一致
    if local_sign == sign:
        # 根据订单号修改订单状态
        out_trade_no = result.get('out_trade_no')
        # order_obj = OrderTable.objects.filter(order_num=out_trade_no)
        # order_obj.update(order_status='103')
        response = """<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>"""
        return response



if __name__ == '__main__':
    app.run()