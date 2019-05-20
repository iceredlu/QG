import pandas as pd
from operator import itemgetter

class recMov():
    def __init__(self):
        self.watchedMov = {}
        self.simMov = {}

    #获取用户以看过的电影
    def getUserMov(self):
        ratFile = r'D:\QG\最终考核\movieRecSys\src\user_mov.csv'
        self.userid = int(self.userid)
        self.userid = float(self.userid)
        self.userid = str(self.userid)
        df = pd.read_csv(ratFile,usecols=('movId',self.userid)).values
        for line in df:
            mov,rat = line
            if rat == 0:
                continue
            self.watchedMov[mov] = rat

    #获取电影相似度矩阵
    def getMovSim(self):
        self.curSim = {}  # 存放相似电影
        simFile = r'D:\QG\最终考核\movieRecSys\algorithm\sim_movid.csv'
        df = pd.read_csv(simFile)
        self.simMov = df.set_index('movid').to_dict()

    #推荐电影列表
    def recmov(self,userid):
        self.userid = userid
        self.getUserMov() #获取已看电影
        self.getMovSim() # 获取电影电影相似度矩阵
        rank = {} #初始推荐列表
        for mov,rat in self.watchedMov.items():
            mov = str(mov)
            self.simMov.setdefault(mov,{})
            for related,w in sorted(self.simMov[mov].items(),key=itemgetter(1),reverse=True)[:50]:
                if related in self.watchedMov:
                    continue
                rank.setdefault(related,0)
                rank[related] += w * float(rat)
        recmov = sorted(rank.items(),key=itemgetter(1),reverse=True)[:21]
        print(recmov)
        return recmov
