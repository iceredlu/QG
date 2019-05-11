import sys
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class ConnetSQL(QWidget):
    def __init__(self):
        super(ConnetSQL,self).__init__()
        self.db = None
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


"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sql = ConnetSQL()
    sql.show()
    sys.exit(app.exec_())
"""