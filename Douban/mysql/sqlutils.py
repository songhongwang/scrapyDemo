import MySQLdb


class SqlUtils:

    host='127.0.0.1'
    port=3306
    user='root'
    passwd='123456'
    db='douban'
    charset='utf8'

    createTableStr = '''create table if not EXISTS movie (id int(11) PRIMARY KEY AUTO_INCREMENT, rank VARCHAR(100) CHARACTER SET 'utf8', title VARCHAR(200) CHARACTER SET 'utf8', link VARCHAR(200) CHARACTER SET 'utf8', star VARCHAR(200) CHARACTER SET 'utf8', rate VARCHAR(200) CHARACTER SET 'utf8', quote VARCHAR(200) CHARACTER SET 'utf8')'''
    insertStr = "insert into movie (rank, title, link, star, rate, quote) value('%s','%s','%s','%s','%s','%s')"


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

    def insert(self, movie_list):
 
        for movie in movie_list:
            self.cursor.execute(self.insertStr%(movie['rank'], movie['title'], movie['link'], movie['star'], movie['rate'], movie['quote']))
 
        
        self.conn.commit()

        self.closeConnect()













