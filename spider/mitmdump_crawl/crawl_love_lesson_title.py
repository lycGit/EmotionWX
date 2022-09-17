# -*- coding: utf-8 -*-
# from utils import mysql_manager
import json
import csv
import os


def response(flow):
    # 创建表
    if flow.request.url.find("do=courselist") != -1:
        text = flow.response.get_text()
        json_data = json.loads(text)
        csvfile = open('/Users/liuyangcheng/Desktop/LearnClass/WXProgram/Service/EmotionWX/spider/mitmdump_crawl/lessenlist.csv', 'a')  # 处理后的数据写入csv文件 , encoding='utf-8'
        csv_wri = csv.writer(csvfile)
        # print(json_data)
        for item in json_data['data']['art']:
            artid = item.get('artid')
            title = item.get('title')
            addtime = item.get('addtime')
            print(title + "------end")
            csvItem = [artid, title, addtime]
            csv_wri.writerow(csvItem)

