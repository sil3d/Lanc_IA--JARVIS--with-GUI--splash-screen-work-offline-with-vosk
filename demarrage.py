# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demarrage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lanc(object):
    def setupUi(self, Lanc):
        Lanc.setObjectName("Lanc")
        Lanc.resize(801, 440)
        self.Demarrage_Lanc = QtWidgets.QFrame(Lanc)
        self.Demarrage_Lanc.setGeometry(QtCore.QRect(120, 40, 651, 351))
        self.Demarrage_Lanc.setStyleSheet("QFrame {    \n"
"    \n"
"    background-color: rgb(15, 15, 15);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 35px;\n"
"}")
        self.Demarrage_Lanc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Demarrage_Lanc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Demarrage_Lanc.setObjectName("Demarrage_Lanc")
        self.label = QtWidgets.QLabel(self.Demarrage_Lanc)
        self.label.setGeometry(QtCore.QRect(20, 80, 631, 311))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/bg1.png"))
        self.label.setObjectName("label")
        self.version = QtWidgets.QLabel(self.Demarrage_Lanc)
        self.version.setGeometry(QtCore.QRect(430, 310, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version.setObjectName("version")
        self.chargement = QtWidgets.QLabel(self.Demarrage_Lanc)
        self.chargement.setGeometry(QtCore.QRect(40, 320, 321, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.chargement.setFont(font)
        self.chargement.setStyleSheet("color:#fff;\n"
"background-color: transparent;\n"
"")
        self.chargement.setAlignment(QtCore.Qt.AlignCenter)
        self.chargement.setObjectName("chargement")
        self.progressBar = QtWidgets.QProgressBar(self.Demarrage_Lanc)
        self.progressBar.setGeometry(QtCore.QRect(400, 10, 231, 21))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(117, 117, 117);\n"
"    color: rgb(217, 217, 217);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.977273 rgba(46, 0, 148, 255), stop:1 rgba(49, 148, 0, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.Demarrage_Lanc)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.description = QtWidgets.QLabel(self.Demarrage_Lanc)
        self.description.setGeometry(QtCore.QRect(256, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.description.setFont(font)
        self.description.setStyleSheet("")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")

        self.retranslateUi(Lanc)
        QtCore.QMetaObject.connectSlotsByName(Lanc)

    def retranslateUi(self, Lanc):
        _translate = QtCore.QCoreApplication.translate
        Lanc.setWindowTitle(_translate("Lanc", "Form"))
        self.version.setText(_translate("Lanc", "Lanc version--1.0"))
        self.chargement.setText(_translate("Lanc", "Chargement..."))
        self.label_2.setText(_translate("Lanc", "LANC"))
        self.description.setText(_translate("Lanc", "chargement du mod??le"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lanc = QtWidgets.QWidget()
    ui = Ui_Lanc()
    ui.setupUi(Lanc)
    Lanc.show()
    sys.exit(app.exec_())
