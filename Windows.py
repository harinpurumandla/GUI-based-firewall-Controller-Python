from PyQt4 import QtCore, QtGui
import One,Two,Three,Four
import sys

def OpenOne():
    mainWindow1 = QtGui.QMainWindow()
    ui1 = One.Ui_mainWindow()
    ui1.setupUi(mainWindow1)
    return mainWindow1,ui1
def OpenTwo():
    mainWindow2 = QtGui.QMainWindow()
    ui2 = Two.Ui_mainWindow()
    ui2.setupUi(mainWindow2)
    return mainWindow2,ui2
def OpenThree():
    mainWindow3 = QtGui.QMainWindow()
    ui2 = Three.Ui_mainWindow()
    ui2.setupUi(mainWindow3)
    return mainWindow3,ui2
def OpenFour():
    mainWindow4 = QtGui.QMainWindow()
    ui2 = Four.Ui_mainWindow()
    ui2.setupUi(mainWindow4)
    return mainWindow4,ui2


def CloseWindow(mainWindow):
    mainWindow.close()



