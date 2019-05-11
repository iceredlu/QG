from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sql import ConnetSQL

class movDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sql = ConnetSQL()

    #初始化界面
    def initUI(self):
        self.resize(550, 700)

        self.setWindowFlag(Qt.FramelessWindowHint)# 设置无框

        palette = QPalette()#设置背景色
        palette.setColor(palette.Background,QColor(178, 223, 219))
        self.setPalette(palette)

        self.initCon()
        self.initLayout()
        self.initConsum()

    #添加控件
    def initCon(self):
        self.posterLabel = QLabel(self)
        self.posterLabel.setScaledContents(True)
        self.titleLable = QLabel(self)
        self.englishNameLable = QLabel(self)
        self.directorLabel = QLabel('导演：/',self)
        self.starLabel = QLabel('演员：/',self)
        self.typeLabel = QLabel('类型：/',self)
        self.placeLabel = QLabel('地区：/',self)
        self.scoreLabel = QLabel('评分：/',self)
        self.yearLabel = QLabel('上映时间：/',self)
        self.timelongLabel = QLabel('片长：/',self)
        self.introLabel = QLabel('简介：/',self)
        self.markLine = QLineEdit(self)
        self.markLine.setPlaceholderText('输入评分(0-10)')
        self.markButton = QPushButton('√',self)
        self.closeButton = QPushButton('<',self)

    #完善控件功能
    def initConsum(self):
        self.closeButton.clicked.connect(self.closePage)
        self.markButton.clicked.connect(self.markMov)

    #布局
    def initLayout(self):
        self.initLabel()
        self.posterLabel.setGeometry(20,70,231,350)
        self.titleLable.setGeometry(260,60,280,100)
        self.englishNameLable.setGeometry(265,145,250,30)
        self.directorLabel.setGeometry(265,175,250,30)
        self.starLabel.setGeometry(265,202,250,30)
        self.typeLabel.setGeometry(265,235,250,30)
        self.placeLabel.setGeometry(265,265,250,30)
        self.scoreLabel.setGeometry(265,295,250,30)
        self.yearLabel.setGeometry(265,325,250,30)
        self.timelongLabel.setGeometry(265,355,250,30)
        self.introLabel.setGeometry(35,430,475,250)

        self.markLine.setGeometry(265,390,125,25)
        self.markButton.setGeometry(395,390,50,25)
        self.closeButton.setGeometry(20,20,50,25)

    #设置标签字体
    def initLabel(self):
        fontTitle = QFont()
        fontTitle.setBold(True)
        fontTitle.setPointSize(18)
        self.titleLable.setFont(fontTitle)
        font = QFont()
        font.setPointSize(11)
        self.englishNameLable.setFont(font)
        self.directorLabel.setFont(font)
        self.starLabel.setFont(font)
        self.typeLabel.setFont(font)
        self.placeLabel.setFont(font)
        self.scoreLabel.setFont(font)
        self.yearLabel.setFont(font)
        self.timelongLabel.setFont(font)
        self.introLabel.setWordWrap(True)
        self.titleLable.setWordWrap(True)

    #改变标签内容
    def resetLabe(self,id):
        movDet = self.sql.movID_get_details(id) #获取电影详细信息
        id = int(id)
        poster = './poster/' + str(id) + '.jpg'
        self.posterLabel.setPixmap(QPixmap(poster))
        title = movDet['moviename']
        self.titleLable.setText("<font color=%s>%s</font>" % ('#00796B',title))
        english = movDet['englishname']
        self.englishNameLable.setText("<font color=%s>%s</font>" % ('#00796B',english))
        dire = '导演：' + movDet['director']
        self.directorLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',dire))
        star = '演员：' + movDet['star']
        self.starLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',star))
        type = '类型：' + movDet['type1'] + ' '+ movDet['type2'] + ' ' + movDet['type3']
        self.typeLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',type))
        place = '地区：' + movDet['place']
        self.placeLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',place))
        score = '评分：' + str(movDet['score'])
        self.scoreLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',score))
        year = '上映时间：' + str(movDet['years'])
        self.yearLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',year))
        timelong = '片长：' + str(movDet['timelong'])
        self.timelongLabel.setText("<font color=%s>%s</font>" % ('#4DB6AC',timelong))
        intro = '    简介：' + movDet['introduction']
        self.introLabel.setText("<font color=%s>%s</font>" % ('#00897B',intro))

    #显示详细页面
    def showDet(self,id):
        self.resetLabe(id)
        self.show()
        self.raise_()

    #关闭页面
    def closePage(self):
        self.close()

    #评分
    def markMov(self):
        pass

   #判断鼠标左键是否被按下，如果按下则将flag设为True并获取当前的位置
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))  # 更改鼠标图标

    #判断鼠标是否移动并且左键被按下，若移动了计算移动的距离在移动窗口
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    #若鼠标释放了则将flag设为False
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
