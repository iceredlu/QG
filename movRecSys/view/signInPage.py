import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sql import ConnetSQL

class signIn(QWidget):
    def __init__(self):
        super().__init__()
        self.sql = ConnetSQL()
        self.initUI()

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
        self.pwd2_line = QLineEdit(self)
        self.signin_bt = QPushButton('注册', self)
        self.signin_bt.setEnabled(False)

        self.user_line.setPlaceholderText('输入账号')  # 完善文本框
        self.pwd_line.setPlaceholderText('输入密码')
        self.pwd2_line.setPlaceholderText('再次输入密码')

        self.pwd_line.setEchoMode(QLineEdit.Password)
        self.pwd2_line.setEchoMode(QLineEdit.Password)

        self.typeLabel = QLabel(self)
        self.typeLabel.setText("<font color=%s>%s</font>" % ('#ffffff','选择喜欢的类型'))
        genres = ['剧情', '喜剧', '动作', '爱情', '科幻', '动画', '悬疑', '惊悚', '恐怖', '音乐', '传记', '奇幻', '冒险', '武侠']
        self.type = '剧情'
        self.type_cb = QComboBox()
        self.type_cb.addItems(genres)

    def initLayout(self):
        self.back_bt.setGeometry(20, 20, 50, 25)

        layout = QVBoxLayout()
        layout.addStretch(6)
        layout.addWidget(self.user_line)
        layout.addStretch(1)
        layout.addWidget(self.pwd_line)
        layout.addStretch(1)
        layout.addWidget(self.pwd2_line)
        layout.addStretch(2)
        layout.addWidget(self.typeLabel)
        layout.addStretch(1)
        layout.addWidget(self.type_cb)
        layout.addStretch(2)
        layout.addWidget(self.signin_bt)
        layout.addStretch(6)

        hLayout = QHBoxLayout()
        hLayout.addStretch(1)
        hLayout.addLayout(layout)
        hLayout.addStretch(1)

        self.setLayout(hLayout)

    def initConsum(self):
        self.back_bt.clicked.connect(self.close)
        self.signin_bt.clicked.connect(self.signIn)

        #检查输入
        self.user_line.textChanged.connect(self.check_input)
        self.pwd_line.textChanged.connect(self.check_input)
        self.pwd2_line.textChanged.connect(self.check_input)

        self.type_cb.currentTextChanged.connect(self.changeType)

    #改变喜欢类型
    def changeType(self):
        self.type = self.type_cb.currentText()

    def check_input(self):
        if self.user_line.text() and self.pwd_line.text() and self.pwd2_line.text():
            self.signin_bt.setEnabled(True)
        else:
            self.signin_bt.setEnabled(False)

    def signIn(self):
        id = self.user_line.text()
        pwd_1 = self.pwd_line.text()
        pwd_2 = self.pwd2_line.text()
        if self.sql.isExistUserID(id):
            QMessageBox.critical(self,'wrong','用户名已存在')
            self.user_line.clear()
        else:
            if pwd_1 == pwd_2:
                self.sql.signIn(id,pwd_2,self.type)
                QMessageBox.information(self,'info','注册成功')
                self.close()
            else:
                QMessageBox.critical(self,'wrong','两次密码输入不一致')
                self.pwd_line.clear()
                self.pwd2_line.clear()

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
    ui = signIn()
    ui.show()
    sys.exit(app.exec_())
