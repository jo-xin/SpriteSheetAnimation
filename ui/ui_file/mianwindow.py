# Form implementation generated from reading ui file 'mianwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 401)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_sheet = QtWidgets.QLabel(parent=self.tab)
        self.label_sheet.setGeometry(QtCore.QRect(30, 20, 256, 256))
        self.label_sheet.setStyleSheet("border: 2px dashed navy;")
        self.label_sheet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sheet.setObjectName("label_sheet")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setGeometry(QtCore.QRect(300, 110, 261, 51))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label.setObjectName("label")
        self.lineEdit_frameW = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_frameW.setGeometry(QtCore.QRect(60, 20, 51, 20))
        self.lineEdit_frameW.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_frameW.setObjectName("lineEdit_frameW")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 41, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_frameH = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_frameH.setGeometry(QtCore.QRect(190, 20, 51, 20))
        self.lineEdit_frameH.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_frameH.setObjectName("lineEdit_frameH")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 50, 261, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_columns = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_columns.setGeometry(QtCore.QRect(60, 20, 51, 20))
        self.lineEdit_columns.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_columns.setObjectName("lineEdit_columns")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(140, 20, 41, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_rows = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_rows.setGeometry(QtCore.QRect(190, 20, 51, 20))
        self.lineEdit_rows.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_rows.setObjectName("lineEdit_rows")
        self.check_rowMajor = QtWidgets.QCheckBox(parent=self.tab)
        self.check_rowMajor.setGeometry(QtCore.QRect(300, 230, 131, 16))
        self.check_rowMajor.setChecked(True)
        self.check_rowMajor.setObjectName("check_rowMajor")
        self.pushButton_guess = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_guess.setGeometry(QtCore.QRect(300, 20, 31, 23))
        self.pushButton_guess.setStyleSheet("")
        self.pushButton_guess.setText("")
        self.pushButton_guess.setObjectName("pushButton_guess")
        self.label_7 = QtWidgets.QLabel(parent=self.tab)
        self.label_7.setGeometry(QtCore.QRect(340, 20, 221, 20))
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 170, 261, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_stopColumn = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEdit_stopColumn.setGeometry(QtCore.QRect(60, 20, 51, 20))
        self.lineEdit_stopColumn.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_stopColumn.setObjectName("lineEdit_stopColumn")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(140, 20, 41, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_stopRow = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEdit_stopRow.setGeometry(QtCore.QRect(190, 20, 51, 20))
        self.lineEdit_stopRow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_stopRow.setObjectName("lineEdit_stopRow")
        self.label_sheetInfo = QtWidgets.QLabel(parent=self.tab)
        self.label_sheetInfo.setGeometry(QtCore.QRect(50, 280, 221, 20))
        self.label_sheetInfo.setText("")
        self.label_sheetInfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sheetInfo.setObjectName("label_sheetInfo")
        self.pushButton_split = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_split.setGeometry(QtCore.QRect(300, 260, 261, 23))
        self.pushButton_split.setObjectName("pushButton_split")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_animation = QtWidgets.QLabel(parent=self.tab_3)
        self.label_animation.setGeometry(QtCore.QRect(20, 20, 281, 281))
        self.label_animation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_animation.setObjectName("label_animation")
        self.pushButton_play = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_play.setGeometry(QtCore.QRect(350, 130, 31, 31))
        self.pushButton_play.setText("")
        self.pushButton_play.setObjectName("pushButton_play")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(300, 40, 261, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_duration = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_duration.setGeometry(QtCore.QRect(170, 40, 71, 20))
        self.lineEdit_duration.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_duration.setObjectName("lineEdit_duration")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(150, 20, 111, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_frequency = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_frequency.setGeometry(QtCore.QRect(30, 40, 71, 20))
        self.lineEdit_frequency.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit_frequency.setObjectName("lineEdit_frequency")
        self.check_repeat = QtWidgets.QCheckBox(parent=self.tab_3)
        self.check_repeat.setGeometry(QtCore.QRect(480, 130, 51, 31))
        self.check_repeat.setText("")
        self.check_repeat.setObjectName("check_repeat")
        self.pushButton_stop = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_stop.setGeometry(QtCore.QRect(410, 130, 31, 31))
        self.pushButton_stop.setText("")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_gif = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_gif.setGeometry(QtCore.QRect(340, 240, 191, 23))
        self.pushButton_gif.setObjectName("pushButton_gif")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpriteSheetAnimation"))
        self.label_sheet.setText(_translate("MainWindow", "Drag And Drop Sprite Sheet Here"))
        self.groupBox.setTitle(_translate("MainWindow", "Each Frame"))
        self.label.setText(_translate("MainWindow", "Width:"))
        self.label_2.setText(_translate("MainWindow", "Height:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "In the sheet, there are"))
        self.label_5.setText(_translate("MainWindow", "Columns:"))
        self.label_6.setText(_translate("MainWindow", "Rows:"))
        self.check_rowMajor.setText(_translate("MainWindow", "Row Major Order"))
        self.label_7.setText(_translate("MainWindow", "try splitting into square frames"))
        self.groupBox_3.setTitle(_translate("MainWindow", "The Last Frame at"))
        self.label_8.setText(_translate("MainWindow", "Column:"))
        self.label_9.setText(_translate("MainWindow", "Row:"))
        self.pushButton_split.setText(_translate("MainWindow", "Split!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SpriteSheet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Frames"))
        self.label_animation.setText(_translate("MainWindow", "Animation will be shown here"))
        self.groupBox_4.setTitle(_translate("MainWindow", "frequency"))
        self.label_4.setText(_translate("MainWindow", "frames per second"))
        self.label_10.setText(_translate("MainWindow", "duration per frame"))
        self.pushButton_gif.setText(_translate("MainWindow", "save as gif"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Animation"))
