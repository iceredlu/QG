import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sql import ConnetSQL
from detailsPage import movDetails


class signIn(QWidget):
    def __init__(self):
        super().__init__()
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

        self.user_line.setPlaceholderText('输入账号')  # 完善文本框
        self.pwd_line.setPlaceholderText('输入密码')
        self.pwd2_line.setPlaceholderText('再次输入密码')

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
        layout.addWidget(self.signin_bt)
        layout.addStretch(6)

        hLayout = QHBoxLayout()
        hLayout.addStretch(1)
        hLayout.addLayout(layout)
        hLayout.addStretch(1)

        self.setLayout(hLayout)

    def initConsum(self):
        self.back_bt.clicked.connect(self.close)

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
    sys.exit(app.exec_())
