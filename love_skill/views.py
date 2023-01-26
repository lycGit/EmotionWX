#coding:utf-8
import os

from werkzeug.utils import redirect

from . import love_skill_bp
from flask import request, jsonify, Response, send_file
from utils import  emotion_db_manager
from flask import render_template
import json
import webbrowser


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


# 恋爱蜜语
@love_skill_bp.route('/skilldetail')
def get_skilldetail():
    artid = request.args.get('artid')
    res = emotion_db_manager.get_love_lesson_detail(int(artid))
    out_html = render_template("love_skill.html", html_content=res[0][4])
    return out_html, "200 Ok", {"Content-type": "text/html"}
    # response = Response()
    # response.data = out_html
    # response.headers = {"Content-type": "text/html"}
    # return out_html


# 恋爱蜜语
@love_skill_bp.route('/skillhtmldetail')
def get_skill_html_detail():
    artid = request.args.get('artid')
    project_path = os.path.abspath(".")

    file_path = str(artid) + ".html"
    # GEN_HTML = project_path + '/static_files/' + file_path
    GEN_HTML = project_path + '/main/static_files/' + file_path
    print(GEN_HTML)
    if os.access(GEN_HTML, os.F_OK):
        # 发送文件
        # return send_file('love_skill/html/1698.html', GEN_HTML)
        # redirectUrl = 'http://127.0.0.1:5000/source/' + file_path
        redirectUrl = 'https://www.qgsq.space/' + file_path
        return redirect(redirectUrl)
    else:
        print('has excute')

        # 打开文件，准备写入
        f = open(GEN_HTML, 'w')
        res = emotion_db_manager.get_love_lesson_detail(int(artid))
        # 准备相关变量
        # 写入HTML界面中
        message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title> %s </title>
        </head>
        <body>
           %s
        </body>
        </html>
        """ % (res[0][3], res[0][4])
        print(res)
        # 写入文件
        f.write(message)
        # 关闭文件
        f.close()
        # redirectUrl = 'http://127.0.0.1:5000/source/' + file_path
        redirectUrl = 'https://www.qgsq.space/' + file_path
        return redirect(redirectUrl)