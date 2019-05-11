import pandas as pd
import csv

#获取200个用户信息 并处理后存储到新文件
def getUserRating():
    filename = 'ratings.csv'
    df = pd.read_csv(filename, usecols=(0, 1, 2), nrows=25127)
    dataSet = df.values
    ratings = [] #存放用户-电影-评分
    user_mov = {} #存放用户-电影矩阵
    for line in dataSet:
        user,movie,rating = line
        user_mov.setdefault(user,{})
        if movie >= 72 and movie <= 9985:
            user_mov[user][movie] = rating
            ratings.append([user,movie,rating])
    user_mov = pd.DataFrame(user_mov)
    user_mov = user_mov.fillna(0)
    user_mov.to_csv('user_mov.csv',index_label='movId')
    with open('testRatings.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['userid','movid','rating'])
        writer.writerows(ratings)

#getUserRating()


