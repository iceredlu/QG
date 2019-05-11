import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sql import ConnetSQL
from detailsPage import movDetails
from logInPage import logIn
from algorithm.algorithm import ItemBaseCf

class mainUI(QTabWidget):
    def __init__(self):
        super().__init__()
        QApplication.setStyle('Fusion') #窗口风格
        self.sql = ConnetSQL()
        self.detail = movDetails()
        self.log = logIn()
        self.cf = ItemBaseCf()

        self.initUI()

    #初始化
    def initUI(self):
        self.tab_class = QWidget()
        self.tab_homepage = QWidget()

        self.addTab(self.tab_class,'分类搜索')#添加窗口
        self.addTab(self.tab_homepage,'个人主页')

        self.tab_classUI()#初始化
        self.tab_homepageUI()

        self.setWindowTitle('电影推荐系统')
        self.resize(1200, 750)

        palette = QPalette()  # 设置背景色
        palette.setColor(palette.Background, QColor(0, 77, 64))
        self.setPalette(palette)

    #分类界面
    def tab_classUI(self):
        self.initClass()
        self.last_page.setEnabled(False)

    #初始化分类界面
    def initClass(self):
        self.classCon()
        self.classLayout()
        self.classConsum()

    #添加分类界面控件
    def classCon(self):
        self.class_search = QLineEdit()
        self.class_search_bt = QPushButton('搜索')
        self.class_search.setPlaceholderText('输入电影名称')

        genres = ['剧情', '喜剧', '动作', '爱情', '科幻', '动画', '悬疑', '惊悚', '恐怖', '音乐', '传记','奇幻', '冒险', '武侠']
        #实例化QComBox对象
        self.genres_label = QLabel('类型:')
        self.cb_gen = QComboBox()
        for i in range(len(genres)):#添加选项
            self.cb_gen.addItem(genres[i])

        regions = ['中国大陆','香港','美国','英国','法国','日本','韩国']
        self.region_label = QLabel('地区:')
        self.cb_region = QComboBox()
        for i in range(len(regions)):
            self.cb_region.addItem(regions[i])

        age = ['2019年','2010年代','00年代','90年代','80年代','70年代','更早']
        self.age_label = QLabel('年代:')
        self.cb_age = QComboBox()
        for i in range(len(age)):
            self.cb_age.addItem(age[i])

        #图片标签
        self.movPosterLabel_1 = QLabel()
        self.movPosterLabel_2 = QLabel()
        self.movPosterLabel_3 = QLabel()
        self.movPosterLabel_4 = QLabel()
        self.movPosterLabel_5 = QLabel()
        self.movPosterLabel_6 = QLabel()

        #自适应大小
        self.movPosterLabel_1.setScaledContents(True)
        self.movPosterLabel_2.setScaledContents(True)
        self.movPosterLabel_3.setScaledContents(True)
        self.movPosterLabel_4.setScaledContents(True)
        self.movPosterLabel_5.setScaledContents(True)
        self.movPosterLabel_6.setScaledContents(True)

        #电影名标签
        self.movTitleLabel_1 = QLabel()
        self.movTitleLabel_2 = QLabel()
        self.movTitleLabel_3 = QLabel()
        self.movTitleLabel_4 = QLabel()
        self.movTitleLabel_5 = QLabel()
        self.movTitleLabel_6 = QLabel()

        #导演
        self.movDirectorLabel_1 = QLabel()
        self.movDirectorLabel_2 = QLabel()
        self.movDirectorLabel_3 = QLabel()
        self.movDirectorLabel_4 = QLabel()
        self.movDirectorLabel_5 = QLabel()
        self.movDirectorLabel_6 = QLabel()

        #电影评分
        self.movScoreLabel_1 = QLabel()
        self.movScoreLabel_2 = QLabel()
        self.movScoreLabel_3 = QLabel()
        self.movScoreLabel_4 = QLabel()
        self.movScoreLabel_5 = QLabel()
        self.movScoreLabel_6 = QLabel()

        #添加按钮显示电影详细信息
        self.detBt_1 = QPushButton('详细信息')
        self.detBt_2 = QPushButton('详细信息')
        self.detBt_3 = QPushButton('详细信息')
        self.detBt_4 = QPushButton('详细信息')
        self.detBt_5 = QPushButton('详细信息')
        self.detBt_6 = QPushButton('详细信息')

        #改变页数
        self.last_page = QPushButton('上一页')
        self.next_page = QPushButton('下一页')

        self.transVar()#初始页面

    #改变类型把信息传到标签中的变量
    def transVar(self):
        self.setMovLabelVar()#重新获取电影信息
        self.resetLabel()

    #获取电影信息，设置标签的值
    def setMovLabelVar(self):
        self.match_mov()#获取匹配的电影id，再根据电影id获取详细信息放在列表
        self.curMov = 0
        self.evalue() #设置标签变量列表

    #重置标签内容
    def resetLabel(self):
        #海报
        self.movPosterLabel_1.setPixmap(QPixmap(self.movPoster[0]))
        self.movPosterLabel_2.setPixmap(QPixmap(self.movPoster[1]))
        self.movPosterLabel_3.setPixmap(QPixmap(self.movPoster[2]))
        self.movPosterLabel_4.setPixmap(QPixmap(self.movPoster[3]))
        self.movPosterLabel_5.setPixmap(QPixmap(self.movPoster[4]))
        self.movPosterLabel_6.setPixmap(QPixmap(self.movPoster[5]))
        #片名
        self.movTitleLabel_1.setText(self.movTitle[0])
        self.movTitleLabel_2.setText(self.movTitle[1])
        self.movTitleLabel_3.setText(self.movTitle[2])
        self.movTitleLabel_4.setText(self.movTitle[3])
        self.movTitleLabel_5.setText(self.movTitle[4])
        self.movTitleLabel_6.setText(self.movTitle[5])
        #导演
        self.movDirectorLabel_1.setText(self.movDirector[0])
        self.movDirectorLabel_2.setText(self.movDirector[1])
        self.movDirectorLabel_3.setText(self.movDirector[2])
        self.movDirectorLabel_4.setText(self.movDirector[3])
        self.movDirectorLabel_5.setText(self.movDirector[4])
        self.movDirectorLabel_6.setText(self.movDirector[5])
        #评分
        self.movScoreLabel_1.setText(self.movScore[0])
        self.movScoreLabel_2.setText(self.movScore[1])
        self.movScoreLabel_3.setText(self.movScore[2])
        self.movScoreLabel_4.setText(self.movScore[3])
        self.movScoreLabel_5.setText(self.movScore[4])
        self.movScoreLabel_6.setText(self.movScore[5])

        #详情按钮
        if self.movTitle[0] == '':
            self.detBt_1.setVisible(False)
        else:
            self.detBt_1.setVisible(True)
        if self.movTitle[1] == '':
            self.detBt_2.setVisible(False)
        else:
            self.detBt_2.setVisible(True)
        if self.movTitle[2] == '':
            self.detBt_3.setVisible(False)
        else:
            self.detBt_3.setVisible(True)
        if self.movTitle[3] == '':
            self.detBt_4.setVisible(False)
        else:
            self.detBt_4.setVisible(True)
        if self.movTitle[4] == '':
            self.detBt_5.setVisible(False)
        else:
            self.detBt_5.setVisible(True)
        if self.movTitle[5] == '':
            self.detBt_6.setVisible(False)
        else:
            self.detBt_6.setVisible(True)

    #改变列表值
    def evalue(self):
        self.movPoster = []  # 海报
        self.movTitle = []  # 电影名称
        self.movDirector = []  # 导演
        self.movScore = []  # 评分
        #为列表赋值
        for i in range(6):
            if self.curMov >= self.movNum:
                self.movPoster.append('')
                self.movTitle.append('')
                self.movDirector.append('')
                self.movScore.append('')
            else:
                #获取电影详细信息
                movDetails = self.sql.movID_get_details(self.get_movID[self.curMov])
                poster = './poster/'+ str(self.get_movID[self.curMov]) + '.jpg'
                title = '片名：'+ movDetails['moviename']
                direc = '导演：' + movDetails['director']
                score = '评分：' + str(movDetails['score'])
                self.movPoster.append(poster)
                self.movTitle.append(title)
                self.movDirector.append(direc)
                self.movScore.append(score)
            self.curMov += 1
        self.last_page.setEnabled(False)

    #初始化分类界面布局
    def classLayout(self):
        #搜索栏
        self.search_hbox = QHBoxLayout()
        self.search_hbox.addStretch(5)
        self.search_hbox.addWidget(self.class_search)
        self.search_hbox.addWidget(self.class_search_bt)
        self.search_hbox.addStretch(1)

        #贴上三个QComBox
        self.type_hbox = QHBoxLayout()
        self.type_hbox.addStretch(1)
        self.type_hbox.addWidget(self.genres_label)
        self.type_hbox.addWidget(self.cb_gen)
        self.type_hbox.addStretch(2)
        self.type_hbox.addWidget(self.region_label)
        self.type_hbox.addWidget(self.cb_region)
        self.type_hbox.addStretch(2)
        self.type_hbox.addWidget(self.age_label)
        self.type_hbox.addWidget(self.cb_age)
        self.type_hbox.addStretch(4)

        #两个hbox分别存放三部电影
        self.movies_hbox1 = QHBoxLayout()
        self.movies_hbox2 = QHBoxLayout()

        #六个电影标签
        self.mov_hbox1 = QHBoxLayout()
        self.mov_hbox2 = QHBoxLayout()
        self.mov_hbox3 = QHBoxLayout()
        self.mov_hbox4 = QHBoxLayout()
        self.mov_hbox5 = QHBoxLayout()
        self.mov_hbox6 = QHBoxLayout()

        #电影标签模块左右布局，海报+电影信息
        #电影信息垂直布局
        self.mov_info_1 = QVBoxLayout()
        self.mov_info_2 = QVBoxLayout()
        self.mov_info_3 = QVBoxLayout()
        self.mov_info_4 = QVBoxLayout()
        self.mov_info_5 = QVBoxLayout()
        self.mov_info_6 = QVBoxLayout()

        #添加电影信息到每个布局
        self.mov_info_1.addWidget(self.movTitleLabel_1)
        self.mov_info_1.addWidget(self.movDirectorLabel_1)
        self.mov_info_1.addWidget(self.movScoreLabel_1)
        self.mov_info_1.addWidget(self.detBt_1)

        self.mov_info_2.addWidget(self.movTitleLabel_2)
        self.mov_info_2.addWidget(self.movDirectorLabel_2)
        self.mov_info_2.addWidget(self.movScoreLabel_2)
        self.mov_info_2.addWidget(self.detBt_2)

        self.mov_info_3.addWidget(self.movTitleLabel_3)
        self.mov_info_3.addWidget(self.movDirectorLabel_3)
        self.mov_info_3.addWidget(self.movScoreLabel_3)
        self.mov_info_3.addWidget(self.detBt_3)

        self.mov_info_4.addWidget(self.movTitleLabel_4)
        self.mov_info_4.addWidget(self.movDirectorLabel_4)
        self.mov_info_4.addWidget(self.movScoreLabel_4)
        self.mov_info_4.addWidget(self.detBt_4)

        self.mov_info_5.addWidget(self.movTitleLabel_5)
        self.mov_info_5.addWidget(self.movDirectorLabel_5)
        self.mov_info_5.addWidget(self.movScoreLabel_5)
        self.mov_info_5.addWidget(self.detBt_5)

        self.mov_info_6.addWidget(self.movTitleLabel_6)
        self.mov_info_6.addWidget(self.movDirectorLabel_6)
        self.mov_info_6.addWidget(self.movScoreLabel_6)
        self.mov_info_6.addWidget(self.detBt_6)

        #电影标签布局加入电影海报和电影信息
        self.mov_hbox1.addWidget(self.movPosterLabel_1)
        self.mov_hbox1.addLayout(self.mov_info_1)

        self.mov_hbox2.addWidget(self.movPosterLabel_2)
        self.mov_hbox2.addLayout(self.mov_info_2)

        self.mov_hbox3.addWidget(self.movPosterLabel_3)
        self.mov_hbox3.addLayout(self.mov_info_3)

        self.mov_hbox4.addWidget(self.movPosterLabel_4)
        self.mov_hbox4.addLayout(self.mov_info_4)

        self.mov_hbox5.addWidget(self.movPosterLabel_5)
        self.mov_hbox5.addLayout(self.mov_info_5)

        self.mov_hbox6.addWidget(self.movPosterLabel_6)
        self.mov_hbox6.addLayout(self.mov_info_6)

        #六个电影布局添分别添加到两个movies_hbox
        self.movies_hbox1.addLayout(self.mov_hbox1)
        self.movies_hbox1.addLayout(self.mov_hbox2)
        self.movies_hbox1.addLayout(self.mov_hbox3)

        self.movies_hbox2.addLayout(self.mov_hbox4)
        self.movies_hbox2.addLayout(self.mov_hbox5)
        self.movies_hbox2.addLayout(self.mov_hbox6)

        #页数变换
        self.page_hbox = QHBoxLayout()
        self.page_hbox.addStretch(3)
        self.page_hbox.addWidget(self.last_page)
        self.page_hbox.addWidget(self.next_page)
        self.page_hbox.addStretch(1)

        #贴上按分类搜索出来的电影
        self.class_vbox = QVBoxLayout()
        self.class_vbox.addLayout(self.search_hbox)
        self.class_vbox.addLayout(self.type_hbox)
        self.class_vbox.addLayout(self.movies_hbox1)
        self.class_vbox.addLayout(self.movies_hbox2)
        self.class_vbox.addLayout(self.page_hbox)

        self.tab_class.setLayout(self.class_vbox)

    #完善分类界面控件功能
    def classConsum(self):
        self.class_search_bt.clicked.connect(self.search_movName) #searchButton连接到earch_movName方法获取相关电影ID
        self.cb_gen.currentTextChanged.connect(self.match_gen)#选项发生改变时发射信号
        self.cb_region.currentTextChanged.connect(self.match_reg)
        self.next_page.clicked.connect(self.nextPage) #点击触发槽函数
        self.last_page.clicked.connect(self.lastPage)

        #详情
        self.detBt_1.clicked.connect(lambda:self.showDet(self.get_movID[self.curMov-6]))
        self.detBt_2.clicked.connect(lambda: self.showDet(self.get_movID[self.curMov - 5]))
        self.detBt_3.clicked.connect(lambda: self.showDet(self.get_movID[self.curMov - 4]))
        self.detBt_4.clicked.connect(lambda: self.showDet(self.get_movID[self.curMov - 3]))
        self.detBt_5.clicked.connect(lambda: self.showDet(self.get_movID[self.curMov - 2]))
        self.detBt_6.clicked.connect(lambda: self.showDet(self.get_movID[self.curMov - 1]))

    #重新获取类型
    def match_gen(self,i):
        self.gen = self.cb_gen.currentText()
        self.transVar()

    #重新获取地区
    def match_reg(self):
        self.reg = self.cb_region.currentText()
        self.transVar()

    #获取匹配QComBox所选类型的电影id列表
    def match_mov(self):
        self.gen = self.cb_gen.currentText()
        self.reg = self.cb_region.currentText()
        gen_list = self.sql.genresSearch(self.gen) #包含所选类型的电影ID列表
        reg_list = self.sql.regionSearch(self.reg) #包含所选地区类型的电影ID列表
        self.get_movID = [x for x in gen_list if x in reg_list] #所选类型和地区的电影ID列表
        self.movNum = len(self.get_movID) #电影数量
        self.sortMov()

    #显示下一页
    def nextPage(self):
        self.evalue()
        self.resetLabel()
        self.last_page.setEnabled(True)
        if self.curMov >= self.movNum:
            self.next_page.setEnabled(False)

    #显示上一页
    def lastPage(self):
        self.curMov -= 12
        self.evalue()
        self.resetLabel()
        self.next_page.setEnabled(True)
        if self.curMov < 12:
            self.last_page.setEnabled(False)

    #搜素电影
    def search_movName(self):
        self.get_movID = self.sql.movName_get_movID(self.class_search.text()) #获取包含所搜索的名字的电影ID 列表
        self.curMov = 0
        self.movNum = len(self.get_movID)
        self.sortMov()
        self.evalue()
        self.resetLabel()
        self.last_page.setEnabled(False)
        if self.movNum <= 6:
            self.next_page.setEnabled(False)

    #显示详细页面
    def showDet(self,movid):
        self.detail.showDet(movid)

    #将获得的电影ID列表按评分排序
    def sortMov(self):
        scoreDict = {}
        for i in range(self.movNum):
            score = self.sql.getScore(self.get_movID[i])
            scoreDict[self.get_movID[i]] = score
        self.get_movID = sorted(scoreDict,key=scoreDict.__getitem__,reverse=True)

    #获取对应movieID列表
    def selecGenres(self):
        pass

    #个人主页初始化
    def tab_homepageUI(self):
        self.homeageCon()
        self.homepageLayout()
        self.homepageConsum()
        self.setLabelFalse() #初始不显示海报标签等

    #添加个人主页控件
    def homeageCon(self):
        self.TitleLabel = QLabel() #给...的最佳推荐
        self.lineLabel = QLabel() #分割线
        self.logIn_button = QPushButton('登录')
        self.signIn_button = QPushButton('注册')

        #电影海报和点击查看详情按钮
        self.poster_1 = QLabel()
        self.poster_2 = QLabel()
        self.poster_3 = QLabel()
        self.det_bt_1 = QPushButton('查看详情')
        self.det_bt_2 = QPushButton('查看详情')
        self.det_bt_3 = QPushButton('查看详情')

        #翻页按钮
        self.last_bt = QPushButton('上一页')
        self.next_bt = QPushButton('下一页')

        #修改信息和退出登录按钮
        self.modify_bt = QPushButton('修改信息')
        self.signOut_bt = QPushButton('退出登录')

    #初始化个人主页布局
    def homepageLayout(self):
        fontTitle = QFont()
        fontTitle.setBold(True)#加粗
        fontTitle.setPointSize(30)#字体大小
        self.TitleLabel.setFont(fontTitle) #大标签的字体
        self.TitleLabel.setText("<font color=%s>%s</font>" % ('#005500','为你推荐'))
        self.lineLabel.setText("<font color=%s>%s</font>" % ('#005500','--------------------------------------------------------------------------------------------------------------'))

        self.title_hbox = QHBoxLayout()
        self.title_hbox.addStretch(1)
        self.title_hbox.addWidget(self.TitleLabel)
        self.title_hbox.addStretch(3)
        self.title_hbox.addWidget(self.logIn_button)
        self.title_hbox.addWidget(self.signIn_button)
        self.title_hbox.addWidget(self.modify_bt)
        self.title_hbox.addWidget(self.signOut_bt)

        #分别存放三部电影的信息
        self.hp_mov_vbox_1 = QVBoxLayout()
        self.hp_mov_vbox_2 = QVBoxLayout()
        self.hp_mov_vbox_3 = QVBoxLayout()

        #电影内容
        self.hp_mov_vbox_1.addStretch(1)
        self.hp_mov_vbox_1.addWidget(self.poster_1)
        self.hp_mov_vbox_1.addWidget(self.det_bt_1)
        self.hp_mov_vbox_1.addStretch(1)

        self.hp_mov_vbox_2.addStretch(1)
        self.hp_mov_vbox_2.addWidget(self.poster_2)
        self.hp_mov_vbox_2.addWidget(self.det_bt_2)
        self.hp_mov_vbox_2.addStretch(1)

        self.hp_mov_vbox_3.addStretch(1)
        self.hp_mov_vbox_3.addWidget(self.poster_3)
        self.hp_mov_vbox_3.addWidget(self.det_bt_3)
        self.hp_mov_vbox_3.addStretch(1)


        self.movHbox = QHBoxLayout()
        #电影添加到横向布局
        self.movHbox.addStretch(1)
        self.movHbox.addLayout(self.hp_mov_vbox_1)
        self.movHbox.addStretch(1)
        self.movHbox.addLayout(self.hp_mov_vbox_2)
        self.movHbox.addStretch(1)
        self.movHbox.addLayout(self.hp_mov_vbox_3)
        self.movHbox.addStretch(1)

        self.hp_page_hbox = QHBoxLayout()
        self.hp_page_hbox.addStretch(3)
        self.hp_page_hbox.addWidget(self.last_bt)
        self.hp_page_hbox.addWidget(self.next_bt)
        self.hp_page_hbox.addStretch(1)


        self.hp_layout = QVBoxLayout()
        self.hp_layout.addLayout(self.title_hbox)
        self.hp_layout.addWidget(self.lineLabel)
        self.hp_layout.addStretch(1)
        self.hp_layout.addLayout(self.movHbox)
        self.hp_layout.addStretch(1)
        self.hp_layout.addLayout(self.hp_page_hbox)
        self.hp_layout.addStretch(1)
        self.tab_homepage.setLayout(self.hp_layout)

    #完善个人主页控件功能
    def homepageConsum(self):
        self.logIn_button.clicked.connect(self.toLog)
        self.det_bt_1.clicked.connect(lambda:self.showDet(self.user_rec_movid[self.curRec-3]))
        self.det_bt_2.clicked.connect(lambda: self.showDet(self.user_rec_movid[self.curRec - 2]))
        self.det_bt_3.clicked.connect(lambda: self.showDet(self.user_rec_movid[self.curRec - 1]))

        self.last_bt.clicked.connect(self.last_recPage)
        self.next_bt.clicked.connect(self.next_recPage)

        self.modify_bt.clicked.connect(self.modify)
        self.signOut_bt.clicked.connect(self.signOut)

    #登录
    def toLog(self):
        self.user_id = 11
        self.recmov(self.user_id)

    #将登录前标签设置不显示
    def setLabelFalse(self):
        self.poster_1.setVisible(False)
        self.poster_2.setVisible(False)
        self.poster_3.setVisible(False)
        self.det_bt_1.setVisible(False)
        self.det_bt_2.setVisible(False)
        self.det_bt_3.setVisible(False)
        self.modify_bt.setVisible(False)
        self.signOut_bt.setVisible(False)
        self.last_bt.setVisible(False)
        self.next_bt.setVisible(False)
        self.logIn_button.setVisible(True)
        self.signIn_button.setVisible(True)

    #登录后显示电影信息标签
    def setLabelTrue(self):
        self.poster_1.setVisible(True)
        self.poster_2.setVisible(True)
        self.poster_3.setVisible(True)
        self.det_bt_1.setVisible(True)
        self.det_bt_2.setVisible(True)
        self.det_bt_3.setVisible(True)
        self.last_bt.setVisible(True)
        self.next_bt.setVisible(True)
        self.modify_bt.setVisible(True)
        self.signOut_bt.setVisible(True)
        self.logIn_button.setVisible(False)
        self.signIn_button.setVisible(False)
        self.last_bt.setEnabled(False)

    #登录成功后login类调用该函数以显示推荐电影
    def recmov(self,userid):
        # 根据userid，获取推荐电影列表
        self.setLabelTrue() # 显示信息标签，隐藏登录注册按钮
        rec = self.cf.recmov(userid) # 获取推荐电影id列表
        self.user_rec_movid = []
        for i in range(len(rec)):
            self.user_rec_movid.append(rec[i][0])
        self.recmovNum = len(self.user_rec_movid) # 为用户推荐的电影数量
        self.curRec = 0  # 当前推荐列表索引
        #重置标签列表，并更换标签的值
        self.evalueRecList()
        self.resetHPmov()

    #推荐电影后重置标签内容
    def resetHPmov(self):
        self.poster_1.setPixmap(QPixmap(self.rec_poster[0]))
        self.poster_2.setPixmap(QPixmap(self.rec_poster[1]))
        self.poster_3.setPixmap(QPixmap(self.rec_poster[2]))

    def evalueRecList(self):
        self.rec_poster = [] #存放海报标签
        for i in range(3):
            if self.curRec >= self.recmovNum:
                self.rec_poster.append('')
            else:
                n = self.user_rec_movid[self.curRec]
                n = int(n)
                poster = './poster/' + str(n) + '.jpg'
                self.rec_poster.append(poster)
            self.curRec += 1

    def last_recPage(self):
        self.curRec -= 6
        self.evalueRecList()
        self.resetHPmov()
        self.next_bt.setEnabled(True)
        if self.curRec < 6:
            self.last_bt.setEnabled(False)

    def next_recPage(self):
        self.evalueRecList()
        self.resetHPmov()
        self.last_bt.setEnabled(True) #点击下一页后设置上一页按钮可使用
        if self.curRec >= 18:
            self.next_bt.setEnabled(False)

    def modify(self):
        pass

    def signOut(self):
        self.setLabelFalse()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainUI()
    ui.show()
    #ui.recmov(11)
    sys.exit(app.exec_())
