# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talker_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from qnodetalker import QNodeT

class Ui_talker(object):
    def setupUi(self, talker):
        talker.setObjectName("talker")
        talker.resize(595, 308)
        self.groupBox = QtWidgets.QGroupBox(talker)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 581, 301))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 561, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.logView.setObjectName("logView")
        self.verticalLayout.addWidget(self.logView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout.addWidget(self.quitButton)
        self.publishButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.publishButton.setObjectName("publishButton")
        self.horizontalLayout.addWidget(self.publishButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.nodo = QNodeT(self.logView) #create qnode to run the Publisher
        self.nodo.updateLog.connect(self.updateLogView) ##connect signal and slot of listview
        self.nodo.rosShutdown.connect(self.close) 

        self.publishButton.clicked.connect(self.talk) ## connect publish button with the talker function
        self.quitButton.clicked.connect(self.close)
        self.flag = False #flag to use one time

        self.retranslateUi(talker)
        QtCore.QMetaObject.connectSlotsByName(talker)

    def retranslateUi(self, talker):
        _translate = QtCore.QCoreApplication.translate
        talker.setWindowTitle(_translate("talker", "Talker ROSPY"))
        self.groupBox.setTitle(_translate("talker", "Talker"))
        self.quitButton.setText(_translate("talker", "Quit"))
        self.publishButton.setText(_translate("talker", "Publish"))

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
    talker = QtWidgets.QWidget()
    ui = Ui_talker()
    ui.setupUi(talker)
    talker.show()
    sys.exit(app.exec_())
