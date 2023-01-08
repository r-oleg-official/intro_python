# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms.main import Ui_MainWindow


class Gui(QtWidgets.QMainWindow):
    """Class of interface"""

    def __init__(self, parent=None):
        super().__init_(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.download_folder = None
        self.ui.pushButton.clicked.connect(self.get_folder)
        self.ui.pushButton_2.clicked.connect(self.start)

class Downloader(QMainWindow, Ui_MainWindow):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Downloader()
    ex.show()
    sys.exit(app.exec())
