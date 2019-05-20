import pymysql
import requests
from lxml import etree
import time
import random

class spiderCom():
    def __init__(self):
        self.connectMySql()
        self.url = {} #电影id为键url为值
        self.shortComment = {} # 电影id为键，值为短评列表

    # 连接数据库
    def connectMySql(self):
        self.db = pymysql.connect(host='localhost', user='root', password='5824', port=3306, db='movie_qg')
        self.cursor = self.db.cursor()

    #从数据库中提取信息
    def getData(self):
        print('getting the link from the database...')
        sql = "SELECT ID,link FROM movie_qg"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            if row[0] > 5002:
                self.url[row[0]] = row[1]

    #由电影详情url构造电影短评地址
    def getURL(self,url):
        url = url + '/comments?start=0&limit=20&sort=new_score&status=P'
        return url

    #抓取电影短评
    def getShortComment(self):
        self.getData()
        print('spidering..')
        start = time.perf_counter()
        keys = list(self.url.keys()) #获取列表形式的电影id作为索引值
        count = 0
        for i in range(len(keys)):
            count += 1
            commentURL = self.getURL(self.url[keys[i]])
            res = requests.get(commentURL)
            html = etree.HTML(res.text)
            comment = [] #存放评论
            for j in range(10):
                curCom = html.xpath('//*[@id="comments"]/div[%d]/div[2]/p/span/text()' % (j+1))
                if curCom == '':
                    curCom = '/'
                comment.append(curCom)
            self.shortComment[keys[i]] = comment
            time.sleep(random.random() * 10)
            #每爬取10个存入数据库
            if count % 10 == 0:
                self.saveToSql()
                cur = time.perf_counter()
                print("spider %d :spend %f seconds" % (count,cur-start))
                self.shortComment = {}

    #创建表
    def creatTabel(self):
        sql = "CREATE TABLE IF NOT EXISTS comments (id INT(6) NOT NULL,1 VARCHAR(255) NOT NULL,comment2 VARCHAR(255) NOT NULL," \
              "comment3 VARCHAR(255) NOT NULL,comment4 VARCHAR(255) NOT NULL,comment5 VARCHAR(255) NOT NULL,comment6 VARCHAR(255) NOT NULL," \
              "comment7 VARCHAR(255) NOT NULL,comment8 VARCHAR(255) NOT NULL,comment9 VARCHAR(255) NOT NULL,comment10 VARCHAR(255) NOT NULL,PRIMARY KEY (id))"
        self.cursor.execute(sql)

    #保存到数据库
    def saveToSql(self):
        keys = list(self.shortComment.keys())
        values = list(self.shortComment.values())
        for i in range(len(self.shortComment)):
            id = keys[i]
            commands = values[i]
            try:
                sql = "INSERT INTO comments(id,comment1,comment2,comment3,comment4,comment5,comment6,comment7,comment8,comment9,comment10) VALUES(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " % (id,commands[0][0],commands[1][0],commands[2][0],commands[3][0],commands[4][0],commands[5][0],commands[6][0],commands[7][0],commands[8][0],commands[9][0])
                self.cursor.execute(sql)
                self.db.commit()
            except:
                print('error:',keys[i])
                self.db.rollback()

spider = spiderCom()
spider.getShortComment()

'''
url = "https://movie.douban.com/subject/1295686//comments?start=0&limit=20&sort=new_score&status=P"
res = requests.get(url)
html = etree.HTML(res.text)
command = html.xpath('//*[@id="comments"]/div[1]/div[2]/p/span/text()')
print(command)


'''
"""
id,'%s' % commands[0][0],commands[1][0],commands[2][0],commands[3][0],commands[4][0],commands[5][0],commands[6][0],commands[7][0],commands[8][0],commands[9][0]
"""

"""
import requests
from lxml import etree

#构造url
url = "https://movie.douban.com/subject/1295686" + "/comments?start=0&limit=20&sort=new_score&status=P"
res = requests.get(url)
html = etree.HTML(res.text)
for i in range(10):
    command = html.xpath('//*[@id="comments"]/div[%d]/div[2]/p/span/text()' % (i+1))
    print(command)

"""