#!/usr/bin/python
# coding: utf-8
import sys
import srv, bkup, menu
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from paramiko import SSHClient, AutoAddPolicy
import threading
from backup.Ssh import Server


class MyClass(QMainWindow, srv.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
	self.server = "s1"
	self.conn = None
	self.connect(self.pushButton,SIGNAL("clicked()"),self.execute)
	self.connect(self.pushButton_2,SIGNAL("clicked()"),self.turn_connect)

	self.connect(self.radioButton_isp,SIGNAL("clicked()"),self.select_isp)
	self.connect(self.radioButton_scp,SIGNAL("clicked()"),self.select_scp)
	self.connect(self.radioButton_spl,SIGNAL("clicked()"),self.select_spl)

	self.connect(self.comboBox_isp,SIGNAL("activated(int)"),self.select_isp)
	self.connect(self.comboBox_scp,SIGNAL("activated(int)"),self.select_scp)
	self.connect(self.comboBox_spl,SIGNAL("activated(int)"),self.select_spl)

	self.textEdit.setReadOnly(True)
	self.textEdit_2.setReadOnly(True)

    def turn_connect(self):
	if not self.conn: 
		self.conn = Server(str(self.server),"imir")
		print "\033[1;32mConnect pressed\033[1;m: server="+self.server+" login=imir"
		self.lineEdit_2.setText("Online")
		self.pushButton_2.setText("Disconnect")
	else:
		self.conn.kill()
		self.conn = None		
		print "\033[1;32mDisconnect pressed\033[1;m: conn="+str(self.conn) 
		self.lineEdit_2.setText("No connection")
		self.pushButton_2.setText("Connect")
  
    def execute(self):
		if self.conn:
			try:
				self.textEdit_2.append(self.conn.cmd(self.lineEdit.text()))
			except:
				self.textEdit_2.append("Error: Can not execute command.")
				print "\033[1;31mError: Can not execute command.\033[1;m" 
    def select_isp(self):
	self.server = "s"+self.comboBox_isp.currentText()
	print "\033[1;32mSelect\033[1;m: server="+self.server

    def select_scp(self):
    	self.server = "scp"+self.comboBox_scp.currentText()
	print "\033[1;32mSelect\033[1;m: server="+self.server

    def select_spl(self):
    	self.server = "spl"+self.comboBox_spl.currentText()
	print "\033[1;32mSelect\033[1;m: server="+self.server
		

#	itm = QTableWidgetItem()
#	itm.setText(str(uptime))
#	self.tableWidget.setItem(0, 2, itm);
#	itm = QTableWidgetItem()
#	itm.setText(str(la))
#	self.tableWidget.setItem(0, 3, itm); 

class Backup_window(QWidget, bkup.Ui_Form):
    def __init__(self, parent=None):
        super(Backup_window, self).__init__(parent)
        self.setupUi(self) 
    self.pushButton_2.setDisabled()		

#class Menu_window(QWidget, menu.Ui_Form):
#    def __init__(self, parent=None):
#        super(Menu_window, self).__init__(parent)
#        self.setupUi(self)
#    self.connect(self.pushButton,SIGNAL("stateChanged()"),self.en_exec)	
#    self.connect(self.pushButton,SIGNAL("stateChanged()"),self.en_backup)	

#    def en_exec(self):
#		if self.pushButton.isChecked():
#			myclass.show()
#		else: myclass.hide()			
#	 

app = QApplication(sys.argv)

myclass = MyClass()
backup_window = Backup_window()
menu_window = Menu_window()

myclass.show()
backup_window.show()
#menu_window.show()

app.exec_()
