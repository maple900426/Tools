#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from ESManager.FileManager import FileManager

def main():
    fm = FileManager()
    f = 'test.txt'
    datas = ['1','2']
    fm.write_file(f, datas, True)

main()