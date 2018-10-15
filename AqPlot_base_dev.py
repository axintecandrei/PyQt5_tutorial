import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pandas as pd
'''
    Using this comand a .ui file shall be converted to .py file
    path_of_pyuic tool : "C:\_Users\axint\AppData\Local\Programs\Python\Python36\Scripts>pyuic5.exe" 
                          C:\_Users\axint\AppData\Roaming\Python\Python36\Scripts
    
    command = pyuic5.exe -x file_to_Be_converted.ui -o result_of_convertion.py
'''

class Model():
    def __init__(self):
        self.number_of_signals = int()
        self.signal_names = []



    def import_signals(self, file_name):

        with open(file_name, newline='') as f:
            if f != "":
                self.meas_data = pd.read_csv(f, low_memory=False)

        self.signal_names = self.meas_data.keys()
        self.number_of_signals = len(self.signal_names)



		
		
'''
    This class shall represent the View:
        - all gui related objects
        - 
'''


class View(object):

    def __init__(self, MainWindow):

        self.main_window = MainWindow
        self.main_frame_init()
        self.create_graph_view()
        self.create_open_meas_butt()
        self.create_clr_scr_butt()
        self.create_signal_list()
        '''
            The show() method shall be called ALWAYS after 
            the backyard is done and ready. 
        '''
        self.main_window.show()

    def main_frame_init(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(1130, 539)

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.central_gridLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_gridLayout.setObjectName("central_gridLayout")

        '''buttons frame'''
        self.butt_frame = QtWidgets.QFrame(self.centralwidget)
        self.butt_frame.setMinimumSize(QtCore.QSize(231, 521))
        self.butt_frame.setMaximumSize(QtCore.QSize(231, 521))
        self.butt_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.butt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.butt_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.butt_frame.setObjectName("butt_frame")

        self.central_gridLayout.addWidget(self.butt_frame)
        self.main_window.setCentralWidget(self.centralwidget)


        self._translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(self._translate("MainWindow", "MainWindow"))


        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def create_graph_view(self):
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(641, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.central_gridLayout.addWidget(self.graphicsView)

    def create_open_meas_butt(self):
        self.open_meas_butt = QtWidgets.QPushButton(self.butt_frame)
        self.open_meas_butt.setGeometry(QtCore.QRect(11, 11, 161, 31))
        self.open_meas_butt.setMinimumSize(QtCore.QSize(161, 31))
        self.open_meas_butt.setMaximumSize(QtCore.QSize(161, 31))
        self.open_meas_butt.setObjectName("open_meas_butt")
        self.open_meas_butt.raise_()
        self.open_meas_butt.setText(self._translate("MainWindow", "Open Measurement"))

    def create_clr_scr_butt(self):
        self.clr_scr = QtWidgets.QPushButton(self.butt_frame)
        self.clr_scr.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.clr_scr.setMinimumSize(QtCore.QSize(161, 31))
        self.clr_scr.setMaximumSize(QtCore.QSize(161, 31))
        self.clr_scr.setObjectName("clr_scr")
        self.clr_scr.raise_()
        self.clr_scr.setText(self._translate("MainWindow", "Clear Screen"))

    def create_menu_bar(self):
        self.mainMenu = self.menuBar()

        self.fileMenu = self.mainMenu.addMenu('&File')


        self.openFileAction_menubar = QtWidgets.QAction("&Open...", self)
        self.openFileAction_menubar.setShortcut("Ctrl+O")
        self.openFileAction_menubar.setStatusTip('Open a txt file')
        self.fileMenu.addAction(self.openFileAction_menubar)


        self.exitAction_menubar = QtWidgets.QAction("&Exit", self)
        self.exitAction_menubar.setShortcut("Ctrl+Q")
        self.exitAction_menubar.setStatusTip('Leave the app from menu bar')
        self.fileMenu.addAction(self.exitAction_menubar)

    def create_tool_bar(self):
        self.toolBar = self.addToolBar("Another Exit")
        self.extractAction_toolbar = QtWidgets.QAction(QtGui.QIcon("exit.png"),"&Another Exit point", self)
        self.toolBar.addAction(self.extractAction_toolbar)
        self.extractAction_toolbar.setStatusTip('Leave the app toolbar')

    def create_check_box(self):
        self.check_box = QtWidgets.QCheckBox("Check this to enlarge window",self)
        self.check_box.setGeometry(100,25,250,40)
        #self.check_box.move(100,25)
        #self.check_box.toggle()
        self.check_box.stateChanged.connect(self.enlarge_window)

    def create_progres_bar(self):
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(250,55,250,20)

    def create_combo_box(self):
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItems(QtWidgets.QStyleFactory.keys())
        self.comboBox.move(0,115)
        self.comboBox.activated[str].connect(self.choise_style)

    def create_signal_list(self):
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
        self.signal_list_box.setObjectName("listWidget")

        self.signals_box_label.setText(self._translate("MainWindow", "Signals"))
        self.signals_box_label.raise_()

    def fill_up_signal_list(self, signal_name):
        for signal in signal_name[1:]:
            self.signal_list_box.addItem(signal)



    def pop_up_on_exit(self):
        areYouSure = QtWidgets.QMessageBox.question(self, 'Exit', "Get Out?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        return areYouSure

    def open_file_dialog(self):
        file_name, value = QtWidgets.QFileDialog.getOpenFileName(self.main_window, 'Choise a file')
        return file_name


class Controller():
    def __init__(self):
        self.app = QtWidgets.QApplication([])

        self.model = Model()

        self.view = View(QtWidgets.QMainWindow())
        self.view.open_meas_butt.clicked.connect(self.open_and_load_file)
        self.view.clr_scr.clicked.connect(self.clear_graph)
        self.view.signal_list_box.itemSelectionChanged.connect(self.add_signal_to_plot)
        '''
        self.gui.quit_btn.clicked.connect(self.clbk_quit)
        self.gui.exitAction_menubar.triggered.connect(self.clbk_quit)
        self.gui.extractAction_toolbar.triggered.connect(self.clbk_quit)
        self.gui.openFileAction_menubar.triggered.connect(self.open_and_load_file)
        '''
    def run(self):
        self.app.exec()

    def open_and_load_file(self):
        file_name = self.view.open_file_dialog()
        self.model.import_signals(file_name)
        self.view.fill_up_signal_list(self.model.signal_names)
        self.aq_plot(self.model.meas_data[self.model.signal_names[2]])


    def aq_plot(self, data):
        self.view.graphicsView.plot(data, pen='g')

    def add_signal_to_plot(self):
        selected_signal = self.view.signal_list_box.currentItem().text()
        self.aq_plot(self.model.meas_data[selected_signal])

    def clear_graph(self):
        self.view.graphicsView.clear()
    def clbk_quit(self):
        get_user_ans = self.view.pop_up_on_exit()
        time_till_exit = 0
        if get_user_ans == QtWidgets.QMessageBox.Yes:
            while time_till_exit <= 100:
                time_till_exit +=0.0001
                self.view.progress.setValue(time_till_exit)

            sys.exit()
        else :
            pass
C = Controller()


if __name__ == '__main__':
    C.run()
