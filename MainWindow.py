# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import datetime
import sys
import pyodbc
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
import sys
import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET


class Ui_Dialog(object):
    databasePath = 0
    uploadType = 0
    classNum = 0

    def getClassNum(self):
        cur, conn = self.initDatabase()
        cur.execute("SELECT DISTINCT 病害类型 FROM 病害标签")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.classNum = rowCount
        cur.close()
        conn.close()
        return self.classNum

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1152, 731)
        self.mainMenu = Dialog

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 60, 1061, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.serverAdd = QtWidgets.QLineEdit(self.groupBox)
        self.serverAdd.setGeometry(QtCore.QRect(140, 40, 301, 31))
        self.serverAdd.setObjectName("serverAdd")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.fileName = QtWidgets.QComboBox(self.groupBox)
        self.fileName.setGeometry(QtCore.QRect(560, 41, 171, 31))
        self.fileName.setObjectName("fileName")
        self.fileName.addItem("雷达图像")
        self.fileName.addItem("标签")

        self.OK_Button = QtWidgets.QPushButton(self.groupBox)
        self.OK_Button.setGeometry(QtCore.QRect(770, 40, 111, 31))
        self.OK_Button.setObjectName("OK_Button")

        self.All_Button = QtWidgets.QPushButton(self.groupBox)
        self.All_Button.setGeometry(QtCore.QRect(910, 40, 111, 31))
        self.All_Button.setObjectName("All_Button")

        self.selectCount = QtWidgets.QPushButton(Dialog)
        self.selectCount.setGeometry(QtCore.QRect(290, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.selectCount.setFont(font)
        self.selectCount.setObjectName("selectCount")

        self.researchAll = QtWidgets.QPushButton(Dialog)
        self.researchAll.setGeometry(QtCore.QRect(130, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.researchAll.setFont(font)
        self.researchAll.setObjectName("researchAll")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 230, 1031, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.reserchMap = QtWidgets.QPushButton(Dialog)
        self.reserchMap.setGeometry(QtCore.QRect(610, 170, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reserchMap.setFont(font)
        self.reserchMap.setObjectName("reserchMap")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(820, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(940, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        # 获取病害种类数
        self.classNum = self.getClassNum()
        for i in range(0, self.classNum):
            self.comboBox.addItem("")
        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)


        # 初始化数据库表头
        # self.initDatabase()
        self.researchAllMethod()

        # 按钮绑定方法
        self.selectCount.clicked.connect(self.selectCountMethod)
        self.researchAll.clicked.connect(self.researchAllMethod)
        self.OK_Button.clicked.connect(self.OKButtonMethod)
        self.All_Button.clicked.connect(self.browsingFiles)
        self.pushButton.clicked.connect(self.defectClassMethod)
        self.comboBox.currentIndexChanged.connect(self.filterClassMethod)
        self.reserchMap.clicked.connect(self.reserchMapMethod)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "病害数据集管理工具"))
        self.groupBox.setTitle(_translate("Dialog", "设 置"))
        self.label_2.setText(_translate("Dialog", "上传类型"))
        self.label.setText(_translate("Dialog", "数据集路径"))
        self.OK_Button.setText(_translate("Dialog", "确定"))
        self.All_Button.setText(_translate("Dialog", "上传文件"))
        self.selectCount.setText(_translate("Dialog", "查询标签数据"))
        self.researchAll.setText(_translate("Dialog", "查询雷达图像"))
        self.pushButton.setText(_translate("Dialog", "查询病害类别"))
        self.label_3.setText(_translate("Dialog", "筛选病害类别"))
        self.reserchMap.setText(_translate("Dialog", "图像与病害映射表"))

        cur, conn = self.initDatabase()
        cur.execute("SELECT DISTINCT 病害类型 FROM 病害标签")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.classNum = rowCount
        cur.close()
        conn.close()
        for i in range(0, rowCount):
            print(str(adminInfor[i][0]))
            defectType = adminInfor[i][0]
            self.comboBox.setItemText(i, _translate("Dialog", defectType))


    def reserchMapMethod(self):
        cur, conn = self.initDatabase()
        databaseCol = ["ID", "文件名", "病害类型", "标签文件路径", "雷达文件路径"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()
        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)
        mutiTableSQL = "SELECT 病害标签.id, 病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.文件名=雷达图谱.文件名"
        cur.execute(mutiTableSQL)
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        cur.close()
        conn.close()

    def filterClassMethod(self):
        defectClass = self.comboBox.currentText()
        cur, conn = self.initDatabase()
        databaseCol = ["ID", "文件名", "病害类型", "标签文件路径", "雷达文件路径"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()
        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)
        mutiTableSQL = "SELECT 病害标签.id, 病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.文件名=雷达图谱.文件名 WHERE [病害类型]= '" + defectClass + "'"
        cur.execute(mutiTableSQL)
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        cur.close()
        conn.close()

    def defectClassMethod(self):
        cur, conn = self.initDatabase()
        databaseCol = ["病害类型", "病害数量"]  # 表头列
        # defectClass = []
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)
        cur.execute("SELECT DISTINCT 病害类型, COUNT(*) AS 病害数量 FROM 病害标签 GROUP BY 病害类型")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        cur.close()
        conn.close()

    def initDatabase(self):
        pathfile = "./数据库/数据表/病害数据集.accdb"
        connStr = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s;' % pathfile
        pyodbc.lowercase = False  # 是否将字段名转为小写
        conn = pyodbc.connect(connStr)
        cur = conn.cursor()
        return cur, conn

    def researchAllMethod(self):
        cur, conn = self.initDatabase()
        databaseCol = ["ID", "文件名", "附件路径"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)

        cur.execute("SELECT ID,文件名,附件路径 FROM 雷达图谱")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        cur.close()
        conn.close()

    def selectCountMethod(self):
        cur, conn = self.initDatabase()
        databaseCol = ["ID", "文件名", "病害类型", "附件路径"]  # 表头列
        # defectClass = []
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)

        cur.execute("SELECT ID,文件名,病害类型,附件路径 FROM 病害标签 ORDER BY ID")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        cur.close()
        conn.close()

    def OKButtonMethod(self):
        self.databasePath = self.serverAdd.text()
        self.uploadType = self.fileName.currentText()
        if len(self.databasePath) == 0:
            QMessageBox.warning(self.mainMenu, '提示', '路径不能为空')
        else:
            QMessageBox.information(self.mainMenu, '提示', '路径设置成功')
        return

    def browsingFiles(self):
        if self.databasePath == 0:
            QMessageBox.warning(self.mainMenu, '提示', '请先设置数据集路径')
            return
        files, _ = QFileDialog.getOpenFileNames(self.mainMenu, "多文件选择", self.databasePath)
        if self.uploadType == '雷达图像':
            cur, conn = self.initDatabase()
            for file in files:
                filePath, fileName = os.path.split(file)
                shutil.copyfile(file, './数据库/雷达图像/' + fileName)
                insertImageSQL = "INSERT INTO 雷达图谱(文件名,附件路径) VALUES('" + fileName[:-4] + "', '" + file + "'" + ")"
                print(insertImageSQL)
                cur.execute(insertImageSQL)
                conn.commit()
            cur.close()
            conn.close()
            QMessageBox.information(self.mainMenu, '提示', '雷达图像上传成功')

        if self.uploadType == '标签':
            cur, conn = self.initDatabase()
            for file in files:
                filePath, fileName = os.path.split(file)
                root = ET.parse(file).getroot()
                objects = root.findall('object')
                for obj in objects:
                    difficult = obj.find('difficult').text.strip()
                    bbox = obj.find('bndbox')
                    defectClass = obj.find('name').text.lower().strip()
                    print(defectClass)
                    if defectClass == 'subgrade settlement':
                        defectClass = '路基下沉'
                    if defectClass == 'settlement':
                        defectClass = '路基下沉'
                    if defectClass == 'mud':
                        defectClass = '翻浆冒泥'
                    if defectClass == 'mud pumping':
                        defectClass = '翻浆冒泥'
                    if defectClass == 'cavity':
                        defectClass = '空洞'
                    if defectClass == 'separate':
                        defectClass = '脱空'
                    if defectClass == 'loose':
                        defectClass = '疏松'
                    insertImageSQL = "INSERT INTO 病害标签(文件名,病害类型,附件路径) VALUES('" + fileName[
                                                                                  :-4] + "', '" + defectClass + "', '" + file + "'" + ")"
                    print(insertImageSQL)
                    cur.execute(insertImageSQL)
                    conn.commit()
                shutil.copyfile(file, './数据库/病害标签/' + fileName)
            cur.close()
            conn.close()
            QMessageBox.information(self.mainMenu, '提示', '标签上传成功')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    new = MainWindow.Ui_Dialog()
    new.setupUi(widget)
    widget.show()
    sys.exit(app.exec())