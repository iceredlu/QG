import pandas as pd
import time
import numpy as np
from operator import itemgetter
import csv

class ItemBaseCf():
    #初始化参数
    def __init__(self):
        print('itembaseCF start..')
        #为目标用户找到50部相似电影，推荐20部相似电影
        self.n_sim_movie = 50
        self.n_rec_movie = 20

        #将数据集划分为训练集和测试集
        self.trainSet = {}
        self.testSet = {}

        #用户相似度矩阵
        self.movie_sim_matrix = {}
        self.movie_popular = {}#包含所有电影

        self.movie_count = 0

    #划分训练集和测试集，得到用户-电影矩阵
    def get_dataSet(self,filename,pivot=0.9):
        print('getting dataSet..')
        train_len = 0
        test_len = 0
        df = pd.read_csv(filename,usecols=(0,1,2)) #从文件中读取数据
        dataSet = df.values
        for line in dataSet:
            user,movie,rating = line
            if(np.random.random() < pivot): #随机划分训练集
                self.trainSet.setdefault(user,{})
                self.trainSet[user][movie] = rating
                train_len += 1
            else:
                self.testSet.setdefault(user,{})
                self.testSet[user][movie] = rating
                test_len += 1
        print('split trainingSet and testSet success.')
        print('TrainSet = %s' % train_len)
        print('TestSet = %s' % test_len)

    #计算电影之间相关系数，得到电影-电影相关度矩阵
    def cal_mov_sim(self):
        #统计电影用户数
        for user,movies in self.trainSet.items():#遍历用户
            for movie in movies:#遍历当前用户所看过的电影
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        self.movie_count = len(self.movie_popular)
        print("total movie number = %d" % self.movie_count)

        #统计电影同时出现的次数
        print('building co-rated user matrix...')
        start_time = time.time()
        step = 0
        for user,movies in self.trainSet.items():#遍历用户
            _time = time.time()
            step += 1
            if (step % 20000 == 0):
                print('step(%d),%f seconds have spent..' % (step, _time - start_time))
            for m1 in movies: #遍历电影
                for m2 in movies: #遍历当前电影相关电影
                    if m1 == m2:
                        continue
                    self.movie_sim_matrix.setdefault(m1,{})
                    self.movie_sim_matrix[m1].setdefault(m2,0)
                    self.movie_sim_matrix[m1][m2] += 1
        end_time = time.time()
        print('build co-rated user matrix success.')
        print(end_time-start_time,' seconds have spent.')

        #计算电影之间的相似性
        print('calculating movie similarity matrix...')
        for m1,related_movies in self.movie_sim_matrix.items():
            for m2,count in related_movies.items():
                if self.movie_popular[m1] == 0 or self.movie_popular[m2] ==0: #某电影用户数为0时两电影相似度为0
                    self.movie_sim_matrix[m1][m2] = 0
                else:
                    self.movie_sim_matrix[m1][m2] = count/np.sqrt(self.movie_popular[m1] * self.movie_popular[m2])
        print('calculate movie similarity matrix success.')

    #为目标用户找推荐n部相似电影
    def recommed(self,user):
        n = self.n_rec_movie
        k = self.n_sim_movie
        rank = {}
        wotched_movies = self.trainSet[user]
        for movie,rating in wotched_movies.items():
            for related_movie,w in sorted(self.movie_sim_matrix[movie].items(),key=itemgetter(1),reverse=True)[:k]:
                if related_movie in wotched_movies:
                    continue
                rank.setdefault(related_movie,0)
                rank[related_movie] += w * float(rating)
        return sorted(rank.items(),key=itemgetter(1),reverse=True)[:n]

    #产生推荐并通过准确率，召回率和覆盖率进行评估
    def evaluate(self):
        print('evaluating...')
        n = self.n_rec_movie
        #准确率和召回率
        hit = 0
        rec_count = 0
        test_count = 0
        #覆盖率
        all_rec_movies = set()
        for i,user in enumerate(self.trainSet):#遍历训练集中的用户
            test_movies = self.testSet.get(user,{}) #取出当前用户在测试集中所看过的电影
            rec_movies = self.recommed(user) #根据当前用户在训练集中的数据得到推荐电影
            for movie,w in rec_movies:#遍历所推荐的电影
                if movie in test_movies: #测试集中存在
                    hit += 1
                all_rec_movies.add(movie)
            rec_count += n#推荐电影数量
            test_count += len(test_movies)#训练集中用户看过的电影数量

        precision = hit / (1.0 * rec_count) #准确率
        recall = hit / (1.0 * test_count)#召回率
        coverage = len(all_rec_movies) / (1.0 * self.movie_count) #覆盖率
        print('precision=%.4f\trecall=%.4f\tcoverage=%.4f' % (precision,recall,coverage))

    def savt_sim_movie(self):
        with open('sim_movie.csv','w') as csvfile:
            csvwriter = csv.writer(csvfile)
            for k,v in itemCF.movie_sim_matrix.items():
                csvwriter.writerow([k,v])
            csvfile.close()

if __name__ == '__main__':
    itemCF = ItemBaseCf()
    filename = 'ratings.csv'
    itemCF.get_dataSet(filename)
    itemCF.cal_mov_sim()
    #itemCF.savt_sim_movie()
    itemCF.evaluate()
