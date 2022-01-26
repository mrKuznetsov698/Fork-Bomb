from PyQt6.QtCore import QSize, QRect
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox
from PyQt6.QtGui import QPixmap

imgsCount = 0
imgTitles = ['a', 'b', 'c', 'd', 'e']
imgNames = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ------------------

        self.resize(700, 350) # Размер 700 на 350
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.imgList = QtWidgets.QComboBox(self.centralwidget)
        self.imgList.setGeometry(QRect(530, 20, 161, 31))
        self.imgList.setObjectName("imgList")
        self.imgList.addItems(imgTitles)
        self.imgList.currentIndexChanged.connect(self.img_change)

        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QRect(550, 80, 121, 31))
        self.Start.setObjectName("Start")
        self.Start.setText("Выбрать")
        self.Start.clicked.connect(self.clicked)

        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QRect(0, 0, 501, 350))
        self.lbl.setText("")
        self.lbl.setObjectName("lbl")
        self.lbl.setPixmap(QPixmap(imgNames[0]).scaled(501, 350))

        self.setCentralWidget(self.centralwidget)

        # ------------------

        self.setWindowTitle("Красивые рабочие столы!")

    def clicked(self):
        # fork-бомбу сам пиши!
        pass

    def img_change(self):
        self.lbl.setPixmap(QPixmap(imgNames[self.imgList.currentIndex()]).scaled(501, 350))


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()