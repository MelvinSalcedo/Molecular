# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_molecular.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImagenEntrada = QtWidgets.QLabel(self.centralwidget)
        self.ImagenEntrada.setGeometry(QtCore.QRect(10, 190, 351, 341))
        self.ImagenEntrada.setText("")
        self.ImagenEntrada.setObjectName("ImagenEntrada")
        self.EimagenSalida = QtWidgets.QLabel(self.centralwidget)
        self.EimagenSalida.setGeometry(QtCore.QRect(420, 200, 351, 341))
        self.EimagenSalida.setText("")
        self.EimagenSalida.setObjectName("EimagenSalida")
        self.OpenImage = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImage.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.OpenImage.setObjectName("OpenImage")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(470, 60, 279, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.DbScan = QtWidgets.QPushButton(self.splitter)
        self.DbScan.setObjectName("DbScan")
        self.Qmeans = QtWidgets.QPushButton(self.splitter)
        self.Qmeans.setObjectName("Qmeans")
        self.Qmedois = QtWidgets.QPushButton(self.splitter)
        self.Qmedois.setObjectName("Qmedois")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenImage.setText(_translate("MainWindow", "Open Image"))
        self.DbScan.setText(_translate("MainWindow", "DbScan"))
        self.Qmeans.setText(_translate("MainWindow", "Qmeans"))
        self.Qmedois.setText(_translate("MainWindow", "Qmedoids"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

