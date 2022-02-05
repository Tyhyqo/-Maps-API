# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 590)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 590))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 590))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map_lablel = QtWidgets.QLabel(self.centralwidget)
        self.map_lablel.setGeometry(QtCore.QRect(340, 90, 640, 450))
        self.map_lablel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map_lablel.setText("")
        self.map_lablel.setPixmap(QtGui.QPixmap("../Space-Nomads_/data/planet_bg.png"))
        self.map_lablel.setObjectName("map_lablel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-131, -20, 421, 821))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.search_button = QtWidgets.QPushButton(self.frame)
        self.search_button.setGeometry(QtCore.QRect(380, 30, 30, 30))
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(20, 20))
        self.search_button.setObjectName("search_button")
        self.searching_line = QtWidgets.QLineEdit(self.frame)
        self.searching_line.setGeometry(QtCore.QRect(165, 30, 215, 30))
        self.searching_line.setText("")
        self.searching_line.setObjectName("searching_line")
        self.reset = QtWidgets.QPushButton(self.frame)
        self.reset.setGeometry(QtCore.QRect(135, 30, 30, 30))
        self.reset.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("location.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset.setIcon(icon1)
        self.reset.setIconSize(QtCore.QSize(20, 20))
        self.reset.setObjectName("reset")
        self.result_search = QtWidgets.QLabel(self.frame)
        self.result_search.setGeometry(QtCore.QRect(140, 80, 261, 121))
        self.result_search.setText("")
        self.result_search.setObjectName("result_search")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 280, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.on_indexing = QtWidgets.QRadioButton(self.frame)
        self.on_indexing.setGeometry(QtCore.QRect(200, 320, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.on_indexing.setFont(font)
        self.on_indexing.setObjectName("on_indexing")
        self.off_indexing = QtWidgets.QRadioButton(self.frame)
        self.off_indexing.setGeometry(QtCore.QRect(200, 360, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.off_indexing.setFont(font)
        self.off_indexing.setObjectName("off_indexing")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(690, -70, 341, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 301, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.map_radio = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.map_radio.setFont(font)
        self.map_radio.setChecked(True)
        self.map_radio.setObjectName("map_radio")
        self.horizontalLayout.addWidget(self.map_radio)
        self.sat_radio = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sat_radio.setFont(font)
        self.sat_radio.setObjectName("sat_radio")
        self.horizontalLayout.addWidget(self.sat_radio)
        self.skl_radio = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.skl_radio.setFont(font)
        self.skl_radio.setObjectName("skl_radio")
        self.horizontalLayout.addWidget(self.skl_radio)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAPS API"))
        self.searching_line.setPlaceholderText(_translate("MainWindow", "Поиск мест и адресов"))
        self.label.setText(_translate("MainWindow", "Почтовый индекс:"))
        self.on_indexing.setText(_translate("MainWindow", "Вкл"))
        self.off_indexing.setText(_translate("MainWindow", "Выкл"))
        self.map_radio.setText(_translate("MainWindow", "Схема"))
        self.sat_radio.setText(_translate("MainWindow", "Спутник"))
        self.skl_radio.setText(_translate("MainWindow", "Гибрид"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
