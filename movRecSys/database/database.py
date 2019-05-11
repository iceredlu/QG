import pymysql
import pandas as pd

db = pymysql.connect(host='localhost',user='root',password='5824',port=3306,db='spiders')
cursor = db.cursor()

"""
#创建表
sql = 'CREATE TABLE IF NOT EXISTS movie(directors VARCHAR(255) NOT NULL,id VARCHAR(255) NOT NULL,casts VARCHAR(255) NOT NULL,' \
      'rate VARCHAR(255) NOT NULL,title VARCHAR(255) NOT NULL,star VARCHAR(255) NOT NULL,url VARCHAR(255) NOT NULL,' \
      'cover VARCHAR(255) NOT NULL,tag VARCHAR(255) NOT NULL,PRIMARY KEY(id))'
cursor.execute(sql)
"""

df = pd.read_csv('movie_data.csv')
df=df.values
for i in range(1,len(df)):
    value = df[i]
    sql = 'INSERT INTO movie(casts,cover,directors,id,rate,star,title,url,tag) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]))
        db.commit()
    except:
        db.rollback()

db.close()