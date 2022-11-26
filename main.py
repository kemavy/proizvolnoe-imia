import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic
from random import randrange
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QBrush, QPainterPath


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setui()

    def setui(self):
        self.setGeometry(500, 200, 800, 800)
        self.setWindowTitle('Супрематизм')

        self.flag = False
        self.btn.clicked.connect(self.b)

    def b(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            pen = QPen(Qt.yellow, 2)
            qp.setPen(pen)
            a = randrange(1, 1000)
            qp.drawEllipse(400 - a//2, 400 - a//2, a, a)
            self.flag = False
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

