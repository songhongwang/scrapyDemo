import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='douban', charset='utf8')

cursor = conn.cursor()

print(conn)
print(cursor)

sqlCreateTable = '''create table if not EXISTS movie (rank int(11) PRIMARY KEY, title VARCHAR(50), link VARCHAR(100), star VARCHAR(100), rate VARCHAR(100), quote VARCHAR(100))'''

sqlInsert = "insert into movie value('%d','%s','%s','%s','%s','%s')"

cursor.execute(sqlCreateTable)

for i in range(1,10):
    cursor.execute(sqlInsert%( int(i), 'title', 'link' + str(i), 'star' + str(i), 'rate' + str(i), 'quote' + str(i)))
conn.commit()


cursor.close()
conn.close()
