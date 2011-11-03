#!/usr/bin/python
# coding: utf-8
import sys
import myui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyClass(QMainWindow,
        myui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
myclass = MyClass()
myclass.myLabel.setText("Hello World!")
myclass.show()
app.exec_()
