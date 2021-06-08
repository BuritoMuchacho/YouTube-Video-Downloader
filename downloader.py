# -*- coding: utf-8 -*-

from logging import exception
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from pytube import *
from pytube import exceptions


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(10, 150, 91, 41))
        self.btn.setObjectName("btn")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(20, 10, 241, 81))
        self.text.setObjectName("text")
        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(10, 90, 271, 31))
        self.textbox.setObjectName("textbox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # download video if button is clicked
        self.btn.clicked.connect(lambda: self.video(self.textbox.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Video Downloader"))
        self.btn.setText(_translate("MainWindow", "Download"))
        self.text.setText(_translate("MainWindow", "Paste a link to YouTube video \nand click download:"))

    def video(self, url):
        """Downloading the video"""
        self.text.setText("Downloading...")
        self.text.repaint()
        try:
            yt = YouTube(url)
            # download the .mp4 video with highest resolution
            video = yt.streams.filter(file_extension='mp4').get_highest_resolution().download(filename=yt.title)
            video = video[:-len(str(yt.title) + '.mp4')]  # path to video
            self.text.setText('Video has been saved to \n' + str(video))
            self.textbox.setText("")
            return self.text.adjustSize()
        except exceptions.RegexMatchError:  # if video not found
            self.text.setText('The link is incorrect, please try again')
        except AttributeError:
            pass
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
