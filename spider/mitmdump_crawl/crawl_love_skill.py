import json
import csv


def response(flow):
    print("aaaaaaa")
    if flow.request.url.find("do=index") != -1:
        text = flow.response.get_text()
        json_data = json.loads(text)
        csvfile = open('/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/skiLl_case.csv',
                       'a')  # 处理后的数据写入csv文件 , encoding='utf-8'
        csv_wri = csv.writer(csvfile)
        all_data = json_data.get('data')
        chatcase = all_data.get('chatcase')
        print(chatcase)
        for case in chatcase:
            origin_id = case.get('id')
            title = case.get('title')
            content = case.get('content')
            category_id = case.get('category_id')
            img = case.get('thumb')
            csvItem = [origin_id, title, content, category_id, img]
            csv_wri.writerow(csvItem)

        pickskill = all_data.get('pickskill')
        for skill in pickskill:
            origin_id = skill.get('id')
            title = skill.get('title')
            content = skill.get('content')
            category_id = skill.get('category_id')
            img = skill.get('thumb')
            csvItem = [origin_id, title, content, category_id, img]
            csv_wri.writerow(csvItem)