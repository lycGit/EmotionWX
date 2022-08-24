# -*- coding: utf-8 -*-
# from utils import mysql_manager
import json
import csv
import os


def response(flow):
    # 创建表
    # create_lesson_list_table()
    # list_1 = ['name', 'height']
    # file_path = 'lesson.csv'
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     csv_writer = csv.writer(f)
    #     csv_writer.writerow(list_1)
    if flow.request.url.find("do=getnews") != -1:
        text = flow.response.get_text()
        json_data = json.loads(text)
        csvfile = open('/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/lesson.csv', 'a')  # 处理后的数据写入csv文件 , encoding='utf-8'
        csv_wri = csv.writer(csvfile)
        for lesson in json_data:
            origin_id = lesson.get('id')
            title = lesson.get('title')
            print(title + "------end")
            content = lesson.get('content')
            category_id = lesson.get('categoryid')
            img = lesson.get('img')
            csvItem = [origin_id, title, content, category_id, img]
            csv_wri.writerow(csvItem)
    # insert_lesson_list_table(origin_id, title, content, category_id, img)
    #     print(text + "------end")


# # 创建课程列表
# def create_lesson_list_table():
#     sql = """
#     CREATE TABLE IF NOT EXISTS  lesson_list_table(
#     id bigint(20) unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'ID',
#     origin_id bigint(20) unsigned NOT NULL COMMENT '原始ID',
#     title varchar(128) NOT NULL COMMENT '标题',
#     content varchar(1024) NOT NULL COMMENT '内容',
#     categoryid bigint(20) unsigned NOT NULL COMMENT '课程分类',
#     img varchar(128) NOT NULL COMMENT '图片url',
#     is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程列表';
#     """
#     mysql_manager.excuse_sql(sql)
#
#
# # 创建课程列表
# def insert_lesson_list_table(self, origin_id, title, content, category_id, img):
#     sql = " INSERT INTO lesson_list_table (origin_id, title, content, category_id, img) VALUES ({origin_id}," \
#           " {title}, {content}, {category_id}, {img})".format(origin_id=origin_id, title=title, content=content, category_id=category_id, img=img)
#     mysql_manager.excuse_sql(sql)