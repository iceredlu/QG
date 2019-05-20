from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys

class ConnetSQL(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connect()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('movie_qg')
        self.db.setUserName('root')
        self.db.setPassword('5824')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()

    #匹配类型
    def genresSearch(self,genre):
        query = QSqlQuery()
        query.exec_("SELECT ID,type1,type2,type3 FROM movie_qg")
        matchID = []
        while query.next():
            if genre == query.value(1) or genre == query.value(2) or genre == query.value(3):
                matchID.append(query.value(0))
        return matchID

    #匹配地区
    def regionSearch(self,region):
        query = QSqlQuery()
        query.exec_("SELECT ID,place FROM movie_qg")
        matchID = []
        while query.next():
            if region == query.value(1):
                matchID.append(query.value(0))
        return matchID

    #由电影ID获取详细信息
    def movID_get_details(self,movID):
        query = QSqlQuery()
        query.exec_("SELECT ID,moviename,englishname,dataID,director,star,type1,type2,type3,place,"
                    "score,years,introduction,timelong,link FROM movie_qg")
        field = ['ID','moviename','englishname','dataID','director','star','type1','type2','type3','place','score','years','introduction','timelong','link']
        movDetails = {}
        while query.next():
            if movID == query.value(0):
                for i in range(len(field)):
                    movDetails[field[i]] = query.value(i)
                return movDetails

    #由电影名称返回包含指定搜索名称的电影ID
    def movName_get_movID(self,name):
        query = QSqlQuery()
        query.exec_()
        query.exec_("SELECT ID,moviename FROM movie_qg")
        movID = []
        while query.next():
            if name in query.value(1):
                movID.append(query.value(0))
        return movID

    #根据电影id获取评分
    def getScore(self,id):
        query = QSqlQuery()
        query.exec_()
        query.exec_("SELECT ID,score FROM movie_qg")
        while query.next():
            ID = query.value(0)
            if id == ID:
                return query.value(1)

    #登录时检查是否用户名密码匹配,匹配返回真值，否则False
    def match_userID(self,id,pwd):
        query = QSqlQuery()
        query.exec_()
        query.exec_("SELECT id,password FROM users")
        while query.next():
            if id == query.value(0) and pwd == query.value(1):
                return True
        return False

    #注册时检查用户名是否存在
    def isExistUserID(self,id):
        query = QSqlQuery()
        query.exec_()
        query.exec_("SELECT id FROM users")
        while query.next():
            if id == query.value(0):
                return True
        return False

    #注册新用户
    def signIn(self,id,pwd,type):
        query = QSqlQuery()
        query.exec_()
        sql = "INSERT INTO users (id,password,type) VALUES (%s,%s,'%s')" % (id,pwd,type)
        query.exec_(sql)
        return True

    #修改用户评分
    def mark(self,userid,movid,mark):
        pass

    #修改密码
    def changePwd(self,id,pwd):
        query = QSqlQuery()
        query.exec_()
        sql = "UPDATE users SET password = '%s' WHERE id = '%s'" % (pwd,id)
        query.exec_(sql)

    #获取新用户所喜欢的类型
    def getNewType(self,id):
        id = str(id)
        query = QSqlQuery()
        query.exec_()
        sql = "SELECT id,type FROM users"
        query.exec_(sql)
        while query.next():
            if query.value(0) == id:
                return query.value(1)

    def col(self):
        query = QSqlQuery()
        query.exec_()

    #获取电影评论
    def getComment(self,id):
        queue = QSqlQuery()
        queue.exec_()
        sql = "SELECT id,comment1,comment2,comment3,comment4,comment5,comment10,comment6,comment7,comment8,comment9 FROM comments"
        queue.exec_(sql)
        comments = []
        while queue.next():
            if queue.value(0) == id:
                for i in range(10):
                    comments.append(queue.value(i+1))
                return comments
        return comments


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sql = ConnetSQL()
    sql.getComment(3961)
    sys.exit(app.exec_())


