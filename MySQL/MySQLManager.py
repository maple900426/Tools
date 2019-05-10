#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import MySQLdb



class SQLManager():

    def __init__(self):
        pass

    def connect(self, IP, usr, pwd, schema):
        db = MySQLdb.connect( IP, usr, pwd, schema, charset='utf8' )
        cursor = db.cursor()
        return cursor

def main():
    classes = ['互联网','科技','产业新闻','企业','双创','手机','数码','行业']
    for c in classes:
        sql = SQLManager()
        cursor = sql.connect('10.0.4.20','hubo','1234567Myc','news')
        query = 'select id, title, content, class from NewsInfo where class = \'' + c + '\' order by date desc'
        # query = 'select count(*), class from NewsInfo where class = \'' + c + '\''
        cursor.execute(query)
        values = cursor.fetchall()

        with open('tech_news.txt','a') as f:
            for v in values:

                id = v[0]
                title = v[1]
                content = v[2]
                classes = v[3]
                content.replace('\\n','\\\\n')
                content.replace('\\t', '\\\\t')
                news = {"id":id,"title":title,"content":content,"class":classes}

                f.write(json.dumps(news,ensure_ascii=False))
                f.write('\n')


if __name__ == '__main__':
    main()
