#coding:utf-8
import os

from . import love_skill_bp
from flask import request, jsonify
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
    return render_template("love_skill.html", html_content=res[0][4])


# # 恋爱蜜语
# @love_skill_bp.route('/skilldetail')
# def get_skilldetail():
#     artid = request.args.get('artid')
#     # 命名生成的html
#     project_path = os.path.abspath(os.path.dirname(__file__))
#     file_list_path = project_path + "/html/"
#     file_path = str(artid) + ".html"
#     GEN_HTML = file_list_path + file_path
#     if os.access(GEN_HTML, os.F_OK):
#         return render_template(GEN_HTML)
#         # return render_template(("mod1.html",html_content = name))
#     else:
#         print('has excute')
#
#         # 打开文件，准备写入
#         f = open(GEN_HTML, 'w')
#         res = emotion_db_manager.get_love_lesson_detail(int(artid))
#         # 准备相关变量
#         # 写入HTML界面中
#         message = """
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <title>Title</title>
#         </head>
#         <body>
#            %s
#         </body>
#         </html>
#         """ % (res[0][4])
#         print(GEN_HTML)
#         # 写入文件
#         f.write(message)
#         # 关闭文件
#         f.close()
#         # return file_path
#         return render_template(GEN_HTML)