#!/usr/bin/python
# coding: utf-8
import sys
import client_ui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyClass(QMainWindow,
        client_ui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
myclass = MyClass()
myclass.show()
app.exec_()
