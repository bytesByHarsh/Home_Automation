# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import paho.mqtt.client as paho



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
        # Added using Signal and Slot
        self.pushButton.clicked.connect(MainWindow.close)
        self.ACTemp.valueChanged['int'].connect(self.ACTemplcd.display)

        
        self.ACTemplcd.display("15") # Display default Temp on LCD
        self.ACTemp.valueChanged['int'].connect(self.AC_Temp_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #MQTT Setup
        self.MQTT_SERVER = "localhost"
        self.MQTT_PATH = "#"
        self.port=1883
        self.mqtt_server_connected=0
        self.client = paho.Client()
        self.client.on_connect = self.on_connect_mqtt
        self.client.on_message = self.on_message_mqtt


        self.connectButton.clicked.connect(self.connect_mqtt)
        self.disconnectBotton.clicked.connect(self.disconnect_mqtt)

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

    # Function call when Connect button is pressed
    def connect_mqtt(self):
        print("Connect button pressed")
        self.client.connect(self.MQTT_SERVER, self.port, 60)
        self.client.loop_start()

    # Function call when Disconnect button is pressed
    def disconnect_mqtt(self):
        self.client.loop_stop()
        self.mqtt_server_connected=0

    # Function call when new message is recieved
    def on_message_mqtt(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        print(str(msg.payload.decode("utf-8")))
        if(str(msg.topic) =="house/temp"):
            self.tempLCD.display(str(msg.payload.decode("utf-8")))
        elif(str(msg.topic) =="house/humidity"):
            self.humidityLCD.display(str(msg.payload.decode("utf-8")))
        else:
            print("Different Topic")

    def on_connect_mqtt(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe(self.MQTT_PATH)
        self.mqtt_server_connected=1

    def AC_Temp_changed(self,val):
        #print(val)
        if(self.mqtt_server_connected==0):
            print("Connect to MQTT Server")
        else:
            self.client.publish("house/ACTemp",str(val))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

