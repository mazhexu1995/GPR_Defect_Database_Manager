# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1152, 731)
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 60, 1061, 91))
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
        self.OK_Button = QtWidgets.QPushButton(self.groupBox)
        self.OK_Button.setGeometry(QtCore.QRect(770, 40, 111, 31))
        self.OK_Button.setObjectName("OK_Button")
        self.All_Button = QtWidgets.QPushButton(self.groupBox)
        self.All_Button.setGeometry(QtCore.QRect(910, 40, 111, 31))
        self.All_Button.setObjectName("All_Button")
        self.fileName = QtWidgets.QComboBox(self.groupBox)
        self.fileName.setGeometry(QtCore.QRect(560, 41, 171, 31))
        self.fileName.setObjectName("fileName")
        self.fileName.addItem("")
        self.fileName.addItem("")
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
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(660, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(780, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "??? ???"))
        self.label_2.setText(_translate("Dialog", "?????????"))
        self.label.setText(_translate("Dialog", "???????????????"))
        self.OK_Button.setText(_translate("Dialog", "??????"))
        self.All_Button.setText(_translate("Dialog", "????????????"))
        self.fileName.setItemText(0, _translate("Dialog", "????????????"))
        self.fileName.setItemText(1, _translate("Dialog", "??????"))
        self.selectCount.setText(_translate("Dialog", "??????????????????"))
        self.researchAll.setText(_translate("Dialog", "??????????????????"))
        self.pushButton.setText(_translate("Dialog", "??????????????????"))
        self.label_3.setText(_translate("Dialog", "??????????????????"))
        self.comboBox.setItemText(0, _translate("Dialog", "??????"))
        self.comboBox.setItemText(1, _translate("Dialog", "??????"))
        self.comboBox.setItemText(2, _translate("Dialog", "??????"))

