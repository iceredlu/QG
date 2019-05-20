import pymysql
import pandas as pd
from sqlalchemy import create_engine


class connecSql():
    def __init__(self):
        self.connetSQL()

    #连接数据库
    def connetSQL(self):
        self.db = pymysql.connect(host='localhost', user='root', password='5824', port=3306, db='movie_qg')
        self.cursor = self.db.cursor()


    #保存用户信息到数据库
    def saveUserid(self):
        for i in range(200):
            sql = "INSERT INTO users(id,password) values(%s,%s)"
            try:
                self.cursor.execute(sql,(i+1,'5824'))
                self.db.commit()
            except:
                self.db.rollback()

    #保存用户电影评分矩阵到数据库
    def saveUserMoveMat(self):
        engine = create_engine('mysql+pymysql://root:5824@localhost:3306/movie_qg')
        try:
            filename = r'D:\QG\最终考核\movieRecSys\src\user_mov.csv'
            df = pd.read_csv(filename)
            df.to_sql('user_rating',con=engine,if_exists='replace',index=False)
        except Exception as e:
            print(e)

    #提取字段（从users表中提取当前用户对电影的评分
    def selectRating(self,userid):
        sql = "SELECT %s FROM user_rating" % userid
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(result)


if __name__ == '__main__':
    sql = connecSql()
    sql.selectRating('movId')