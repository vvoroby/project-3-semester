# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Desktop\natalie\dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 443)
        Dialog.setStyleSheet("background-color: rgb(225, 252, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("text-decoration: underline;\n"
"color: rgb(85, 0, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\natalie\\girl (1).png"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\natalie\\boy (2).png"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\natalie\\oblaco_pushbotton.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 7, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(29, -1, 24, -1)
        self.horizontalLayout.setSpacing(39)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setTabletTracking(False)
        self.pushButton_4.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ПОЛЬЗОВАТЕЛЬСКАЯ ИНФОРМАЦИЯ"))
        self.label_3.setText(_translate("Dialog", "ПОЛ"))
        self.label_5.setText(_translate("Dialog", "прогулка"))
        self.label_6.setText(_translate("Dialog", "спорт"))
        self.label_7.setText(_translate("Dialog", "дела"))
        self.pushButton_4.setText(_translate("Dialog", "НАЗАД"))
        self.pushButton_5.setText(_translate("Dialog", "ПРОДОЛЖИТЬ"))
        self.label_2.setText(_translate("Dialog", "ДАТА"))
        self.label_4.setText(_translate("Dialog", "ДЕЯТЕЛЬНОСТЬ"))
        self.radioButton.setText(_translate("Dialog", "Ж"))
        self.radioButton_2.setText(_translate("Dialog", "М"))