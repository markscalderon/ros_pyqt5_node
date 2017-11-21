#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from listenerui import Ui_listener

class MainWindow(QMainWindow, Ui_listener):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
