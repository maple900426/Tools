#-*-coding:utf-8-*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from elasticsearch import Elasticsearch

es=Elasticsearch('10.0.4.23:8405')
index = 'tmall_shop'
dtype = 'external'

if __name__ == '__main__':
    settings = {"settings":{"number_of_shards":2,"number_of_replicas":1,"max_result_window":200000000}}
    mappings = {}
    with open('es_mapping_template','r') as f:
       mappings = f.read()
    if not es.indices.exists(index=index):
        es.indices.create(index=index,body=settings)
    if not es.indices.exists_type(index=index,doc_type=dtype):
        es.indices.put_mapping(index=index,doc_type=dtype,body=mappings)
