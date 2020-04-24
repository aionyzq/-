from functools import partial
from os import listdir, mkdir
from shutil import move
from sys import argv, exit
from time import time

from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 86)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件整理工具"))
        self.label.setText(_translate("MainWindow", "输入文件夹路径："))
        self.pushButton.setText(_translate("MainWindow", "整理"))

def start(ui):
    

    path = ui.lineEdit.text()
    print(path)
    e = listdir(path)
    allList = []
    path = path+'\\'
    for i in e:
        try:
            r = i.split('.')
            print(i)
            if r[0] == '' or len(r) == 1:
                continue
            print('.'.join(r))
            allList.append('.'.join(r))
            name = '.'.join(r)
            try:
                mkdir(path+'.'+r[-1])
            except:
                try:
                    move(path+name, path+'.'+r[-1])
                except FileExistsError:
                    move(path+'('+str(time()*100000)+')'+name, path+'.'+r[-1])
                continue
            move(path+name, path+'.'+r[-1])
        except:
            pass

if __name__ == '__main__':
    app = QApplication(argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(partial(start,ui))
    MainWindow.show()
    exit(app.exec_())
