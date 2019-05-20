from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from sql import ConnetSQL

class modifyInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.sql = ConnetSQL()
        self.initUI()

    def initUI(self):
        self.resize(480,400)

        self.setWindowFlag(Qt.FramelessWindowHint)# 设置无框

        palette = QPalette()#设置背景色
        palette.setColor(palette.Background,QColor(0, 77, 64))
        self.setPalette(palette)

        self.initCon()
        self.initLayout()
        self.initConsum()

    def initCon(self):
        self.closeButton = QPushButton('<',self)
        self.changePwdLabel = QLabel(self)
        self.changePwdLabel.setText("<font color=%s>%s</font>" % ('#ffffff','修改密码'))
        self.changePwfLine_1 = QLineEdit(self)
        self.changePwfLine_1.setPlaceholderText('输入原始密码')
        self.changePwfLine_2 = QLineEdit(self)
        self.changePwfLine_2.setPlaceholderText('输入新密码')
        self.changePwfLine_3 = QLineEdit(self)
        self.changePwfLine_3.setPlaceholderText('重复新密码')
        self.changePwdBt = QPushButton('修改',self)
        # 表示密码输入
        self.changePwfLine_1.setEchoMode(QLineEdit.Password)
        self.changePwfLine_2.setEchoMode(QLineEdit.Password)
        self.changePwfLine_3.setEchoMode(QLineEdit.Password)

        self.changePwdBt.setEnabled(False)

    def initLayout(self):
        self.changePwdBt.setGeometry(20, 20, 50, 25)

        self.vLayout = QVBoxLayout()
        self.vLayout.addStretch(5)
        self.vLayout.addWidget(self.changePwdLabel)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.changePwfLine_1)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.changePwfLine_2)
        self.vLayout.addStretch(1)
        self.vLayout.addWidget(self.changePwfLine_3)
        self.vLayout.addStretch(2)
        self.vLayout.addWidget(self.changePwdBt)
        self.vLayout.addStretch(6)

        self.layout = QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.addLayout(self.vLayout)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def initConsum(self):
        self.closeButton.clicked.connect(self.closePage)
        #文本信息改变时检查输入
        self.changePwfLine_1.textChanged.connect(self.check_input)
        self.changePwfLine_2.textChanged.connect(self.check_input)
        self.changePwfLine_3.textChanged.connect(self.check_input)

        self.changePwdBt.clicked.connect(self.check_pwd)

    #检查输入
    def check_input(self):
        #同时有输入时检查密码是否匹配，再检查输入密码是否相同，结果都为真时执行修改
        if self.changePwfLine_1.text() and self.changePwfLine_2.text() and self.changePwfLine_3.text():
            self.changePwdBt.setEnabled(True)
        else:
            self.changePwdBt.setEnabled(False)

    #检查插入信息正确性
    def check_pwd(self):
        if self.sql.match_userID(self.userid,self.changePwfLine_1.text()):
            if self.changePwfLine_2.text() == self.changePwfLine_3.text():
                self.changePwd()
                QMessageBox.information(self,'Info','密码修改成功')
                self.close()
            else:
                QMessageBox.critical(self,'wrong','两次输入密码不匹配')
        else:
            QMessageBox.critical(self,'wrong','原密码输入错误')
            self.changePwfLine_1.clear()


    def changePwd(self):
        id = self.userid
        pwd = self.changePwfLine_2.text()
        self.sql.changePwd(id,pwd)

    #获取用户id信息，打开修改信息界面
    def modify(self,id):
        self.userid = id
        self.show()

    #关闭页面
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = modifyInfo()
    ui.show()
    sys.exit(app.exec_())