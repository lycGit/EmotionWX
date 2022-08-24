import requests
import time
import re
import os
from os import path


# 读取gif
def read_crawl_gifs():
    patter = r'http.*gif'
    return read_crawl_content(patter)


# 读取png
def read_crawl_pngs():
    patter = r'http.*png'
    return read_crawl_content(patter)


# 读取jpg
def read_crawl_jpgs():
    patter = r'http.*jpg'
    return read_crawl_content(patter)


# 读取jpeg
def read_crawl_jpegs():
    patter = r'http.*jpeg'
    return read_crawl_content(patter)


# 读取mp3
def read_crawl_mp3s():
    patter = r'http.*mp3'
    return read_crawl_content(patter)


def read_crawl_content(patter):
    f = open("../spider/crawl_content/tu.txt", encoding="utf-8")
    content_str = f.read()
    arr = re.findall(patter, content_str)
    f.close()
    return arr


# 下载gif 图片
def crawl_gif_image(image_url):
    crawl_image_path(image_url, '../spider/crawl_gif_images')


# 下载png 图片
def crawl_png_image(image_url):
    crawl_image_path(image_url, '../spider/crawl_png_images')


# 下载jpg 图片
def crawl_jpg_image(image_url):
    crawl_image_path(image_url, '../spider/crawl_jpg_images')


# 下载mp3
def crawl_mp3s(mp3_url):
    crawl_image_path(mp3_url, '../spider/crawl_mp3s')


# 指定图片URL 和 路径
def crawl_image_path(image_url, path):
    image_url = image_url.replace('\\', '')
    response = requests.get(image_url)
    image_name_int = time.time() * 1000000
    image_name = '{}'.format(image_name_int)
    print(image_name)
    with open(path + '/{}'.format(image_name), 'wb') as f:  # 创建用来保存图片的.png文件
        f.write(response.content)  # 注意，'wb'中的b 必不可少！！


# 遍历所有的文件
def scan_all_files(url):
    print(url)
    file = os.listdir(url)
    for f in file:
        # 字符串拼接
        old_url = path.join(url, f)
        if old_url.find('.0') != -1:
            new_url = old_url
            new_url = new_url.replace('.0', '')
            new_url = new_url + '.gif'
            os.rename(old_url, new_url)
            # 打印出来
            print(new_url)


