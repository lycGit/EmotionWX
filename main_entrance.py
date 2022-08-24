from flask import Flask

import pymysql
from flask import jsonify
import json


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


if __name__ == '__main__':
    app.run()