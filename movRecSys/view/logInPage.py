import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from signInPage import signIn
from sql import ConnetSQL

class logIn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.signIn = signIn()
        self.sql = ConnetSQL()

    def initUI(self):
        self.resize(480,400)
        self.setWindowFlag(Qt.FramelessWindowHint)  # 设置无框
        palette = QPalette()  # 设置背景色
        palette.setColor(palette.Background, QColor(0, 77, 64))
        self.setPalette(palette)

        self.initCon()
        self.initLayout()
        self.initConsum()

    def initCon(self):
        self.back_bt = QPushButton('<', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_bt = QPushButton('登录', self)
        self.signin_bt = QPushButton('注册', self)

        self.user_line.setPlaceholderText('输入账号')  # 完善文本框
        self.pwd_line.setPlaceholderText('输入密码')

    def initLayout(self):
        self.signin_bt.setGeometry(70,20,50,25)
        self.back_bt.setGeometry(20, 20, 50, 25)

        layout = QVBoxLayout()
        layout.addStretch(6)
        layout.addWidget(self.user_line)
        layout.addStretch(1)
        layout.addWidget(self.pwd_line)
        layout.addStretch(2)
        layout.addWidget(self.login_bt)
        layout.addStretch(6)

        hLayout = QHBoxLayout()
        hLayout.addStretch(1)
        hLayout.addLayout(layout)
        hLayout.addStretch(1)

        self.setLayout(hLayout)

    def initConsum(self):
        self.back_bt.clicked.connect(self.close)
        self.signin_bt.clicked.connect(self.openSignIn)
        #文本框的信号变化连接槽函数,判断是否两个框都有内容
        self.user_line.textChanged.connect(self.check_input)
        self.pwd_line.textChanged.connect(self.check_input)
        self.login_bt.clicked.connect(self.check_login)
        self.pwd_line.setEchoMode(QLineEdit.Password) #表示密码输入

    def openSignIn(self):
        self.signIn.show()

    #检查文本框输入
    def check_input(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_bt.setEnabled(True)
        else:
            self.login_bt.setEnabled(False)

    #检查用户密码是否匹配
    def check_login(self):
        id = self.user_line.text()
        pwd = self.pwd_line.text()
        if self.sql.match_userID(id,pwd):
            QMessageBox.information(self,'Info','登陆成功')
            self.flag = True
            self.close()
        else:
            QMessageBox.critical(self,'wrong','账号或密码错误')
        self.user_line.clear()
        self.pwd_line.clear()

    # 判断鼠标左键是否被按下，如果按下则将flag设为True并获取当前的位置
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))  # 更改鼠标图标

        # 判断鼠标是否移动并且左键被按下，若移动了计算移动的距离在移动窗口

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

        # 若鼠标释放了则将flag设为False

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = logIn()
    ui.show()
    sys.exit(app.exec_())