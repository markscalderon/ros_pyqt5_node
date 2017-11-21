#!/usr/bin/python

import sys
import rospy
from std_msgs.msg import String
import numpy as np
from PyQt5.QtCore import QThread, QStringListModel, QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QListView

class QNodeT(QThread):
    updateLog = pyqtSignal() ## create a signal to emit when the listview updates
    rosShutdown = pyqtSignal() ## signal the gui for a shutdown
    def __init__(self, text):
        QThread.__init__(self)

        self.text_window = text
        self.model = QStringListModel(self)
        self.list = []
        self.model.setStringList(self.list)
        self.text_window.setModel(self.model)
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker',anonymous=True)
        self.rate = rospy.Rate(10) #2hz

        ##connect signal

    def __del__(self):
        if not rospy.is_shutdown():

            rospy.shutdown('shutdown reason')
            self.wait()

    def run(self):

        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            self.list.append(hello_str)
            self.model.setStringList(self.list)
            self.text_window.setModel(self.model)
            self.updateLog.emit()

            rospy.loginfo(hello_str)
            self.pub.publish(hello_str)
            self.rate.sleep()
        self.rosShutdown.emit() #emit signal for shutdown
