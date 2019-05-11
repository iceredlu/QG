import pymysql
import pandas as pd
from sqlalchemy import create_engine

class loadData():
    def __init__(self):
        self.initDB()

    def initDB(self):
        self.db = pymysql.connect(host='localhost',user='root',password='5824',port=3306,db='movie_qg')
        self.cursor = self.db.cursor()

    def load_rating(self):
        df = pd.read_csv('ratings.csv',usecols=(0,1,2))
        df = df.values
        for i in range(10):
            value = df[i]
            sql = "INSERT INTO ratings(index,userid,movid,rating) values(%d,%f,%f,%f)"
            try:
                self.cursor.execute(sql,(i,value[0],value[1],value[2]))
                self.db.commit()
            except:
                self.db.rollback()



if __name__ == '__main__':
    load = loadData()
    load.load_rating()