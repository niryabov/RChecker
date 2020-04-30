# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 319)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(346, 319))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget{\n"
                                 "\n"
                                 "background-color: white\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "#start{background-color:#DC546B;\n"
                                 "border-radius: 5px;\n"
                                 "color: white;\n"
                                 "\n"
                                 "}\n"
                                 "#column:focus{\n"
                                 "border-bottom:1px solid #3471FF;}\n"
                                 "QLineEdit{\n"
                                 "border-bottom:1px solid #6E757F;\n"
                                 "padding-left: 5px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "#start:hover{\n"
                                 "background-color: #232A46}\n"
                                 "\n"
                                 "#file {\n"
                                 "border: 2px solid #232A46;\n"
                                 "border-radius: 5px;\n"
                                 "\n"
                                 "color: #232A46;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "#file:hover{\n"
                                 "border: 2px solid #232A46;\n"
                                 "background-color:#232A46;\n"
                                 "color:white}\n"
                                 "\n"
                                 "QLineEdit:focus{\n"
                                 "border: 1px solid #232A46;\n"
                                 "border-radius:8px}\n"
                                 "#column{\n"
                                 "border: None;\n"
                                 "border-radius:0px;\n"
                                 "padding-bottom: 0px;\n"
                                 "border-bottom:1px solid #6E757F;}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(30, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login.setToolTipDuration(-2)
        self.login.setWhatsThis("")
        self.login.setAutoFillBackground(False)
        self.login.setStyleSheet("")
        self.login.setText("")
        self.login.setFrame(False)
        self.login.setObjectName("login")
        self.psw = QtWidgets.QLineEdit(self.centralwidget)
        self.psw.setGeometry(QtCore.QRect(30, 150, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.psw.setFont(font)
        self.psw.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.psw.setToolTipDuration(0)
        self.psw.setAutoFillBackground(False)
        self.psw.setStyleSheet("")
        self.psw.setText("")
        self.psw.setFrame(False)
        self.psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psw.setObjectName("psw")
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(20, 250, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file.setFont(font)
        self.file.setObjectName("file")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(170, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 360, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#232A46")
        self.label.setObjectName("label")
        self.label_ready = QtWidgets.QLabel(self.centralwidget)
        self.label_ready.setGeometry(QtCore.QRect(70, 110, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(50)
        self.label_ready.setFont(font)
        self.label_ready.setStyleSheet("color:#3471FF;\n"
                                       "background-color: None")
        self.label_ready.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 60, 401, 20))
        self.line.setStyleSheet("color: #6E757F")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.column = QtWidgets.QLineEdit(self.centralwidget)
        self.column.setGeometry(QtCore.QRect(140, 210, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.column.setFont(font)
        self.column.setFrame(False)
        self.column.setObjectName("column")
        self.label_column = QtWidgets.QLabel(self.centralwidget)
        self.label_column.setGeometry(QtCore.QRect(30, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.label_column.setFont(font)
        self.label_column.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RChecker"))
        self.file.setText(_translate("MainWindow", "Выбрать файл"))
        self.start.setText(_translate("MainWindow", "Начать проверку"))
        self.label.setText(_translate("MainWindow", "RChecker"))
        self.label_ready.setText(_translate("MainWindow", "Готово"))
        self.column.setText(_translate("MainWindow", "6"))
        self.label_column.setText(_translate("MainWindow", "Номер столбца"))
