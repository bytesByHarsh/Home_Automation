# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(30, 340, 93, 28))
        self.connectButton.setObjectName("connectButton")
        self.disconnectBotton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectBotton.setGeometry(QtCore.QRect(170, 340, 93, 28))
        self.disconnectBotton.setObjectName("disconnectBotton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 101, 31))
        self.label_2.setObjectName("label_2")
        self.tempLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.tempLCD.setGeometry(QtCore.QRect(110, 50, 71, 31))
        self.tempLCD.setObjectName("tempLCD")
        self.humidityLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.humidityLCD.setGeometry(QtCore.QRect(110, 90, 71, 31))
        self.humidityLCD.setObjectName("humidityLCD")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 350, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.ACTemp = QtWidgets.QSlider(self.centralwidget)
        self.ACTemp.setGeometry(QtCore.QRect(350, 60, 160, 22))
        self.ACTemp.setMinimum(15)
        self.ACTemp.setMaximum(30)
        self.ACTemp.setOrientation(QtCore.Qt.Horizontal)
        self.ACTemp.setObjectName("ACTemp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 60, 131, 16))
        self.label_3.setObjectName("label_3")
        self.ACTemplcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.ACTemplcd.setGeometry(QtCore.QRect(523, 60, 71, 31))
        self.ACTemplcd.setObjectName("ACTemplcd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.ACTemp.valueChanged['int'].connect(self.ACTemplcd.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectBotton.setText(_translate("MainWindow", "Dissconnect"))
        self.label.setText(_translate("MainWindow", "Temprature"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.label_3.setText(_translate("MainWindow", "Set AC Temprature"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

