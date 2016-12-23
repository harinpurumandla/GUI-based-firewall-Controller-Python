# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Two.ui'
#
# Created: Tue Nov 29 17:58:15 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import Functions as iptable
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(750, 469)
        mainWindow.setAcceptDrops(False)
        mainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
""))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 171, 81))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 140, 171, 91))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 171, 91))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 320, 171, 91))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 410, 751, 61))
        self.frame.setStyleSheet(_fromUtf8("border-top-color: rgb(0, 0, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 751, 61))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 20, 85, 27))
        self.pushButton_5.setStyleSheet(_fromUtf8("color: rgb(13, 29, 221);\n"
"text-decoration: underline;"))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 400, 751, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.AddRemove = QtGui.QTabWidget(self.centralwidget)
        self.AddRemove.setGeometry(QtCore.QRect(170, 60, 581, 351))
        self.AddRemove.setObjectName(_fromUtf8("AddRemove"))
        self.Add = QtGui.QWidget()
        self.Add.setObjectName(_fromUtf8("Add"))
        self.frame_3 = QtGui.QFrame(self.Add)
        self.frame_3.setGeometry(QtCore.QRect(70, 110, 381, 61))
        self.frame_3.setStyleSheet(_fromUtf8("border-style: ridge;\n"
"border-width: 1px;\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.radioButton = QtGui.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(51, 21, 63, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(_fromUtf8("border-style: none;"))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(214, 21, 93, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(_fromUtf8("border-style: none;"))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_3 = QtGui.QLabel(self.Add)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 31, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame_4 = QtGui.QFrame(self.Add)
        self.frame_4.setGeometry(QtCore.QRect(70, 200, 381, 61))
        self.frame_4.setStyleSheet(_fromUtf8("border-style: ridge;\n"
"border-width: 1px;\n"
""))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.radioButton_3 = QtGui.QRadioButton(self.frame_4)
        self.radioButton_3.setGeometry(QtCore.QRect(21, 21, 42, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(_fromUtf8("border-style: none;"))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.frame_4)
        self.radioButton_4.setGeometry(QtCore.QRect(139, 21, 89, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet(_fromUtf8("border-style: none;"))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.frame_4)
        self.radioButton_5.setGeometry(QtCore.QRect(258, 21, 87, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet(_fromUtf8("border-style: none;"))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.label_4 = QtGui.QLabel(self.Add)
        self.label_4.setGeometry(QtCore.QRect(80, 190, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_6 = QtGui.QPushButton(self.Add)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 270, 101, 41))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.layoutWidget = QtGui.QWidget(self.Add)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 20, 381, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.AddRemove.addTab(self.Add, _fromUtf8(""))
        self.RemoveUpdate = QtGui.QWidget()
        self.RemoveUpdate.setObjectName(_fromUtf8("RemoveUpdate"))
        self.tableView = QtGui.QTableView(self.RemoveUpdate)
        self.tableView.setGeometry(QtCore.QRect(30, 30, 521, 201))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.model = QtGui.QStandardItemModel(None)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.model.setHorizontalHeaderLabels(['Name','Src','Direction','Action','Protocol'])
        self.tableView.setModel(self.model)

        def fillTable():
            listIn,rules = iptable.listSetupRules()
            for row in listIn:
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                    ]
                self.model.appendRow(items)
        fillTable()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.pushButton_7 = QtGui.QPushButton(self.RemoveUpdate)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 260, 101, 41))
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.RemoveUpdate)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 260, 101, 41))
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;"))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.hide()
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.AddRemove.addTab(self.RemoveUpdate, _fromUtf8(""))
        def showMessage(message):
            QtGui.QMessageBox.information(None, "Information", message, QMessageBox.Ok, QMessageBox.NoButton)
        def Onclick():
            website = self.lineEdit.text()
            website = str(website)
            ipaddress =iptable.getIpaddress(website)
            print ipaddress
            if self.radioButton.isChecked():
                if self.radioButton_4.isChecked():

                    if iptable.inserRule(True,ipaddress,"DROP","tcp",website):
                        if iptable.inserRule(True,ipaddress,"DROP","udp",website):
                            if iptable.inserRule(True,ipaddress,"DROP","icmp",website):
                                showMessage("Rule inserted Succesfully")
                    else:
                        showMessage("Rule insertion Failed/ Duplicate Entry Found.")
                elif self.radioButton_5.isChecked():

                    if iptable.inserRule(False, ipaddress, "DROP", "tcp", website):
                        if iptable.inserRule(False, ipaddress, "DROP", "udp", website):
                            if iptable.inserRule(False, ipaddress, "DROP", "icmp", website):
                                showMessage("Rule inserted Succesfully")
                    else:
                        showMessage("Rule insertion Failed/ Duplicate Entry Found.")
                elif self.radioButton_3.isChecked():
                    print ipaddress
                    if iptable.inserRule(False, ipaddress, "DROP", "tcp", website):
                        if iptable.inserRule(False, ipaddress, "DROP", "udp", website):
                            if iptable.inserRule(False, ipaddress, "DROP", "icmp", website):
                                if iptable.inserRule(True, ipaddress, "DROP", "tcp", website):
                                    if iptable.inserRule(True, ipaddress, "DROP", "udp", website):
                                        if iptable.inserRule(True, ipaddress, "DROP", "icmp", website):
                                            showMessage("Rule inserted Succesfully")
                    else:
                        showMessage("Rule insertion Failed/ Duplicate Entry Found.")

            elif self.radioButton_2.isChecked():
                if self.radioButton_4.isChecked():
                    if iptable.inserRule(True, ipaddress, "ACCEPT", "tcp", website):
                        if iptable.inserRule(True, ipaddress, "ACCEPT", "udp", website):
                            if iptable.inserRule(True, ipaddress, "ACCEPT", "icmp", website):
                                showMessage("Rule inserted Succesfully")
                    else:
                        showMessage("Rule insertion Failed/ Duplicate Entry Found.")
                elif self.radioButton_5.isChecked():
                    if iptable.inserRule(False, ipaddress, "ACCEPT", "tcp", website):
                        if iptable.inserRule(False, ipaddress, "ACCEPT", "udp", website):
                            if iptable.inserRule(False, ipaddress, "ACCEPT", "icmp", website):
                                showMessage("Rule inserted Succesfully")
                    else:
                        showMessage("Rule insertion Failed/ Duplicate Entry Found.")
                elif self.radioButton_3.isChecked():
                    if iptable.inserRule(False, ipaddress, "ACCEPT", "tcp", website):
                        if iptable.inserRule(False, ipaddress, "ACCEPT", "udp", website):
                            if iptable.inserRule(False, ipaddress, "ACCEPT", "icmp", website):
                                if iptable.inserRule(True, ipaddress, "ACCEPT", "tcp", website):
                                    if iptable.inserRule(True, ipaddress, "ACCEPT", "udp", website):
                                        if iptable.inserRule(True, ipaddress, "ACCEPT", "icmp", website):
                                            showMessage("Rule inserted Succesfully")
                    else:
                        showMessage("Rule insertion Failed/ Duplicate Entry Found.")
                iptable.findDuplicates()
            fillTable()
            self.lineEdit.setText("")
            self.radioButton.setChecked(True)
            self.radioButton_3.setChecked(True)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.AddRemove.setCurrentIndex(0)
        self.radioButton.setChecked(True)
        self.radioButton_3.setChecked(True)
        def Onclick1():
            indexes = self.tableView.selectionModel().selectedRows()
            listIn,rules = iptable.listSetupRules()
            for index in sorted(indexes):
                item =listIn[index.row()]
                if item[2] == 'INPUT':
                    iptable.removeRules(rules[index.row()],True)
                elif item[2] == 'OUTPUT':
                    iptable.removeRules(rules[index.row()],False)
                showMessage("Rule removed Succesfully")
            self.model1 = QtGui.QStandardItemModel(None)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.model1.setHorizontalHeaderLabels(['Name', 'Src', 'Direction', 'Action', 'Protocol'])
            self.tableView.setModel(self.model1)
            self.model = QtGui.QStandardItemModel(None)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.model.setHorizontalHeaderLabels(['Name', 'Src', 'Direction', 'Action', 'Protocol'])
            self.tableView.setModel(self.model)
            fillTable()
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), Onclick1)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), Onclick)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Firewall Controller", None))
        self.pushButton.setText(_translate("mainWindow", "System State", None))
        self.pushButton_2.setText(_translate("mainWindow", "Rules", None))
        self.pushButton_3.setText(_translate("mainWindow", "Analysis", None))
        self.pushButton_4.setText(_translate("mainWindow", "Tools/Quick Links", None))
        self.label.setText(_translate("mainWindow", "IP-TABLE FIREWALL CONTROLLER", None))
        self.pushButton_5.setText(_translate("mainWindow", "Manual", None))
        self.radioButton.setText(_translate("mainWindow", "DROP", None))
        self.radioButton_2.setText(_translate("mainWindow", "ACCEPT", None))
        self.label_3.setText(_translate("mainWindow", "Type", None))
        self.radioButton_3.setText(_translate("mainWindow", "All", None))
        self.radioButton_4.setText(_translate("mainWindow", "Incoming", None))
        self.radioButton_5.setText(_translate("mainWindow", "Outgoing", None))
        self.label_4.setText(_translate("mainWindow", "Direction", None))
        self.pushButton_6.setText(_translate("mainWindow", "ADD", None))
        self.label_2.setText(_translate("mainWindow", "Enter Website", None))
        self.AddRemove.setTabText(self.AddRemove.indexOf(self.Add), _translate("mainWindow", "Add Rule", None))
        self.pushButton_7.setText(_translate("mainWindow", "Remove", None))
        self.pushButton_8.setText(_translate("mainWindow", "Update", None))
        self.AddRemove.setTabText(self.AddRemove.indexOf(self.RemoveUpdate), _translate("mainWindow", "Remove/Update Rule", None))



