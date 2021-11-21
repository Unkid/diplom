# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/unkid/qtproj/try/sett.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setSettings(object):
    def setupUi(self, setSettings):
        setSettings.setObjectName("setSettings")
        setSettings.resize(424, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(setSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lGet = QtWidgets.QLabel(setSettings)
        self.lGet.setObjectName("lGet")
        self.verticalLayout.addWidget(self.lGet)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lDirGet = QtWidgets.QLabel(setSettings)
        self.lDirGet.setObjectName("lDirGet")
        self.horizontalLayout.addWidget(self.lDirGet)
        self.btnGet = QtWidgets.QPushButton(setSettings)
        self.btnGet.setObjectName("btnGet")
        self.horizontalLayout.addWidget(self.btnGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lOut = QtWidgets.QLabel(setSettings)
        self.lOut.setObjectName("lOut")
        self.verticalLayout.addWidget(self.lOut)
        self.lDirOut = QtWidgets.QLabel(setSettings)
        self.lDirOut.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lDirOut.setObjectName("lDirOut")
        self.verticalLayout.addWidget(self.lDirOut)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(setSettings)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btnOut = QtWidgets.QPushButton(setSettings)
        self.btnOut.setObjectName("btnOut")
        self.horizontalLayout_2.addWidget(self.btnOut)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lFormat = QtWidgets.QLabel(setSettings)
        self.lFormat.setObjectName("lFormat")
        self.verticalLayout.addWidget(self.lFormat)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkAvi = QtWidgets.QCheckBox(setSettings)
        self.checkAvi.setChecked(True)
        self.checkAvi.setObjectName("checkAvi")
        self.horizontalLayout_3.addWidget(self.checkAvi)
        self.checkMp4 = QtWidgets.QCheckBox(setSettings)
        self.checkMp4.setObjectName("checkMp4")
        self.horizontalLayout_3.addWidget(self.checkMp4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnOk = QtWidgets.QPushButton(setSettings)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_4.addWidget(self.btnOk)
        self.btnExt = QtWidgets.QPushButton(setSettings)
        self.btnExt.setObjectName("btnExt")
        self.horizontalLayout_4.addWidget(self.btnExt)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(setSettings)
        QtCore.QMetaObject.connectSlotsByName(setSettings)

    def retranslateUi(self, setSettings):
        _translate = QtCore.QCoreApplication.translate
        setSettings.setWindowTitle(_translate("setSettings", "Настройки обработки"))
        self.lGet.setText(_translate("setSettings", "Выберите путь до  папки с вашими видеозаписями:"))
        self.lDirGet.setText(_translate("setSettings", "videos"))
        self.btnGet.setText(_translate("setSettings", "Обзор"))
        self.lOut.setText(_translate("setSettings", "Выберите путь до папки сохранения и имя нового файла"))
        self.lDirOut.setText(_translate("setSettings", "output"))
        self.lineEdit.setText(_translate("setSettings", "name"))
        self.btnOut.setText(_translate("setSettings", "Обзор"))
        self.lFormat.setText(_translate("setSettings", "Выберите формат, в котором хотите сохранить видео"))
        self.checkAvi.setText(_translate("setSettings", "AVI"))
        self.checkMp4.setText(_translate("setSettings", "MP4"))
        self.btnOk.setText(_translate("setSettings", "Сохранить"))
        self.btnExt.setText(_translate("setSettings", "Выход"))
