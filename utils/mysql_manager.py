import pymysql


# 创建数据库游标
def connect_database():
    conn = pymysql.connect(host="localhost", port=3306, user='root', password='1', database='emotionwx',charset='utf8')
    return conn


# 创建表
def create_table(sql):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.close()


# 创建用户表
def create_user_table():
    sql = """
    CREATE TABLE IF NOT EXISTS user_table  (
    user_id bigint(20) primary key auto_increment COMMENT '用户ID',
    username varchar(32)  NOT NULL COMMENT '用户名称',
    mobile char(11)  NOT NULL COMMENT '手机号',
    level tinyint(2) unsigned NOT NULL DEFAULT '0' COMMENT '0 零级 1 一级  2 二级',
    is_vip tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户基本信息表';
    """
    create_table(sql)


# 创建频道表
def create_channel_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  channel_table (
    channel_id bigint(20) unsigned NOT NULL COMMENT '频道ID',
    channel_name varchar(32)  NOT NULL COMMENT '频道名称',
    is_hot tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否是热门： 0 否 1 是',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='频道表';
    """
    create_table(sql)


# 创建用户频道表
def create_user_channel_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  user_channel_table (
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    user_id bigint(20) unsigned NOT NULL COMMENT '用户ID',
    channel_id bigint(20) unsigned NOT NULL COMMENT '频道ID',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户频道表';
    """
    create_table(sql)


# 创建话题表
def create_topic_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  topic_table (
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    title varchar(128)  NOT NULL COMMENT '标题',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题表';
    """
    create_table(sql)


# 创建话题详情列表
def create_topic_detail_list_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  topic_detail_list_table (
    item_id bigint(20) unsigned NOT NULL COMMENT '话题详情item ID',
    title varchar(128)  NOT NULL COMMENT '标题',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题详情列表';
    """
    create_table(sql)


# 创建话题与话题详情列表关系表
def create_topic_list_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  topic_list_table(
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    topic_id bigint(20) unsigned NOT NULL COMMENT '话题 ID',
    item_id bigint(20) unsigned NOT NULL COMMENT '话题详情item ID',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='话题与话题详情列表关系表';
    """
    create_table(sql)


# 创建话题详情内容表
def create_topic_detail_content_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  topic_detail_content_table(
    content_id bigint(20) unsigned NOT NULL COMMENT '内容ID',
    content varchar(1024)  NOT NULL COMMENT '内容',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='创建话题详情内容表';
    """
    create_table(sql)


# 创建话题内容关系表
def create_topic_list_detail_content_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  topic_list_detail_content_table(
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    item_id bigint(20) unsigned NOT NULL COMMENT '话题详情item ID',
    content_id bigint(20) unsigned NOT NULL COMMENT '话题详情内容 ID',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='创建话题内容关系表';
    """
    create_table(sql)


# 创建案例表
def create_case_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  case_table(
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    title varchar(128) NOT NULL COMMENT '标题',
    image varchar(128) NOT NULL COMMENT '图片URL',
    content varchar(1024) NOT NULL COMMENT '文章内容',
    content_id bigint(20) unsigned NOT NULL COMMENT '话题详情内容 ID',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='案例表';
    """
    create_table(sql)


# 创建课程表
def create_lesson_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  lesson_table(
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    title varchar(128) NOT NULL COMMENT '标题',
    wx varchar(32) NOT NULL COMMENT '微信号',
    lesson_count int(4) unsigned NOT NULL COMMENT ' 课程数量',
    look_count bigint(20) unsigned NOT NULL COMMENT ' 观看人数',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程表';
    """
    create_table(sql)


# 创建恋爱技巧表
def create_love_skill_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  love_skill_table(
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    title varchar(128) NOT NULL COMMENT '标题',
    images varchar(128) NOT NULL COMMENT '图片url json 字符串',
    date varchar(32) NOT NULL COMMENT '日期',
    look_count bigint(20) unsigned NOT NULL COMMENT ' 观看人数',
    content varchar(1024) NOT NULL COMMENT '内容',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='恋爱技巧表';
    """
    create_table(sql)


# 创建头部轮播表
def create_header_scroll_table():
    sql = """
    CREATE TABLE IF NOT EXISTS  header_scroll_table(
    id bigint(20) unsigned NOT NULL COMMENT 'ID',
    title varchar(128) NOT NULL COMMENT '标题',
    image varchar(128) NOT NULL COMMENT '图片url',
    is_delete tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 否 1 是'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='头部轮播表';
    """
    create_table(sql)

