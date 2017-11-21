# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listener_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from qnodelistener import QNodeL

class Ui_listener(object):
    def setupUi(self, listener):
        listener.setObjectName("listener")
        listener.resize(567, 323)
        self.groupBox = QtWidgets.QGroupBox(listener)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 541, 301))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 521, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.connectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout_2.addWidget(self.connectButton)
        self.quitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout_2.addWidget(self.quitButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.logView = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.logView.setObjectName("logView")
        self.horizontalLayout_2.addWidget(self.logView)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.nodo = QNodeL(self.logView) #create qnode to run the Publisher
        self.nodo.updateLog.connect(self.updateLogView) ##connect signal and slot of listview
        self.nodo.rosShutdown.connect(self.close)

        self.flag = False #flag to use one time

        self.connectButton.clicked.connect(self.talk) ## connect publish button with the talker function
        self.quitButton.clicked.connect(self.close)

        self.retranslateUi(listener)
        QtCore.QMetaObject.connectSlotsByName(listener)

    def retranslateUi(self, listener):
        _translate = QtCore.QCoreApplication.translate
        listener.setWindowTitle(_translate("listener", "ListenerROSPY"))
        self.groupBox.setTitle(_translate("listener", "Listener"))
        self.connectButton.setText(_translate("listener", "Connect"))
        self.quitButton.setText(_translate("listener", "Quit"))

    def talk(self):
        if not self.flag:
            self.flag = True
            self.nodo.start()

    @pyqtSlot()
    def updateLogView(self):
        self.nodo.text_window.scrollToBottom()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listener = QtWidgets.QWidget()
    ui = Ui_listener()
    ui.setupUi(listener)
    listener.show()
    sys.exit(app.exec_())
