# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_utilityUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 176)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_init_device = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_init_device.setGeometry(QtCore.QRect(110, 110, 91, 23))
        self.pushButton_init_device.setObjectName("pushButton_init_device")
        self.pushButton_reset_projects = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset_projects.setGeometry(QtCore.QRect(210, 110, 111, 23))
        self.pushButton_reset_projects.setObjectName("pushButton_reset_projects")
        self.textEdit_status = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_status.setGeometry(QtCore.QRect(10, 10, 311, 91))
        self.textEdit_status.setObjectName("textEdit_status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tinkert Kit Setup Utility"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_init_device.setText(_translate("MainWindow", "Initialise Device"))
        self.pushButton_reset_projects.setText(_translate("MainWindow", "Reset Project Files"))
        self.textEdit_status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Starting...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

