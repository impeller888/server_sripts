# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Документы/untitled.ui'
#
# Created: Tue Dec 14 12:20:49 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 804)
        self.centralwidget = QtGui.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.files = QtGui.QTreeWidget(self.centralwidget)
        self.files.setGeometry(QtCore.QRect(20, 210, 291, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(199, 208, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 208, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.files.setPalette(palette)
        self.files.setObjectName("files")
        self.files.headerItem().setText(0, "1")
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(490, 40, 71, 27))
        self.start.setObjectName("start")
        self.todo = QtGui.QComboBox(self.centralwidget)
        self.todo.setGeometry(QtCore.QRect(30, 50, 89, 31))
        self.todo.setObjectName("todo")
        self.todo.addItem("")
        self.todo.addItem("")
        self.server = QtGui.QComboBox(self.centralwidget)
        self.server.setGeometry(QtCore.QRect(160, 50, 89, 31))
        self.server.setObjectName("server")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.server.addItem("")
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(40, 20, 81, 20))
        self.label1.setObjectName("label1")
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(180, 20, 51, 17))
        self.label2.setObjectName("label2")
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(330, 20, 51, 17))
        self.label3.setObjectName("label3")
        self.user_id = QtGui.QLineEdit(self.centralwidget)
        self.user_id.setGeometry(QtCore.QRect(300, 50, 113, 31))
        self.user_id.setObjectName("user_id")
        self.isp = QtGui.QRadioButton(self.centralwidget)
        self.isp.setGeometry(QtCore.QRect(160, 80, 109, 22))
        self.isp.setChecked(True)
        self.isp.setObjectName("isp")
        self.cpanel = QtGui.QRadioButton(self.centralwidget)
        self.cpanel.setGeometry(QtCore.QRect(160, 100, 109, 22))
        self.cpanel.setObjectName("cpanel")
        self.line1 = QtGui.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(140, 10, 16, 121))
        self.line1.setFrameShape(QtGui.QFrame.VLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.line2 = QtGui.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(280, 10, 16, 121))
        self.line2.setFrameShape(QtGui.QFrame.VLine)
        self.line2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.line3 = QtGui.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(10, 120, 611, 21))
        self.line3.setFrameShape(QtGui.QFrame.HLine)
        self.line3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.label4 = QtGui.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(110, 150, 101, 20))
        self.label4.setObjectName("label4")
        self.label5 = QtGui.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(440, 140, 61, 20))
        self.label5.setObjectName("label5")
        self.label6 = QtGui.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(290, 580, 62, 17))
        self.label6.setObjectName("label6")
        self.label7 = QtGui.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(460, 350, 41, 17))
        self.label7.setObjectName("label7")
        self.line4 = QtGui.QFrame(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(10, 550, 611, 20))
        self.line4.setFrameShape(QtGui.QFrame.HLine)
        self.line4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line4.setObjectName("line4")
        self.progress = QtGui.QProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(430, 90, 181, 21))
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.label9 = QtGui.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(120, 180, 81, 17))
        self.label9.setObjectName("label9")
        self.history = QtGui.QTextEdit(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(20, 600, 591, 161))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 0, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 0, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 147, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.history.setPalette(palette)
        self.history.setFrameShadow(QtGui.QFrame.Plain)
        self.history.setObjectName("history")
        self.line3_2 = QtGui.QFrame(self.centralwidget)
        self.line3_2.setGeometry(QtCore.QRect(10, 0, 611, 21))
        self.line3_2.setFrameShape(QtGui.QFrame.HLine)
        self.line3_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line3_2.setObjectName("line3_2")
        self.line1_2 = QtGui.QFrame(self.centralwidget)
        self.line1_2.setGeometry(QtCore.QRect(0, 10, 16, 761))
        self.line1_2.setFrameShape(QtGui.QFrame.VLine)
        self.line1_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1_2.setObjectName("line1_2")
        self.line2_2 = QtGui.QFrame(self.centralwidget)
        self.line2_2.setGeometry(QtCore.QRect(610, 10, 20, 761))
        self.line2_2.setFrameShape(QtGui.QFrame.VLine)
        self.line2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2_2.setObjectName("line2_2")
        self.line4_2 = QtGui.QFrame(self.centralwidget)
        self.line4_2.setGeometry(QtCore.QRect(10, 760, 611, 20))
        self.line4_2.setFrameShape(QtGui.QFrame.HLine)
        self.line4_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line4_2.setObjectName("line4_2")
        self.line1_3 = QtGui.QFrame(self.centralwidget)
        self.line1_3.setGeometry(QtCore.QRect(305, 130, 31, 431))
        self.line1_3.setFrameShape(QtGui.QFrame.VLine)
        self.line1_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1_3.setObjectName("line1_3")
        self.line3_3 = QtGui.QFrame(self.centralwidget)
        self.line3_3.setGeometry(QtCore.QRect(320, 330, 301, 21))
        self.line3_3.setFrameShape(QtGui.QFrame.HLine)
        self.line3_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line3_3.setObjectName("line3_3")
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(330, 170, 281, 161))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(230)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(330, 380, 281, 171))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMidLineWidth(1)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(230)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 23))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.todo.setItemText(0, QtGui.QApplication.translate("MainWindow", "Выдача", None, QtGui.QApplication.UnicodeUTF8))
        self.todo.setItemText(1, QtGui.QApplication.translate("MainWindow", "Восстановление", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(5, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(6, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(7, QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(8, QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(9, QtGui.QApplication.translate("MainWindow", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(10, QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(11, QtGui.QApplication.translate("MainWindow", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(12, QtGui.QApplication.translate("MainWindow", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(13, QtGui.QApplication.translate("MainWindow", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(14, QtGui.QApplication.translate("MainWindow", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.server.setItemText(15, QtGui.QApplication.translate("MainWindow", "17", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("MainWindow", "Действие", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("MainWindow", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("MainWindow", "user id", None, QtGui.QApplication.UnicodeUTF8))
        self.isp.setText(QtGui.QApplication.translate("MainWindow", "ISP manager", None, QtGui.QApplication.UnicodeUTF8))
        self.cpanel.setText(QtGui.QApplication.translate("MainWindow", "CPanel", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("MainWindow", "hosting server", None, QtGui.QApplication.UnicodeUTF8))
        self.label5.setText(QtGui.QApplication.translate("MainWindow", "Домены", None, QtGui.QApplication.UnicodeUTF8))
        self.label6.setText(QtGui.QApplication.translate("MainWindow", "История", None, QtGui.QApplication.UnicodeUTF8))
        self.label7.setText(QtGui.QApplication.translate("MainWindow", "Базы", None, QtGui.QApplication.UnicodeUTF8))
        self.label9.setText(QtGui.QApplication.translate("MainWindow", "Подключен", None, QtGui.QApplication.UnicodeUTF8))
        self.history.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">imir@backup1 ~ $ restore_site_files_bs.sh server8 user_0000547833 kiroshop.ru 2010-12-06</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">imir@server8.hosting.reg.ru\'s password: </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Step 1: backup server</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   /usr/local/fsbackup/restore_user.sh user_0000547833 server8.hosting.reg.ru 2010-12-06 [             ===============] [ OK ]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   mv /mnt/server8.hosting.reg.ru/tmp/restore/user_0000547833-2010-12-06.tgz ~/temp/ `/mnt/server8.hosting.reg.ru/tmp/restore/user_0000547833-2010-12-06.tgz\' -&gt; `/home/imir/temp/user_0000547833-2010-12-06.tgz\'</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">removed `/mnt/server8.hosting.reg.ru/tmp/restore/user_0000547833-2010-12-06.tgz\'</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[ OK ]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   tar xzf ~/temp/user_0000547833-2010-12-06.tgz user_0000547833/data/www/kiroshop.ru [ OK ]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   tar czf kiroshop.ru_2010-12-06.tgz kiroshop.ru [ OK ]changed ownership of `kiroshop.ru_2010-12-06.tgz\' to imir:imir</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[ OK ]rm -f /home/imir/temp/user_0000547833-2010-12-06.tgz</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rm -rf /home/imir/temp/user_0000547833/data/www/kiroshop.ru</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   scp kiroshop.ru_2010-12-06.tgz server8.hosting.reg.ru:~/temp/ </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">imir@server8.hosting.reg.ru\'s password: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kiroshop.ru_2010-12-06.tgz                                           100%   19MB   9.5MB/s   00:02    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[ OK ]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Step 2: server8 server</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">imir@server8.hosting.reg.ru\'s password: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">`/var/www/user_0000547833/data/www/kiroshop.ru\' -&gt; `/var/www/user_0000547833/data/www/kiroshop.ru.2010-12-07.15273\'</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   mv ~/temp/kiroshop.ru_2010-12-06.tgz /var/www/user_0000547833/data/www/ [ OK ]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   tar xzf kiroshop.ru_2010-12-06.tgz [ OK ]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   chown -R user_0000547833:user_0000547833 kiroshop.ru [ OK ]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   rm kiroshop.ru_2010-12-06.tgz [ OK ]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Job complete!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "domain1.ru", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(1, 0).setText(QtGui.QApplication.translate("MainWindow", "domain2.su", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(2, 0).setText(QtGui.QApplication.translate("MainWindow", "доменю.рф", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget_2.setSortingEnabled(True)
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "u2742374_default", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.item(1, 0).setText(QtGui.QApplication.translate("MainWindow", "u2742374_forum", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.item(2, 0).setText(QtGui.QApplication.translate("MainWindow", "u2742374_drupal", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

