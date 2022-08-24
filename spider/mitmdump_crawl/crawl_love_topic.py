import json
import csv

# 获取小类具体的聊天技巧数据
# def response(flow):
#     if flow.request.url.find("do=list") != -1:
#         text = flow.response.get_text()
#         json_data = json.loads(text)
#         all_data = json_data.get('data')
#         file_name = all_data.get('name')
#         chats = all_data.get('chat')
#         file_path = '/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/{}.csv'.format(file_name)
#         csvfile = open(file_path, 'a')  # 处理后的数据写入csv文件 , encoding='utf-8'
#         csv_wri = csv.writer(csvfile)
#         for chat in chats:
#             jstr = json.dumps(chat, ensure_ascii=False)
#             print(jstr + "------end")
#             csvItem = [jstr]
#             csv_wri.writerow(csvItem)


# 获取聊天大类具体的聊天技巧数据
# def response(flow):
#     if flow.request.url.find("do=cate") != -1:
#         text = flow.response.get_text()
#         json_data = json.loads(text)
#         data = json_data.get('data')
#         parent_data = data.get('parent')
#         csvfile = open('/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/parent.csv', 'a')  # 处理后的数据写入csv文件 , encoding='utf-8'
#         csv_wri = csv.writer(csvfile)
#         for parent in parent_data:
#             categoryid = parent.get('categoryid')
#             name = parent.get('name')
#             csvItem = [categoryid, name]
#             csv_wri.writerow(csvItem)



# 获取聊天小类具体的聊天技巧数据
def response(flow):
    if flow.request.url.find("do=cate") != -1:
        text = flow.response.get_text()
        json_data = json.loads(text)
        data = json_data.get('data')
        parent_data = data.get('parent')
        child_data = data.get('child')
        csvfile = open('/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/child.csv', 'a')  # 处理后的数据写入csv文件 , encoding='utf-8'
        csv_wri = csv.writer(csvfile)
        # parent_list = []
        # for parent in parent_data:
        #     categoryid = parent.get('categoryid')
        #     parent_list.append(categoryid)
        # print(parent_list)

        for key, child_arr in child_data.items():
            print(key)
            for child in child_arr:
                categoryid = child.get('categoryid')
                name = child.get('name')
                super = child.get('super')
                csvItem = [categoryid, name, super]
                csv_wri.writerow(csvItem)
