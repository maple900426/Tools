#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from elasticsearch import Elasticsearch, helpers

class ESManager():

    def __init__(self):
        self.headers = "Content-Type: application/json"

    def load_es(self, IP, index, doc_type):

        client = Elasticsearch(IP)
        es_result = helpers.scan(
            client = client,
            index = index,
            doc_type = doc_type,
            scroll = '10m',
        )

        datas = []
        for es_item in es_result:
            source = es_item['_source']
            datas.append(source)
        return datas

    def insert(self, IP, index, doc_type, datas = []):
        es = Elasticsearch(IP)
        for data in datas:
            jdata = data
            id = jdata['details']['shop_id']
            es.index(index=index, doc_type=doc_type, id=id, body=jdata)
        es.indices.refresh(index)

    def update(self, IP, index, doc_type, body):
        id = body['details']['id']
        es = Elasticsearch(IP)
        es.update(index=index, doc_type=doc_type, id=id, body=body)

    def delete_by_id(self, IP, index, doc_type, id):
        es = Elasticsearch(IP)
        es.delete(index=index, doc_type=doc_type, id=id)
        es.indices.refresh(index)

    def search_by_query(self, IP, index, doc_type, body ):
        es = Elasticsearch(IP)
        return es.search(index, doc_type, body)

    def bulk_insert(self):
        pass


def main():
    es = ESManager()

    '''
    1.
    从 ES 检索数据
    input: IP, index, doc_type
    
    example:
    datas = es.load_es('10.0.4.23:8405','basketball','teams')
    datas 为 json格式数组
    '''


    '''
    批量灌库
    # es = Elasticsearch('10.0.4.112:8405')
    # actions = [
    #     {
    #         '_op_type': 'index',
    #         '_index': 'cars_4_2',
    #         '_type': 'cars_info',
    #         '_source': d,
    #     }
    #     for d in datas
    # ]
    # helpers.bulk(es, actions)
    # es.write_file('team_data.dat', datas)
    '''


    '''
    2.
    ES 灌库
    input: IP, index, doc_type, datas
    
    example:
    es.insert('10.0.2.100:8401','basketball','teams', datas)
    datas = []， 每条数据必须为json格式，可用JSONManager将string先转换为json
    JSONManager.to_json(data)
    '''

    '''
    3.
    es检索
    basic search by query:
    input: IP, index, doc_type, body
    
    body = '{"query":{"bool":{"must":{"term":{"normalized.alias":"猛龙"}}}},"size":10}'
    335
    example:
    res = es.search_by_query('10.0.2.100:8401','basketball','teams', body)
    print js.parser(res)
    '''

    '''
    4.
    修改 ES 数据
    es.update('10.0.2.100:8401','basketball','teams',body)
    
    '''


if __name__ == '__main__':
    main()