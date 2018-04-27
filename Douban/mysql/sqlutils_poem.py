import MySQLdb
from Douban.items import Poem

class SqlUtilsPoem:
 
    host='qdm21456398.my3w.com'
    port=3306
    user='qdm21456398'
    passwd='xiaoyu123'
    db='qdm21456398_db'
    charset='utf8'


    # host='127.0.0.1'
    # port=3306
    # user='root'
    # passwd='123456'
    # db='douban'
    # charset='utf8'

    createTableStr = '''create table if not EXISTS poem (id int(11) PRIMARY KEY AUTO_INCREMENT, type VARCHAR(50) CHARACTER SET 'utf8', name VARCHAR(50) CHARACTER SET 'utf8', dynasty VARCHAR(1000) CHARACTER SET 'utf8', author VARCHAR(50) CHARACTER SET 'utf8', content VARCHAR(300) CHARACTER SET 'utf8', translation VARCHAR(300) CHARACTER SET 'utf8')'''
    insertStr = "insert into poem (type, name, dynasty, author, content, translation) value('%s','%s','%s','%s','%s','%s')"


    conn = None
    cursor = None

    def __init__(self):
        self.conn = MySQLdb.connect(host = self.host, port = self.port, user = self.user, passwd = self.passwd, db = self.db, charset = self.charset)
        self.cursor = self.conn.cursor()

        self.cursor.execute(self.createTableStr)
        self.conn.commit()

    def closeConnect(self):
        self.cursor.close()
        self.conn.close()

# crud

    def insert(self, poem):  
         
        sql = self.insertStr%(poem['type'], poem['name'], poem['dynasty'], poem['author'], poem['content'], poem['translation'])
        self.cursor.execute(sql)
        self.conn.commit()
        
        print('insert success :'+poem['name'])
        self.closeConnect()













