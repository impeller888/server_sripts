# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created: Mon Nov  9 20:00:19 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 133)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.myLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(140, 40, 251, 24))
        self.myLineEdit.setObjectName("myLineEdit")
        self.myLabel = QtGui.QLabel(self.centralwidget)
        self.myLabel.setGeometry(QtCore.QRect(50, 40, 62, 18))
        self.myLabel.setObjectName("myLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.myLineEdit, QtCore.SIGNAL("textChanged(QString)"), self.myLabel.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel.setText(QtGui.QApplication.translate("MainWindow", "Метка", None, QtGui.QApplication.UnicodeUTF8))

