#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from File.FileManager import FileManager
from ES.ESManager import ESManager

def file_manager():
    fm = FileManager()
    f = 'test.txt'
    datas = ['1','2']
    fm.write_file(f, datas, True)

def es_manager():
    es = ESManager()

es_manager()
