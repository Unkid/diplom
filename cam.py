# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/unkid/qtproj/try/camcap.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_camCap(object):
    def setupUi(self, camCap):
        camCap.setObjectName("camCap")
        camCap.resize(500, 345)
        self.verticalLayout = QtWidgets.QVBoxLayout(camCap)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nameLabel = QtWidgets.QLabel(camCap)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_4.addWidget(self.nameLabel)
        self.nameL = QtWidgets.QLabel(camCap)
        self.nameL.setObjectName("nameL")
        self.horizontalLayout_4.addWidget(self.nameL)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.reportLabel = QtWidgets.QLabel(camCap)
        self.reportLabel.setObjectName("reportLabel")
        self.horizontalLayout_5.addWidget(self.reportLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reportL1 = QtWidgets.QLabel(camCap)
        self.reportL1.setObjectName("reportL1")
        self.verticalLayout_2.addWidget(self.reportL1)
        self.reportL2 = QtWidgets.QLabel(camCap)
        self.reportL2.setObjectName("reportL2")
        self.verticalLayout_2.addWidget(self.reportL2)
        self.reportL3 = QtWidgets.QLabel(camCap)
        self.reportL3.setObjectName("reportL3")
        self.verticalLayout_2.addWidget(self.reportL3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dirLabel = QtWidgets.QLabel(camCap)
        self.dirLabel.setObjectName("dirLabel")
        self.horizontalLayout_3.addWidget(self.dirLabel)
        self.dirL = QtWidgets.QLabel(camCap)
        self.dirL.setObjectName("dirL")
        self.horizontalLayout_3.addWidget(self.dirL)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.settBtn = QtWidgets.QPushButton(camCap)
        self.settBtn.setObjectName("settBtn")
        self.horizontalLayout_7.addWidget(self.settBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formatLabel = QtWidgets.QLabel(camCap)
        self.formatLabel.setObjectName("formatLabel")
        self.verticalLayout_3.addWidget(self.formatLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formatRadio1 = QtWidgets.QRadioButton(camCap)
        self.formatRadio1.setChecked(True)
        self.formatRadio1.setObjectName("formatRadio1")
        self.horizontalLayout_2.addWidget(self.formatRadio1)
        self.formatRadio2 = QtWidgets.QRadioButton(camCap)
        self.formatRadio2.setObjectName("formatRadio2")
        self.horizontalLayout_2.addWidget(self.formatRadio2)
        self.formatRadio3 = QtWidgets.QRadioButton(camCap)
        self.formatRadio3.setObjectName("formatRadio3")
        self.horizontalLayout_2.addWidget(self.formatRadio3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.statusLabel = QtWidgets.QLabel(camCap)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.startBtn = QtWidgets.QPushButton(camCap)
        self.startBtn.setEnabled(True)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_6.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(camCap)
        self.stopBtn.setEnabled(False)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_6.addWidget(self.stopBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exitBtn = QtWidgets.QPushButton(camCap)
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout.addWidget(self.exitBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(camCap)
        QtCore.QMetaObject.connectSlotsByName(camCap)

    def retranslateUi(self, camCap):
        _translate = QtCore.QCoreApplication.translate
        camCap.setWindowTitle(_translate("camCap", "Запись видео на камеру"))
        self.nameLabel.setText(_translate("camCap", "Имя записи"))
        self.nameL.setText(_translate("camCap", "year_month_day-hour_minute_second'.avi"))
        self.reportLabel.setText(_translate("camCap", "Параметры отчёта"))
        self.reportL1.setText(_translate("camCap", "Процент активных учеников"))
        self.reportL2.setText(_translate("camCap", "Процент отвлекшихся учеников "))
        self.reportL3.setText(_translate("camCap", "Процент всех эмоций"))
        self.dirLabel.setText(_translate("camCap", "Каталог сохранения записи  "))
        self.dirL.setText(_translate("camCap", "/output"))
        self.settBtn.setText(_translate("camCap", "Изменить параметры"))
        self.formatLabel.setText(_translate("camCap", "Формат вывода:"))
        self.formatRadio1.setText(_translate("camCap", "Только видео"))
        self.formatRadio2.setText(_translate("camCap", "Только отчет"))
        self.formatRadio3.setText(_translate("camCap", "Видео и отчет"))
        self.statusLabel.setText(_translate("camCap", "Запись не ведется"))
        self.startBtn.setText(_translate("camCap", "Начать запись"))
        self.stopBtn.setText(_translate("camCap", "Завершить запись"))
        self.exitBtn.setText(_translate("camCap", "Выход"))
