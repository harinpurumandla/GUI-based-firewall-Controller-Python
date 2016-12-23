from PyQt4 import QtCore, QtGui
import One,Two,Three,Four
import sys
import Windows
import Functions as iptable


def storeAnalysis():
    length, input, output = iptable.countRules()
    st = "\n\nNumber of Total Rules in the System: " + str(length) + "\n\n\n \tNumber of Input Rules: " + str(
        input) + "\n\n\n \tNumber of Output Rules: " + str(output)
    length, input, output = iptable.coutSetupRules()
    st = st + "\n\n\n\nNumber of Total Rules in the System installed by the application: " + str(
        length) + "\n\n\n \tNumber of Input Rules: " + str(input) + "\n\n\n \tNumber of Output Rules: " + str(
        output)
    return st
app = QtGui.QApplication(sys.argv)
Window1,ui1 = Windows.OpenOne()
Window2,ui2 = Windows.OpenTwo()
Window3,ui3 =Windows.OpenThree()
Window4,ui4 = Windows.OpenFour()

ui1.pushButton_2.clicked.connect(Window1.close)
ui1.pushButton_2.clicked.connect(Window2.show)
ui1.pushButton_3.clicked.connect(Window1.close)
ui1.pushButton_3.clicked.connect(Window3.show)
ui1.pushButton_3.clicked.connect(Window3.show)
ui1.pushButton_4.clicked.connect(Window1.close)
ui1.pushButton_4.clicked.connect(Window4.show)

ui2.pushButton.clicked.connect(Window2.close)
ui2.pushButton.clicked.connect(Window1.show)
ui2.pushButton_3.clicked.connect(Window2.close)
ui2.pushButton_3.clicked.connect(Window3.show)
ui2.pushButton_4.clicked.connect(Window2.close)
ui2.pushButton_4.clicked.connect(Window4.show)

ui3.pushButton.clicked.connect(Window3.close)
ui3.pushButton.clicked.connect(Window1.show)
ui3.pushButton_2.clicked.connect(Window3.close)
ui3.pushButton_2.clicked.connect(Window2.show)
ui3.pushButton_4.clicked.connect(Window3.close)
ui3.pushButton_4.clicked.connect(Window4.show)

ui4.pushButton.clicked.connect(Window4.close)
ui4.pushButton.clicked.connect(Window1.show)
ui4.pushButton_2.clicked.connect(Window4.close)
ui4.pushButton_2.clicked.connect(Window2.show)
ui4.pushButton_3.clicked.connect(Window4.close)
ui4.pushButton_3.clicked.connect(Window3.show)


if __name__ == '__main__':


    Window1.show()

    app.exec_()

