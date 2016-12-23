

from PyQt4 import QtCore, QtGui
import webbrowser
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
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 180, 211, 41))
        self.pushButton_7.setStyleSheet(_fromUtf8("color: rgb(13, 29, 221);\n"
"text-decoration: underline;"))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 130, 211, 41))
        self.pushButton_6.setStyleSheet(_fromUtf8("color: rgb(13, 29, 221);\n"
"text-decoration: underline;"))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 220, 211, 41))
        self.pushButton_8.setStyleSheet(_fromUtf8("color: rgb(13, 29, 221);\n"
"text-decoration: underline;"))
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        mainWindow.setCentralWidget(self.centralwidget)
        def openbrowMan():
            new = 2
            url = "http://ipset.netfilter.org/iptables.man.html"
            webbrowser.open(url, new=new)
        def openbrowVid2():
            new = 2
            url = "https://www.youtube.com/watch?v=XMvprnhP6wI"
            webbrowser.open(url, new=new)

        def openbrowVid1():
            new = 2
            url = "https: // www.youtube.com / watch?v = IVquJh3DXUA"
            webbrowser.open(url, new=new)
        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.clear)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), openbrowVid1)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), openbrowVid2)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), openbrowMan)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Firewall Controller", None))
        self.pushButton.setText(_translate("mainWindow", "System State", None))
        self.pushButton_2.setText(_translate("mainWindow", "Rules", None))
        self.pushButton_3.setText(_translate("mainWindow", "Analysis", None))
        self.pushButton_4.setText(_translate("mainWindow", "Tools/Quick Links", None))
        self.label.setText(_translate("mainWindow", "IP-TABLE FIREWALL CONTROLLER", None))
        self.pushButton_5.setText(_translate("mainWindow", "Manual", None))
        self.pushButton_7.setText(_translate("mainWindow", "IPtables Basics", None))
        self.pushButton_6.setText(_translate("mainWindow", "Basic Linux Commands video", None))
        self.pushButton_8.setText(_translate("mainWindow", "Manual for IPtables", None))
