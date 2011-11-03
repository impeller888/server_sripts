#!/usr/bin/python
# coding: utf-8
import sys
import avto_db
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import kinterbasdb
import codecs
import urllib
from xml.etree.ElementTree import ElementTree

conn = ''
model = ''

# ===============================================================================
# Класс модели таблицы для tableView, наследующий QAbstractTableModel
class Model(QAbstractTableModel):
    def __init__(self, parent):
        QAbstractTableModel.__init__(self)
        self.gui = parent
        self.colLabels = [u'Дата',u'Дистанция',u'Литры',u'Цена',u'Сумма']

    def rowCount(self, parent):
        return len(self.cached)
    def columnCount(self, parent):
        return len(self.colLabels)
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole and role != Qt.EditRole:
            return QVariant()
        value = ''
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.cached[row][col]
        return QVariant(value)
    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.colLabels[section])
        return QVariant()

# ================================================================================
# Класс главного окна приложения 
class MyClass(QMainWindow,
        avto_db.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton,SIGNAL("clicked()"),self.Connect)
        self.connect(self.pushButton_3,SIGNAL("clicked()"),self.Disconnect)
        self.connect(self.append,SIGNAL("clicked()"),self.Append)
        self.connect(self.del_row,SIGNAL("clicked()"),self.Del_Row)
        self.fillFields()
        global conn
        conn = self.Connect()
        self.Update(conn)

#.................................................................................
    # Заполняет поля настроек параметрами из хайла settings.xml
    def fillFields(self):

         # Создаем дерево
         tree = ElementTree()
         # Парсим файл в созданное дерево
         tree.parse('/home/ilya/mytest/db/settings.xml')

         # Находим нужные параметры в дереве и заносим в переменные 
         user = (tree.find("user")).text
         passw = (tree.find("pass")).text
         path = (tree.find("path")).text
   
         # Заполняем поля вкладки Настройки, используя созданные переменные
         self.lineEdit.setText(path)
         self.lineEdit_2.setText(user)
         self.lineEdit_3.setText(passw)

#.................................................................................
# Разрывает соединиение с БД (пока не работает)
    def Disconnect(self):
        try: con.disconnect()
        except:
         self.lineEdit_4.setText(u"Не удалось отключиться")

#.................................................................................
# Устанавливает соединение с БД
    def Connect(self):

        # Считываем параметры соединения из текстовых полей вкладки Настройки    
        user  = str(self.lineEdit_2.text())
        passw = str(self.lineEdit_3.text())
        path  = str(self.lineEdit.text())

        try: 
         # Подключаемся к базе
         con = kinterbasdb.connect(dsn=path, user=user,  password=passw)
        except:  
         self.lineEdit_4.setText(u"Не удалось подключиться к базе ")
         return False
        self.label_2.setText(u"Подключено")
        self.lineEdit_4.setText(u"Подключение к avto_db удалось.")
        return con
    
#.................................................................................
    # Вставляет в БД новую строку при нажатии кнопки Добавить
    def Append(self):
        global conn

        # Считываем данные из полей и заносим в строковые переменные        
        data = "'" + str(self.data.text()) + "'," 
        dist = str(self.dist.text()) + ","
        litres = str(self.litres.text()) + ","
        price = str(self.price.text()) + ","
        summa = str(self.summa.text()) + ")"
        cur = conn.cursor()

        # Формируем строку запроса
        request = "insert into FUEL (DATA, DISTANCE, LITRES, PRICE, SUMMA) VALUES (" + data + dist + litres + price + summa

        # Выполняем запрос 
        cur.execute(request)
        # Подтверждаем изменения БД
        conn.commit()
        # Обновляем таблицу
        self.Update(conn)
        return True  

#.................................................................................
    # Обновляет таблицу и поля
    def Update(self,con):  
        global model
        cur = con.cursor()
    
        # Выполняем запрос
        cur.execute("select cast(Data as CHAR(24)), distance, litres, price, summa from FUEL")

        # Обрабатываем полученные данные как нам нужно
        cells = cur.fetchall()
        cells_list = []

        summ = 0.0 # Общая сумма денег за все время 
        litres = 0.0
        km = 0.0
        for row in cells:
          cells_list.append([])
          litres = litres + row[2]
          km = km + row[1]
          summ = summ + row[4]
          for item in row:   
           cells_list[len(cells_list)-1].append(item)

        # Пересоздаем модель и заносим в неё данные
        model = Model(self.tableView)
        model.cached = cells_list

        # Устанавливаем полученную модель для tableView
        self.tableView.setModel(model)

        # Заполняем поля
        self.full_summa.setText(str(summ))
        self.notes.setText(str(len(cells)))
        self.rashod_100.setText(str((litres/km)*100))
        self.start.setText(str(cells[0][0]))
        self.end.setText(str(cells[len(cells)-1][0]))
        return True
      
#.................................................................................
# Удаляет строку из таблицы по введенной дате
    def Del_Row(self):
        global conn
        cur = conn.cursor()
        data = "'" + str(self.data_del.text()) + "'"
        request = "delete from FUEL where data = " + data
        cur.execute(request)
        conn.commit()
        self.Update(conn)
        return True 
# =================================================================================

app = QApplication(sys.argv)
myclass = MyClass()
myclass.show()
app.exec_()


