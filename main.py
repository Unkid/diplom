import sys 
import os
import configparser

from PyQt5 import QtWidgets, QtCore

import mw
import settings
import cam
import easy
import test
import time 

class OpenCap(QtWidgets.QMainWindow, test.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.setupUi(self)
        self.label_2.setText(self.config.get("Settings", "brightness"))
        self.label.setText(self.config.get("Settings", "contrast"))
        self.saveSett.setEnabled(False)
        self.brightSlider.setValue(int(self.config.get("Settings", "brightness")))
        self.contrSlider.setValue(float(self.config.get("Settings", "contrast"))*10)
        self.brightSlider.sliderMoved.connect(self.brightMoved)
        self.contrSlider.sliderMoved.connect(self.contrMoved)
        self.brightSlider.valueChanged.connect(self.changed)
        self.contrSlider.valueChanged.connect(self.changed)
        self.saveSett.clicked.connect(self.settSave)
        self.startBtn.clicked.connect(self.openCam)
        self.stopBtn.clicked.connect(self.stopUpdate)
        self.exitBtn.clicked.connect(self.ext)
        self.stop = False
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    
    def brightMoved(self):
        self.label_2.setText(str(self.brightSlider.value()))

    def contrMoved(self):
        self.label.setText(str(self.contrSlider.value()/10))

    def changed(self):
        self.saveSett.setEnabled(True)
    
    def stopUpdate(self):
        self.stop = True
        self.stopBtn.setEnabled(False)
        self.startBtn.setEnabled(True)

    def settSave(self):
        self.config.set("Settings", "brightness", str(self.brightSlider.value()))
        self.config.set("Settings", "contrast", str(self.contrSlider.value()/10))
        with open('settings.ini', "w") as config_file:
            self.config.write(config_file)
        self.stop = True
        self.startBtn.setEnabled(True)
        print("save")

    def openCam(self):
        self.stop = False
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)
        face_det = easy.FaceDet()
        opn = face_det.opnVideo('videos/light_test.mp4')
        while True:
            reply = face_det.startCapture('output/light_brighter',self.stop)
            if (reply == 'killed'):
                break
            if (reply =='done'):
                break
    def ext(self):
        self.saveSett.setEnabled(True)
        self.stopBtn.setEnabled(False)
        self.stop = True
        self.close()
            
class CameraCap(QtWidgets.QWidget, cam.Ui_camCap):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.nameL.setText(self.config.get("Settings", "name"))
        self.dirL.setText(self.config.get("Settings", "outpath"))
        self.statusLabel.setText('Запись не ведется')
        self.settBtn.clicked.connect(self.changeSett)
        self.startBtn.clicked.connect(self.openCam)
        self.stopBtn.clicked.connect(self.stopUpdate)
        self.exitBtn.clicked.connect(self.ext)
        self.stopBtn.setEnabled(False)
        self.stop = False
        self.setS = SetSettings()
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def stopUpdate(self):
        self.stop = True
        self.stopBtn.setEnabled(False)
        self.startBtn.setEnabled(True)

    def changeSett(self):
        self.setS.show()
        self.close()

    def ext(self):
        self.statusLabel.setText('Запись не ведется')
        self.stop = True
        self.close()

    def openCam(self):
        self.stop = False
        self.stopBtn.setEnabled(True)
        self.startBtn.setEnabled(False)
        face_det = easy.FaceDet()
        opn = face_det.opnVideo('0')
        name = str(time.strftime("%Y_%m_%d-%H_%M_%S"))
        path = os.path.join(self.config.get("Settings", "outpath"), name)
        print(path)
        while True:
            self.statusLabel.setText('Ведется запись')
            reply = face_det.startCapture(path,self.stop)
            if (reply == 'killed'):
                self.statusLabel.setText('Обработка завершена неудачно')
                break
            if (reply =='done'):
                self.statusLabel.setText('Обработка завершена успешно')
                break
        if not(os.path.isfile(path+'.'+self.config.get("Settings", "format"))):
                self.statusLabel.setText('Файл не был сохренен, проверьте существование папки сохранения')


class SetSettings(QtWidgets.QWidget, settings.Ui_setSettings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.dirEdit.setText(self.config.get("Settings", "outpath"))
        self.exitBtn.clicked.connect(self.close)
        self.dirBtn.clicked.connect(self.selDir)
        self.saveBtn.clicked.connect(self.save)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def save(self):
        self.config.set("Settings", "outpath", self.dirEdit.text()+'/')
        with open('settings.ini', "w") as config_file:
            self.config.write(config_file)

    def selDir(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.dirEdit.setText(directory)

class MainWindow(QtWidgets.QMainWindow, mw.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnExit.clicked.connect(sys.exit)
        self.opnV = CameraCap()
        self.camC = OpenCap()
        self.setS = SetSettings()
        self.opnVid.clicked.connect(self.openVid)
        self.crtVid.clicked.connect(self.createVid)
        self.setPar.clicked.connect(self.setSet)

    def openVid(self):
        self.opnV.show()

    def createVid(self):
        self.camC.show()

    def setSet(self):
        self.setS.show()


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = MainWindow() 
    window.show()  
    app.exec_()  

if __name__ == '__main__':
    main()