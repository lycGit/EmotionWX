import pymysql
import csv
import os


class SingleDB(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Lyc198901', db='emotionwx',charset='utf8')

# 创建数据库游标
def connect_database():
    conn = pymysql.connect(host="localhost", port=3306, user='root', password='1', database='emotionwx',charset='utf8')
    return conn


# 执行数据库语句
def excute_sql(sql):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


# 创建聊天大类表
def create_chat_skill_table():
    sql = """
    CREATE TABLE IF NOT EXISTS chat_skill_table  (
    id bigint(20) primary key auto_increment COMMENT '话题大类ID',
    name varchar(32)  NOT NULL COMMENT '话题大类',
    categoryid char(5)  NOT NULL COMMENT '大类类别ID',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题大类表';
    """
    excute_sql(sql)


def init_chat_skill_table():
    create_chat_skill_table()
    csv_reader = csv.reader(open("/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/parent.csv"))
    for row in csv_reader:
        categoryid = row[0]
        name = row[1]
        sql = """insert into chat_skill_table(categoryid,name) VALUES('{}', '{}');""".format(categoryid, name)
        excute_sql(sql)


def get_chat_skill():
    sql = 'select * from chat_skill_table'
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res
    # for item in res:
    #     print(item[1]+item[2])



# 创建聊天小类表
def create_chat_child_table():
    sql = """
    CREATE TABLE IF NOT EXISTS chat_child_table  (
    id bigint(20) primary key auto_increment COMMENT '话题小类ID',
    name varchar(32)  NOT NULL COMMENT '话题小类',
    categoryid char(5)  NOT NULL COMMENT '小类类别ID',
    superCategoryID char(5)  NOT NULL COMMENT '小类父类类别ID',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题小类表';
    """
    excute_sql(sql)


def init_chat_child_table():
    create_chat_child_table()
    csv_reader = csv.reader(open("/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/child.csv"))
    for row in csv_reader:
        categoryid = row[0]
        name = row[1]
        superCategoryID = row[2]
        sql = """insert into chat_child_table(categoryid,name,superCategoryID) VALUES('{}', '{}', '{}');""".format(categoryid, name, superCategoryID)
        excute_sql(sql)


def get_chat_child_skill(superCategoryID):
    sql = """select * from chat_child_table where superCategoryID = '{}';""".format(superCategoryID)
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    # for item in res:
    #     print(item[1]+item[2])
    return res


# 通过话题标题进行查询
def get_chat_child_by_name(name):
    sql = """select * from chat_child_table where name = '{}';""".format(name)
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    # for item in res:
    #     print(item[1]+item[2])
    return res


def create_chat_detail_table():
    sql = """
    CREATE TABLE IF NOT EXISTS chat_detail_table  (
    id bigint(20) primary key auto_increment COMMENT '话题详情ID',
    superID bigint(20) NOT NULL COMMENT '话题详情父ID',
    content varchar(1024)  NOT NULL COMMENT '话题详情内容',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题详情表';
    """
    excute_sql(sql)


def init_chat_detail_table():
    create_chat_detail_table()
    res = get_chat_skill()
    for item in res:
        big_categroy = item[1]
        path1 = '/Users/liuyangcheng/Desktop/LearnClass/EmotionWX/spider/mitmdump_crawl/聊天话术/{}'.format(big_categroy)
        list = os.listdir(path1)
        for name in list:
            namestr = name.replace('.csv', '')
            res = get_chat_child_by_name(namestr)
            line = res[0]
            print(line)
            chat_child_id = line[0]
            path2 = path1 + '/' + name
            csv_reader = csv.reader(open(path2))
            print(path2)
            for row in csv_reader:
                content = row[0]
                sql = """insert into chat_detail_table(superID,content) VALUES('{}', '{}');""".format(chat_child_id, content)
                excute_sql(sql)


def get_chat_detail_by_superID(superID, page, pageSize):
    index = (page - 1) * pageSize
    sql = """select * from chat_detail_table where superID = '{}' order by id desc limit {},{};""".format(superID, index, pageSize)
    print(sql)
    conn = SingleDB().conn
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    # for item in res:
    #     print(item[2] + '{}'.format(item[1]))
    return res
