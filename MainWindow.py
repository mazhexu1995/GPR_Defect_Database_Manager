# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import datetime
import pyodbc

from PyQt5.QtWidgets import *
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
        cur.execute("SELECT DISTINCT 病害 FROM 病害表")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.classNum = rowCount
        cur.close()
        conn.close()
        return self.classNum

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1152, 731)
        self.mainMenu = Dialog
        print(Dialog.size())

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 60, 1061, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 40, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.serverAdd = QtWidgets.QLineEdit(self.groupBox)
        self.serverAdd.setGeometry(QtCore.QRect(140, 40, 301, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverAdd.sizePolicy().hasHeightForWidth())
        self.serverAdd.setSizePolicy(sizePolicy)
        self.serverAdd.setObjectName("serverAdd")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.fileName = QtWidgets.QComboBox(self.groupBox)
        self.fileName.setGeometry(QtCore.QRect(560, 41, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileName.sizePolicy().hasHeightForWidth())
        self.fileName.setSizePolicy(sizePolicy)
        self.fileName.setObjectName("fileName")
        self.fileName.addItem("雷达图像")
        self.fileName.addItem("标签")

        self.OK_Button = QtWidgets.QPushButton(self.groupBox)
        self.OK_Button.setGeometry(QtCore.QRect(770, 40, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OK_Button.sizePolicy().hasHeightForWidth())
        self.OK_Button.setSizePolicy(sizePolicy)
        self.OK_Button.setObjectName("OK_Button")

        self.All_Button = QtWidgets.QPushButton(self.groupBox)
        self.All_Button.setGeometry(QtCore.QRect(910, 40, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.All_Button.sizePolicy().hasHeightForWidth())
        self.All_Button.setSizePolicy(sizePolicy)
        self.All_Button.setObjectName("All_Button")

        self.selectCount = QtWidgets.QPushButton(Dialog)
        self.selectCount.setGeometry(QtCore.QRect(230, 170, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectCount.sizePolicy().hasHeightForWidth())
        self.selectCount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.selectCount.setFont(font)
        self.selectCount.setObjectName("selectCount")

        self.researchAll = QtWidgets.QPushButton(Dialog)
        self.researchAll.setGeometry(QtCore.QRect(80, 170, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.researchAll.sizePolicy().hasHeightForWidth())
        self.researchAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.researchAll.setFont(font)
        self.researchAll.setObjectName("researchAll")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 230, 1031, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 170, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.reserchMap = QtWidgets.QPushButton(Dialog)
        self.reserchMap.setGeometry(QtCore.QRect(530, 170, 161, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reserchMap.sizePolicy().hasHeightForWidth())
        self.reserchMap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reserchMap.setFont(font)
        self.reserchMap.setObjectName("reserchMap")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(860, 180, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(980, 180, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.defectNum = QtWidgets.QPushButton(Dialog)
        self.defectNum.setGeometry(QtCore.QRect(720, 170, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defectNum.sizePolicy().hasHeightForWidth())
        self.defectNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.defectNum.setFont(font)
        self.defectNum.setObjectName("defectNum")

        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(890, 690, 171, 28))
        self.deleteButton.setObjectName("deleteButton")

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
        self.defectNum.clicked.connect(self.defectNumMethod)
        self.deleteButton.clicked.connect(self.deleteButtonMethod)
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
        self.pushButton.setText(_translate("Dialog", "查询病害表"))
        self.label_3.setText(_translate("Dialog", "筛选病害类别"))
        self.defectNum.setText(_translate("Dialog", "病害数量"))
        self.reserchMap.setText(_translate("Dialog", "更新并生成映射表"))
        self.deleteButton.setText(_translate("Dialog", "删除选中的数据"))

        cur, conn = self.initDatabase()
        cur.execute("SELECT DISTINCT 病害 FROM 病害表")
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
        databaseCol = ["文件名", "病害数", "雷达图像", "病害标签", "图像路径", "标签路径"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()
        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)
        mutiTableSQL = (
                "SELECT 病害标签.id, 病害标签.病害数, 雷达图谱.文件名, 病害标签.文件名, 雷达图谱.路径, 病害标签.路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.id=雷达图谱.id"
                + " UNION "
                + "SELECT 病害标签.id, 病害标签.病害数, 雷达图谱.文件名, 病害标签.文件名, 雷达图谱.路径, 病害标签.路径 FROM 病害标签 RIGHT JOIN 雷达图谱 ON 病害标签.id=雷达图谱.id"
                + " ORDER BY 病害标签.id"
        )
        cur.execute(mutiTableSQL)
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        print(adminInfor)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        truncateTable = "DELETE FROM 映射表"
        cur.execute(truncateTable)
        updateID = "ALter Table 映射表 alter ID Counter(1,1)"
        cur.execute(updateID)

        insertSQL = "INSERT INTO 映射表 (文件名, 病害数, 雷达图像, 病害标签, 图像路径, 标签路径) VALUES (?, ?, ?, ?, ?, ?)"
        for i in range(0, rowCount):
            cur.execute(insertSQL, adminInfor[i][0], adminInfor[i][1], adminInfor[i][2], adminInfor[i][3],
                        adminInfor[i][4], adminInfor[i][5])
        conn.commit()
        cur.close()
        conn.close()

    def defectNumMethod(self):
        cur, conn = self.initDatabase()
        databaseCol = ["病害类型", "病害数量"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)

        cur.execute(
            "SELECT 病害, COUNT(*) FROM 病害表 GROUP BY 病害")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        sumNum = 0
        self.tableWidget.setRowCount(rowCount + 1)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol)):
                if j == len(databaseCol) - 1:
                    sumNum += adminInfor[i][j]
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem('合计'))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(str(sumNum)))
        cur.close()
        conn.close()

    def filterClassMethod(self):
        defectClass = self.comboBox.currentText()
        cur, conn = self.initDatabase()
        databaseCol = ["ID", "图像与标签名", "病害", "病害图分辨率", "病害坐标"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()
        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)
        filterDefectSQL = "SELECT ID, 文件名, 病害, 病害图分辨率, 病害坐标 FROM 病害表 WHERE [病害]='" + defectClass + "'" + " ORDER BY ID"
        print(filterDefectSQL)
        cur.execute(filterDefectSQL)
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
        databaseCol = ["ID", "文件名", "病害", "病害图分辨率", "病害坐标", "标签", "雷达图像"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)

        cur.execute(
            "SELECT 病害表.ID, 病害表.文件名, 病害表.病害, 病害表.病害图分辨率, 病害表.病害坐标,病害表.标签, 雷达图谱.文件名 FROM 病害表 LEFT JOIN 雷达图谱 ON 病害表.文件名=雷达图谱.num"
            + " UNION "
            + "SELECT 病害表.ID, 病害表.文件名, 病害表.病害, 病害表.病害图分辨率, 病害表.病害坐标,病害表.标签, 雷达图谱.文件名 FROM 病害表 RIGHT JOIN 雷达图谱 ON 病害表.文件名=雷达图谱.num"
            + " ORDER BY 病害表.ID")
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
        databaseCol = ["选中", "ID", "文件名", "路径", "上传时间"]  # 表头列
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)

        cur.execute("SELECT num AS ID,文件名, 路径, 上传时间 FROM 雷达图谱 ORDER BY ID")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol) - 1):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                # deleteButton = QtWidgets.QPushButton("删除")
                # deleteButton.clicked.connect(self.deleteClicked)
                self.check = QtWidgets.QTableWidgetItem()
                self.check.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, 0, self.check)
                self.tableWidget.setItem(i, j + 1, newItem)
                # self.tableWidget.setCellWidget(i, len(databaseCol)-1, deleteButton)
        cur.close()
        conn.close()

    def deleteButtonMethod(self):
        # print(self.tableWidget.item(0, 0).type())
        # self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        button = QMessageBox.warning(self.mainMenu, "警告", "该操作会导致数据库表中ID混乱，并删除对应文件与所有表中对应数据，是否继续?",
                                     QMessageBox.Yes | QMessageBox.No)
        if button == QMessageBox.Yes:
            rows = self.tableWidget.rowCount()
            removeState = 0
            cur, conn = self.initDatabase()
            for rows_index in range(rows - 1, -1, -1):
                checkBoxState = self.tableWidget.item(rows_index, 0).checkState()
                print(checkBoxState)
                if checkBoxState == 2:
                    deleteItem = "DELETE FROM 雷达图谱 WHERE num = '" + str(rows_index) + "'"
                    cur.execute(deleteItem)
                    conn.commit()
                    deleteItem = "DELETE FROM 病害标签 WHERE num = '" + str(rows_index) + "'"
                    cur.execute(deleteItem)
                    conn.commit()
                    deleteItem = "DELETE FROM 病害表 WHERE 文件名 = '" + str(rows_index) + "'"
                    cur.execute(deleteItem)
                    conn.commit()
                    removeState = 1
                    self.tableWidget.removeRow(rows_index)  # 删除指定行
            cur.close()
            conn.close()
            if removeState == 1:
                QMessageBox.information(self.mainMenu, "提示", "数据库表及文件已更新，删除完成")

            if removeState == 0:
                QMessageBox.information(self.mainMenu, "提示", "无删除数据")
            return
        if button == QMessageBox.No:
            return

    def selectCountMethod(self):
        cur, conn = self.initDatabase()
        databaseCol = ["选中", "ID", "文件名", "病害数", "路径", "上传时间"]  # 表头列
        # defectClass = []
        self.tableWidget.setColumnCount(len(databaseCol))
        cnt = list()

        for tup in databaseCol:
            cnt.append(tup)
        cnt.append(" ")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(cnt)

        cur.execute("SELECT num AS ID ,文件名,病害数, 路径, 上传时间 FROM 病害标签 ORDER BY ID")
        adminInfor = (cur.fetchall())
        rowCount = len(adminInfor)
        self.tableWidget.setRowCount(rowCount)
        for i in range(0, rowCount):
            for j in range(0, len(databaseCol) - 1):
                newItem = QTableWidgetItem(str(adminInfor[i][j]))
                self.check = QtWidgets.QTableWidgetItem()
                self.check.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, 0, self.check)
                self.tableWidget.setItem(i, j + 1, newItem)
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
            # updateID = "ALter Table 雷达图谱 alter ID Counter(1,1)"
            # cur.execute(updateID)
            # conn.commit()
            for file in files:
                print(file)
                filePath, fileName = os.path.split(file)
                resarchNumSQL = "SELECT COUNT(*) FROM 雷达图谱"
                cur.execute(resarchNumSQL)
                countNum = (cur.fetchall())
                dataNum = countNum[0][0] + 1
                now = datetime.datetime.now()
                # print(dataNum)
                # print("INSERT INTO 雷达图谱(文件名,路径,num) VALUES('" + str(dataNum) + fileName[-4:] + "', '" + "./数据库/雷达图像/" + str(dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "')")
                insertImageSQL = "INSERT INTO 雷达图谱(文件名,路径,num,上传时间) VALUES('" + str(dataNum) + fileName[
                                                                                               -4:] + "', '" + "./数据库/雷达图像/" + str(
                    dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "', '" + str(now.isoformat()) + "')"
                shutil.copyfile(file, './数据库/雷达图像/' + str(dataNum) + fileName[-4:])
                # print(insertImageSQL)
                cur.execute(insertImageSQL)
                conn.commit()
            cur.close()
            conn.close()
            if len(files) != 0:
                QMessageBox.information(self.mainMenu, '提示', '雷达图像上传成功')

        if self.uploadType == '标签':
            cur, conn = self.initDatabase()
            # updateID = "ALter Table 病害标签 alter ID Counter(1,1)"
            # cur.execute(updateID)
            # conn.commit()
            # updateID = "ALter Table 病害表 alter ID Counter(1,1)"
            # cur.execute(updateID)
            # conn.commit()
            for file in files:
                filePath, fileName = os.path.split(file)
                root = ET.parse(file).getroot()
                objects = root.findall('object')
                resarchNumSQL = "SELECT COUNT(*) FROM 病害标签"
                cur.execute(resarchNumSQL)
                countNum = (cur.fetchall())
                dataNum = countNum[0][0] + 1
                size = root.findall('size')
                width = size[0].find('width').text.strip()
                height = size[0].find('height').text.strip()
                print(width, height)
                for obj in objects:
                    difficult = obj.find('difficult').text.strip()
                    bbox = obj.find('bndbox')
                    xmin = bbox.find('xmin').text.strip()
                    xmax = bbox.find('xmax').text.strip()
                    ymin = bbox.find('ymin').text.strip()
                    ymax = bbox.find('ymax').text.strip()
                    print(xmin, xmax, ymin, ymax)
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
                    # insertImageSQL = "INSERT INTO 病害表(文件名, 病害, 病害位置, 标签文件) VALUES('" + str(
                    #     dataNum) + "', '" + defectClass + "', '" + str(bbox) + "', '" + fileName + "')"
                    insertDefectTableSQL = "INSERT INTO 病害表(文件名, 病害, 病害图分辨率,病害坐标, 标签) VALUES('" + str(
                        dataNum) + "', '" + defectClass + "', '(" + width + "," + height + ")', '" + "左下坐标: (" + xmin + ", " + ymin + ") 右上坐标: (" + xmax + ", " + ymax + ")', '" + str(
                        dataNum) + fileName[-4:] + "')"
                    print(insertDefectTableSQL)
                    cur.execute(insertDefectTableSQL)
                    conn.commit()
                now = datetime.datetime.now()
                insertImageSQL = "INSERT INTO 病害标签(文件名,病害数,路径,num,上传时间) VALUES('" + str(dataNum) + fileName[
                                                                                                   -4:] + "', " + "'" + str(
                    len(objects)) + "', " + "'" + "./数据库/病害标签/" + str(
                    dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "', '" + str(now.isoformat()) + "')"
                print(insertImageSQL)
                cur.execute(insertImageSQL)
                conn.commit()
                shutil.copyfile(file, './数据库/病害标签/' + str(dataNum) + fileName[-4:])
            cur.close()
            conn.close()
            if len(files) != 0:
                QMessageBox.information(self.mainMenu, '提示', '标签上传成功')


if __name__ == "__main__":
    print("当前python版本", sys.version)
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    new = MainWindow.Ui_Dialog()
    new.setupUi(widget)
    widget.show()
    sys.exit(app.exec())
