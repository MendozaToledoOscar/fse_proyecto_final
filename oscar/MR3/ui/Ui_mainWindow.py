# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/FSE/GUI/MR3/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 735)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.exit_btn = QtWidgets.QPushButton(self.centralWidget)
        self.exit_btn.setGeometry(QtCore.QRect(960, 650, 141, 71))
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(741, 200, 160, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.internet_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.internet_Layout.setContentsMargins(0, 0, 0, 0)
        self.internet_Layout.setObjectName("internet_Layout")
        self.netlfix_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.netlfix_btn.setObjectName("netlfix_btn")
        self.internet_Layout.addWidget(self.netlfix_btn)
        self.prime_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.prime_btn.setObjectName("prime_btn")
        self.internet_Layout.addWidget(self.prime_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(561, 200, 160, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.video_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.video_Layout.setContentsMargins(0, 0, 0, 0)
        self.video_Layout.setObjectName("video_Layout")
        self.v_local_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.v_local_btn.setObjectName("v_local_btn")
        self.video_Layout.addWidget(self.v_local_btn)
        self.v_usb_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.v_usb_btn.setObjectName("v_usb_btn")
        self.video_Layout.addWidget(self.v_usb_btn)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(381, 200, 160, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.foto_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.foto_Layout.setContentsMargins(0, 0, 0, 0)
        self.foto_Layout.setObjectName("foto_Layout")
        self.f_local_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.f_local_btn.setObjectName("f_local_btn")
        self.foto_Layout.addWidget(self.f_local_btn)
        self.f_usb_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.f_usb_btn.setObjectName("f_usb_btn")
        self.foto_Layout.addWidget(self.f_usb_btn)
        self.internet_label = QtWidgets.QLabel(self.centralWidget)
        self.internet_label.setGeometry(QtCore.QRect(740, 160, 161, 28))
        self.internet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.internet_label.setObjectName("internet_label")
        self.video_label = QtWidgets.QLabel(self.centralWidget)
        self.video_label.setGeometry(QtCore.QRect(560, 160, 161, 28))
        self.video_label.setAlignment(QtCore.Qt.AlignCenter)
        self.video_label.setObjectName("video_label")
        self.foto_label = QtWidgets.QLabel(self.centralWidget)
        self.foto_label.setGeometry(QtCore.QRect(380, 160, 161, 28))
        self.foto_label.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_label.setObjectName("foto_label")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(200, 200, 160, 381))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.musicLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.musicLayout.setContentsMargins(0, 0, 0, 0)
        self.musicLayout.setObjectName("musicLayout")
        self.m_local_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.m_local_btn.setObjectName("m_local_btn")
        self.musicLayout.addWidget(self.m_local_btn)
        self.m_usb_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.m_usb_btn.setObjectName("m_usb_btn")
        self.musicLayout.addWidget(self.m_usb_btn)
        self.music_label = QtWidgets.QLabel(self.centralWidget)
        self.music_label.setGeometry(QtCore.QRect(200, 160, 161, 28))
        self.music_label.setAlignment(QtCore.Qt.AlignCenter)
        self.music_label.setObjectName("music_label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_btn.setText(_translate("MainWindow", "EXIT"))
        self.netlfix_btn.setText(_translate("MainWindow", "Netflix"))
        self.prime_btn.setText(_translate("MainWindow", "Prime"))
        self.v_local_btn.setText(_translate("MainWindow", "Local"))
        self.v_usb_btn.setText(_translate("MainWindow", "USB"))
        self.f_local_btn.setText(_translate("MainWindow", "Local"))
        self.f_usb_btn.setText(_translate("MainWindow", "USB"))
        self.internet_label.setText(_translate("MainWindow", "Internet"))
        self.video_label.setText(_translate("MainWindow", "Video"))
        self.foto_label.setText(_translate("MainWindow", "Foto"))
        self.m_local_btn.setText(_translate("MainWindow", "Local"))
        self.m_usb_btn.setText(_translate("MainWindow", "USB"))
        self.music_label.setText(_translate("MainWindow", "Music"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

