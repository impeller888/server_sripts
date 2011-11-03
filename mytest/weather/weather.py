#!/usr/bin/python
# coding: utf-8
import sys
import gui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from xml.etree.ElementTree import ElementTree
from lxml import etree
import urllib2

class MyClass(QMainWindow,
        gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.update,SIGNAL("clicked()"),self.Update)
        self.Update() 
        self.comboBox.detEditText()  
    def Update(self):
        tod = [u"Ночь",u"Утро",u"День",u"Вечер"]
        weekday = [u"Воскресенье",u"Понедельник",u"Вторник",u"Среда",u"Четверг",u"Пятница",u"Суббота"]
        cloudiness = [u"Ясно",u"Малооблачно",u"Облачно",u"Пасмурно"]
        precipitation = [u"Дождь",u"Ливень",u"Снег",u"Снег",u"Гроза",u"Нет данных",u"Без осадков"]
        url = urllib2.urlopen("http://informer.gismeteo.ru/xml/28900_1.xml")
        tree = etree.fromstring(url.read())
        fc=[]
        for fc_item in tree.findall("REPORT/TOWN/FORECAST"): 
         fc.append([])

         fc[len(fc)-1].append(fc_item.attrib['day'])           #0
         fc[len(fc)-1].append(fc_item.attrib['month'])  
         fc[len(fc)-1].append(fc_item.attrib['year'])  
         fc[len(fc)-1].append(fc_item.attrib['hour'])  
         fc[len(fc)-1].append(fc_item.attrib['tod'])  
         fc[len(fc)-1].append(fc_item.attrib['predict'])  
         fc[len(fc)-1].append(fc_item.attrib['weekday'])  
         fc[len(fc)-1].append(fc_item.attrib['tod'])           #7

         fc[len(fc)-1].append(fc_item.find("PHENOMENA").attrib['cloudiness'])  
         fc[len(fc)-1].append(fc_item.find("PHENOMENA").attrib['precipitation'])  
         fc[len(fc)-1].append(fc_item.find("PHENOMENA").attrib['rpower'])  
         fc[len(fc)-1].append(fc_item.find("PHENOMENA").attrib['spower'])  #11
 
         fc[len(fc)-1].append(fc_item.find("PRESSURE").attrib['max'])
         fc[len(fc)-1].append(fc_item.find("PRESSURE").attrib['min'])   #13
 
         fc[len(fc)-1].append(fc_item.find("TEMPERATURE").attrib['max'])  
         fc[len(fc)-1].append(fc_item.find("TEMPERATURE").attrib['min'])  #15

         fc[len(fc)-1].append(fc_item.find("WIND").attrib['min'])  
         fc[len(fc)-1].append(fc_item.find("WIND").attrib['max'])  
         fc[len(fc)-1].append(fc_item.find("WIND").attrib['direction'])   #18

         fc[len(fc)-1].append(fc_item.find("RELWET").attrib['max'])  
         fc[len(fc)-1].append(fc_item.find("RELWET").attrib['min'])  #20

         fc[len(fc)-1].append(fc_item.find("HEAT").attrib['max'])  
         fc[len(fc)-1].append(fc_item.find("HEAT").attrib['min'])  #22

         fc[len(fc)-1].append(tree.find("REPORT/TOWN").attrib['latitude'])
         fc[len(fc)-1].append(tree.find("REPORT/TOWN").attrib['longitude'])  #24
 
        self.temp_max.setValue(int(fc[0][14]))
        self.temp_min.setValue(int(fc[0][15]))
        self.date.setText(str(fc[0][0])+"."+str(fc[0][1])+"."+str(fc[0][2]))
        self.weekday.setText(weekday[int(fc[0][6])-1])
        self.tod.setText(tod[int(fc[0][4])])
        self.cldn.setText(cloudiness[int(fc[0][8])])
        self.prec.setText(precipitation[int(fc[0][9])-4])
        self.pres_min.setText(fc[0][13])
        self.pres_max.setText(fc[0][12])
        self.relwet.setText(fc[0][20])
        self.lat.setText(fc[0][23])
        self.long_2.setText(fc[0][24])
        self.long_2.setText(fc[0][24])


app = QApplication(sys.argv)
myclass = MyClass()
#myclass.myLabel.setText("Hello World!")
myclass.show()
app.exec_()
