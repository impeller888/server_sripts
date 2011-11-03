#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
import timeui
import time
from timeit import Timer
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def fibonacci():        # генератор (а не функция, т.к. оператор return заменён на yield)
   a,b = 0,1
   while True:
      yield a         # return a, + запоминаем место рестарта для следующего вызова
      a,b = b,a+b

class MyClass(QMainWindow,
        timeui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Timing Attack test program')
        self.pushButton.setText(u"Старт")
        self.connect(self.pushButton,SIGNAL("clicked()"),self._compute)
        self.plainTextEdit.setReadOnly(1)

#---------Кнопка1-----------------
    def _compute(self):
     x = int(myclass.lineEdit.text())
     y = int(myclass.lineEdit_2.text())
     str1=""
     try: 
      t1 = time.time()
#      for i in fibonacci():
#       if i<x:  
#        str1=str1+str(i)+"\n"
#       else:
#        break
      z=x*y*x*y*x*y*x*y 
      t2 = time.time()
     except:
      myclass.listWidget.addItem(u"Ошибка во время замера времени")
#-----timeit-----------------------
#     x = 123
#     t1 = Timer('x + y', 'from __main__ import x','from __main__ import y')
#     t2 = Timer('x * y', 'from __main__ import x', 'from __main__ import y')
#     number_of_calls = 1000
#     time1 = t1.timeit(number = number_of_calls)
#     time2 = t2.timeit(number = number_of_calls)
#-----/timeit-----------------------------
     try:
      myclass.plainTextEdit.clear()
      myclass.plainTextEdit.insertPlainText(str(t2-t1))
     except:  
      myclass.listWidget.addItem(u"Ошибка вывода в область plainTextEdit")     
     try:
      myclass.lineEdit_3.clear()
     # myclass.lineEdit_3.setText((time2/time1))
     except: 
      myclass.listWidget.addItem(u"Ошибка вывода в область lineEdit_3")     
#---------/Кнопка1-----------------


app = QApplication(sys.argv)
myclass = MyClass()

myclass.show()
app.exec_()
