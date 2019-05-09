#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json

class FileManager():

    def __init__(self):
        pass

    def load_file(self, file_name, js = False):
        datas = []
        with open(file_name, 'r') as f:
            for line in f:
                if not line:
                    break
                line = line.strip()
                if len(line) == 0:
                    continue
                if js:
                    try:
                        line = json.loads(line)
                    except Exception as e:
                        print 'load file to json failed with error: ', e
                datas.append(line)
        return datas


    def write_file(self, file_name, datas, js = False):
        with open(file_name, 'w') as f:
            for data in datas:
                line = data
                if js:
                    line = json.dumps(data, ensure_ascii=False)
                f.write(line + '\n')

