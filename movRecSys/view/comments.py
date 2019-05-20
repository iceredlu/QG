from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sql import ConnetSQL

class movComment(QWidget):
    def __init__(self):
        super().__init__()
        self.sql = ConnetSQL()
        self.initUI()

    def initUI(self):
        self.resize(550, 700)

        self.setWindowFlag(Qt.FramelessWindowHint)# 设置无框

        palette = QPalette()#设置背景色
        palette.setColor(palette.Background,QColor(178, 223, 219))
        self.setPalette(palette)

        self.initCon()
        self.initLayout()
        self.initConsum()

    def initCon(self):
        self.comment_1 = QLabel(self)
        self.comment_2 = QLabel(self)
        self.comment_3 = QLabel(self)
        self.comment_4 = QLabel(self)
        self.comment_5 = QLabel(self)

        self.title = QLabel(self)
        self.setTitleFont()

        self.closeButton = QPushButton('<', self)

        self.lastPage = QPushButton('<前页',self)
        self.nextPage = QPushButton('后页>',self)

        self.lastPage.setEnabled(False)


    def initLayout(self):
        self.vLayout = QVBoxLayout()
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.title)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.comment_1)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.comment_2)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.comment_3)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.comment_4)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.comment_5)
        self.vLayout.addStretch(2)

        self.setLayout(self.vLayout)

        self.comment_1.setWordWrap(True)
        self.comment_2.setWordWrap(True)
        self.comment_3.setWordWrap(True)
        self.comment_4.setWordWrap(True)
        self.comment_5.setWordWrap(True)

        self.closeButton.setGeometry(20,20,50,25)
        self.lastPage.setGeometry(400,650,50,25)
        self.nextPage.setGeometry(455,650,50,25)

    def initConsum(self):
        self.closeButton.clicked.connect(self.close)

        self.nextPage.clicked.connect(self.next)
        self.lastPage.clicked.connect(self.last)

    #后页
    def next(self):
        self.lastPage.setEnabled(True)
        self.nextPage.setEnabled(False)
        self.setComment(5)

    def last(self):
        self.lastPage.setEnabled(False)
        self.nextPage.setEnabled(True)
        self.setComment(0)

    #设置标签变量
    def setComment(self,flag):
        if len(self.comments) == 10:
            self.title.setText("<font color=%s>%s</font>" % ('#00897B', '电影短评'))
            self.comment_1.setText("<font color=%s>%s</font>" % ('#00897B', self.comments[flag]))
            self.comment_2.setText("<font color=%s>%s</font>" % ('#00897B', self.comments[flag+1]))
            self.comment_3.setText("<font color=%s>%s</font>" % ('#00897B', self.comments[flag+2]))
            self.comment_4.setText("<font color=%s>%s</font>" % ('#00897B', self.comments[flag+3]))
            self.comment_5.setText("<font color=%s>%s</font>" % ('#00897B', self.comments[flag+4]))
        else:
            self.comment_1.setText('')
            self.comment_2.setText('')
            self.comment_3.setText('')
            self.comment_4.setText('')
            self.comment_5.setText('')

    #字体
    def setTitleFont(self):
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setPointSize(18)
        self.title.setFont(titleFont)

    #获取电影id显示评论
    def getComment(self,id):
        self.comments = self.sql.getComment(id) #获取评论列表
        self.setComment(0) #设置标签变量
        self.show()

    def closePage(self):
        self.close()

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
