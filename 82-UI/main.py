# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#if __name__ == "__main__":
#    app = QApplication([])
#    # ...
#    sys.exit(app.exec_())
