#!/usr/bin/python

import sys
import rospy
from std_msgs.msg import String
import numpy as np
from PyQt5.QtCore import QThread, QStringListModel, QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QListView

class QNodeL(QThread):
    updateLog = pyqtSignal() ## create a signal to emit when the listview updates
    rosShutdown = pyqtSignal() ## signal the gui for a shutdown
    def __init__(self, text):
        QThread.__init__(self)
        rospy.init_node('listener',anonymous=True)
        rospy.Subscriber('chatter', String, self.callback) #2hz
        self.text_window = text
        self.model = QStringListModel(self)
        self.list = []
        self.model.setStringList(self.list)
        self.text_window.setModel(self.model)



        ##connect signal

    def __del__(self):
        if not rospy.is_shutdown():

            #rospy.shutdown('shutdown reason')
            self.wait()

    def callback(self, data):
        hello = rospy.get_caller_id() + 'I heard ' + data.data
        self.list.append(hello)
        self.model.setStringList(self.list)
        self.text_window.setModel(self.model)
        self.updateLog.emit()

        rospy.loginfo(hello)

    def run(self):
        rospy.spin()
        self.rosShutdown.emit() #emit signal for shutdown
