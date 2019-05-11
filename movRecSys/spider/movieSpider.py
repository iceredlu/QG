import requests
import json
import pandas as pd
import numpy as np
import time
import os

#按分类爬取
genres = ['剧情', '喜剧', '动作', '爱情', '科幻', '动画', '悬疑', '惊悚', '恐怖', '犯罪', '同性', '音乐', '歌舞', '传记', '历史',
              '战争', '西部', '奇幻', '冒险', '灾难', '武侠', '情色']

#构造网页
def get_url(page_start,genresIndex):
    gen = genres[genresIndex]
    url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&genres={}'.format(page_start,gen)
    return url

#获取数据
def get_data():
    for genIndex in range(len(genres)):
        for page_start in range(0,240,20):#获取当前分类前240部影片信息
            try:
                url = get_url(page_start,genIndex)
                res = requests.get(url)
                data = res.text
                dicts = json.loads(data)
                df = pd.DataFrame(dicts['data'])#转为dataframe格式
                df.drop('cover_x',axis=1,inplace=True) #删除不需要的列
                df.drop('cover_y',axis=1,inplace=True)
                df['tag'] = np.tile(genres[genIndex],(df.shape[0],1))  #加入列存放分类值
                if (genIndex==0)&(page_start==0):
                    df.to_csv('movie_data.csv', sep=',', header=True, index=False) #genindex=0&page_stare=0时第一次存储，保留标签名
                else:
                    df.to_csv('movie_data.csv', sep=',', header=False, index=False, mode='a') #不保留标签名
            except requests.exceptions.ProxyError as e:
                print("Crawl failure：",e,'\n',url,'\n')
                page_start -= 20
            else:
                print(res.reason, '\n', url, '\n')
                page_start -= 20
            time.sleep(np.random.random()*5)

#存储电影海报
def get_poster():
    img = pd.read_csv('movie_data.csv',usecols=(1,3)).values
    path = os.getcwd() #当前路径
    for i in range(len(img)):
        picpath = path + '/' + 'poster'
        if not os.path.isdir(picpath): #创建目录
            os.mkdir(picpath)
        dir = picpath + '/' + str(img[i,1]) + '.jpg' #海报存储目录
        try:
            pic = requests.get(img[i,0])
        except requests.exceptions.ConnectionError:
            print("Faile:",img[i,0])
        with open(dir,'wb') as f:
            f.write(pic.content)
            f.close()

if __name__ == '__main__':
    get_data()
    get_poster()