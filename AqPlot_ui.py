# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\.github.com\PyQt5_tutorial\AqPlot.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_gridLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_gridLayout.setObjectName("central_gridLayout")

        self.butt_frame = QtWidgets.QFrame(self.centralwidget)
        self.butt_frame.setMinimumSize(QtCore.QSize(231, 521))
        self.butt_frame.setMaximumSize(QtCore.QSize(231, 521))
        self.butt_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.butt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.butt_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.butt_frame.setObjectName("butt_frame")

        self.open_meas_butt = QtWidgets.QPushButton(self.butt_frame)
        self.open_meas_butt.setGeometry(QtCore.QRect(11, 11, 161, 31))
        self.open_meas_butt.setMinimumSize(QtCore.QSize(161, 31))
        self.open_meas_butt.setMaximumSize(QtCore.QSize(161, 31))
        self.open_meas_butt.setObjectName("open_meas_butt")

        self.clr_scr = QtWidgets.QPushButton(self.butt_frame)
        self.clr_scr.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.clr_scr.setMinimumSize(QtCore.QSize(161, 31))
        self.clr_scr.setMaximumSize(QtCore.QSize(161, 31))
        self.clr_scr.setObjectName("clr_scr")

        self.signals_box_label = QtWidgets.QLabel(self.butt_frame)
        self.signals_box_label.setGeometry(QtCore.QRect(11, 85, 60, 29))
        self.signals_box_label.setMinimumSize(QtCore.QSize(60, 29))
        self.signals_box_label.setMaximumSize(QtCore.QSize(60, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signals_box_label.setFont(font)
        self.signals_box_label.setTextFormat(QtCore.Qt.AutoText)
        self.signals_box_label.setScaledContents(True)
        self.signals_box_label.setWordWrap(False)
        self.signals_box_label.setObjectName("signals_box_label")
        self.signal_list_box = QtWidgets.QListWidget(self.butt_frame)
        self.signal_list_box.setGeometry(QtCore.QRect(10, 120, 201, 281))
        self.signal_list_box.setObjectName("signal_list_box")
        self.signals_box_label.raise_()
        self.signal_list_box.raise_()
        self.open_meas_butt.raise_()
        self.clr_scr.raise_()

        self.central_gridLayout.addWidget(self.butt_frame)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(641, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.central_gridLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.open_meas_butt.clicked.connect(self.open_file_dialog)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_meas_butt.setText(_translate("MainWindow", "Open Measurement"))
        self.clr_scr.setText(_translate("MainWindow", "Clear Screen"))
        self.signals_box_label.setText(_translate("MainWindow", "Signals"))

    def open_file_dialog(self):
        file_name, value = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Choise a file')
        return file_name

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

