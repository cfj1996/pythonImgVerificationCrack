import pymysql
from datetime import datetime
connection = pymysql.connect(host='localhost',port=3307,user='root',password='root',db='cnblogs',charset='utf8')
def create(data):
    cursor = connection.cursor()
    effect_row = cursor.executemany('INSERT INTO `url` (`url`, `creator_time`) VALUES (%s, %s)',
    data)
    connection.commit()