#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from talkerui import Ui_talker
from PyQt5.QtCore import pyqtSlot
from qnodetalker import QNodeT
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('talker_ui.ui', self)
        self.nodo = QNodeT(self.logView) #create qnode to run the Publisher
        self.nodo.updateLog.connect(self.updateLogView) ##connect signal and slot of listview
        self.nodo.rosShutdown.connect(self.close)

        self.flag = False #flag to use one time

        self.publishButton.clicked.connect(self.talk) ## connect publish button with the talker function
        self.quitButton.clicked.connect(self.close)

    def talk(self):
        if not self.flag:
            self.flag = True
            self.nodo.start()

    @pyqtSlot()
    def updateLogView(self):
        self.nodo.text_window.scrollToBottom()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
