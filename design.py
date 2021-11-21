# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/unkid/qtproj/try/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.dirL = QtWidgets.QLabel(self.centralwidget)
        self.dirL.setObjectName("dirL")
        self.verticalLayout.addWidget(self.dirL)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.btnSel = QtWidgets.QPushButton(self.centralwidget)
        self.btnSel.setObjectName("btnSel")
        self.horizontalLayout_3.addWidget(self.btnSel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout.addWidget(self.btnExit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обработка существующего видео"))
        self.result.setText(_translate("MainWindow", "Откройте файл"))
        self.checkBox.setText(_translate("MainWindow", "Выбрать папку и имя для обработнной видеозаписи"))
        self.dirL.setText(_translate("MainWindow", "output/"))
        self.lineEdit.setText(_translate("MainWindow", "name"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите имя файла"))
        self.btnSel.setText(_translate("MainWindow", "Обзор"))
        self.btnBrowse.setText(_translate("MainWindow", "Выберите видео"))
        self.btnExit.setText(_translate("MainWindow", "Выход"))
