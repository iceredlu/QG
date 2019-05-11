import pandas as pd


class recMov():
    def __init__(self):
        self.watchedMov = {}
        self.simMov = {}

    #获取用户以看过的电影
    def getUserMov(self):
        ratFile = r'D:\QG\最终考核\movieRecSys\src\user_mov.csv'
        df = pd.read_csv(ratFile,usecols=(0,self.userid)).values
        for line in df:
            mov,rat = line
            if rat == 0:
                continue
            self.watchedMov[mov] = rat

    #获取电影-电影相似度矩阵
    def getMovSim(self):
        

    #推荐电影列表
    def recmov(self,userid):
        self.userid = userid
        self.getUserMov() #获取已看电影



#获取电影相似度矩阵
def getMovSim():
    movsim = r'D:\QG\最终考核\movieRecSys\algorithm\sim_movid.csv'
    m=112
    m = str(m) + '.0'
    df = pd.read_csv(movsim,usecols=('movid',m)).values

    print(df)

print(getUserMov(9))