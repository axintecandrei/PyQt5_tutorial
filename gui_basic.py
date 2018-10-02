import sys
from PyQt5 import QtCore, QtGui, QtWidgets


'''
    This class shall represent the View:
        - all gui related objects
        - 
'''
class Model():
    def __init__(self):
        pass



class View(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_frame_init()

        self.create_quit_butt()
        self.create_menu_bar()
        self.create_tool_bar()
        self.create_check_box()
        self.create_progres_bar()
        #self.create_combo_box()
        self.statusBar()

        '''
            The show() method shall be called ALWAYS after 
            the backyard is done and ready. 
        '''
        self.show()

    def main_frame_init(self):
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("GUI with PyQt5 Tutorial")
        self.setWindowIcon(QtGui.QIcon("app_icon.png"))
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        self.currentStyle = QtWidgets.QLabel("Style: " + self.style().objectName(),self)
        self.currentStyle.move(0,90)

    def create_quit_butt(self):
        self.quit_btn = QtWidgets.QPushButton("Fuck Off", self)
        self.quit_btn.resize(self.quit_btn.sizeHint())
        self.quit_btn.move(0, 55)
        '''
        Show a sort of message into the statusbar when mouse hover butt
        '''
        self.quit_btn.setStatusTip('Leave the app from Button')

    def create_menu_bar(self):
        self.mainMenu = self.menuBar()
        self.fileMenu = self.mainMenu.addMenu('&File')


        self.extractAction_menubar = QtWidgets.QAction("&Exit", self)
        self.extractAction_menubar.setShortcut("Ctrl+Q")
        self.extractAction_menubar.setStatusTip('Leave the app from menu bar')

        self.fileMenu.addAction(self.extractAction_menubar)

    def create_tool_bar(self):
        self.toolBar = self.addToolBar("Another Exit")
        self.extractAction_toolbar = QtWidgets.QAction(QtGui.QIcon("exit.png"),"&Another Exit point", self)
        self.toolBar.addAction(self.extractAction_toolbar)
        self.extractAction_toolbar.setStatusTip('Leave the app toolbar')

    def create_check_box(self):
        self.check_box = QtWidgets.QCheckBox("Check this to enlarge window",self)
        self.check_box.move(100,25)
        self.check_box.toggle()
        self.check_box.stateChanged.connect(self.enlarge_window)

    def create_progres_bar(self):
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(250,55,250,20)

    def create_combo_box(self):
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItems(QtWidgets.QStyleFactory.keys())
        self.comboBox.move(0,115)
        self.comboBox.activated[str].connect(self.choise_style)

    def choise_style(self, text):
        '''
        NOT WORKING!!!
        '''
        self.currentStyle.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QtStyleFactory.create(str(text)))

    def enlarge_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 800, 420)
        else:
            self.setGeometry(50, 50, 500, 300)

    def pop_up_on_exit(self):
        areYouSure = QtWidgets.QMessageBox.question(self, 'Exit', "Get Out?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        return areYouSure

class Controller():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.gui = View()
        self.gui.quit_btn.clicked.connect(self.clbk_quit)
        self.gui.extractAction_menubar.triggered.connect(self.clbk_quit)
        self.gui.extractAction_toolbar.triggered.connect(self.clbk_quit)

    def run(self):
        self.app.exec()

    def clbk_quit(self):
        get_user_ans = self.gui.pop_up_on_exit()
        time_till_exit = 0
        if get_user_ans == QtWidgets.QMessageBox.Yes:
            while time_till_exit <= 100:
                time_till_exit +=0.00001
                self.gui.progress.setValue(time_till_exit)

            sys.exit()
        else :
            pass


C = Controller()


if __name__ == '__main__':

    C.run()
