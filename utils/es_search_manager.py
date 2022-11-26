from elasticsearch5 import Elasticsearch
from flask import jsonify

class SingleES(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.es = init_es()


def init_es():
    ES = [
        '127.0.0.1:9200'
    ]
    search = Elasticsearch(
        ES,
        # 启动前嗅探es集群服务器
        sniff_on_start=True,
        # es集群服务器结点连接异常时是否刷新es结点信息
        sniff_on_connection_fail=True,
        # 每60秒刷新结点信息
        sniffer_timeout=60
    )
    return search


def serch_chat_word(word):
    query = {
        "from": 0,
        "size": 5,
        "_source": ["id", "content"],
        "query": {
            "match": {
                "content": word
            }
        }
    }
    ret = SingleES().es.search(index='emotionwx', doc_type='_doc', body=query)
    return jsonify(ret)
