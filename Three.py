
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
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
        def storeAnalysis():
            length, input, output = iptable.countRules()
            st = "\n\nNumber of Total Rules in the System: " + str(length) + "\n\n\n \tNumber of Input Rules: " + str(
                input) + "\n\n\n \tNumber of Output Rules: " + str(output)
            length, input, output = iptable.coutSetupRules()
            st = st + "\n\n\n\nNumber of Total Rules in the System installed by the application: " + str(
                length) + "\n\n\n \tNumber of Input Rules: " + str(input) + "\n\n\n \tNumber of Output Rules: " + str(
                output)
            return st
        st = storeAnalysis()
        def updatePractices():
            string = "\n\nIndustries Best Practices used \n\n\t -> No Duplicate Rules \n\n\t ->No rule clashing With other Rules\n\n\t ->State Selection according to the Operation Performed."
            return string
        string = updatePractices()
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
        self.AddRemove.setGeometry(QtCore.QRect(160, 50, 581, 351))
        self.AddRemove.setObjectName(_fromUtf8("AddRemove"))
        self.Analysis = QtGui.QWidget()
        self.Analysis.setObjectName(_fromUtf8("Analysis"))
        self.textEdit = QtGui.QTextEdit(self.Analysis)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 571, 391))
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_8 = QtGui.QPushButton(self.Analysis)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 280, 101, 31))
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
                                                  "font-weight: bold;"))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.AddRemove.addTab(self.Analysis, _fromUtf8(""))
        self.defaultrules = QtGui.QWidget()
        self.defaultrules.setObjectName(_fromUtf8("defaultrules"))
        self.tableView = QtGui.QTableView(self.defaultrules)
        self.tableView.setGeometry(QtCore.QRect(30, 30, 521, 251))
        self.tableView.setFrameShadow(QtGui.QFrame.Plain)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.model = QtGui.QStandardItemModel(None)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.model.setHorizontalHeaderLabels(['Src', 'Direction', 'Action', 'Protocol'])
        self.tableView.setModel(self.model)

        def fillTable():
            listIn, rules = iptable.listRules()
            for row in listIn:
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                    ]
                self.model.appendRow(items)

        fillTable()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.AddRemove.addTab(self.defaultrules, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 10, 571, 391))
        self.textEdit_2.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_2.setText(string)
        self.AddRemove.addTab(self.tab, _fromUtf8(""))
        mainWindow.setCentralWidget(self.centralwidget)
        self.textEdit.setText(st)
        self.retranslateUi(mainWindow)
        self.AddRemove.setCurrentIndex(0)
        def refresh():
            st = storeAnalysis()
            self.textEdit.setText(st)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.clear)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), refresh)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Firewall Controller", None))
        self.pushButton.setText(_translate("mainWindow", "System State", None))
        self.pushButton_2.setText(_translate("mainWindow", "Rules", None))
        self.pushButton_3.setText(_translate("mainWindow", "Analysis", None))
        self.pushButton_4.setText(_translate("mainWindow", "Tools/Quick Links", None))
        self.label.setText(_translate("mainWindow", "IP-TABLE FIREWALL CONTROLLER", None))
        self.pushButton_5.setText(_translate("mainWindow", "Manual", None))
        self.AddRemove.setTabText(self.AddRemove.indexOf(self.Analysis), _translate("mainWindow", "Analysis", None))
        self.AddRemove.setTabText(self.AddRemove.indexOf(self.defaultrules), _translate("mainWindow", "System Default Rules", None))
        self.AddRemove.setTabText(self.AddRemove.indexOf(self.tab), _translate("mainWindow", "Best Practices", None))
        self.pushButton_8.setText(_translate("mainWindow", "Refresh", None))
