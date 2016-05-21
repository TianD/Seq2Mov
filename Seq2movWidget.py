#coding:utf-8
'''
Created on 2015年7月31日 上午11:29:01

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132
'''
import random
from PyQt4 import QtGui, QtCore

XPROGRESS_DEFAULT_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}
QProgressBar::chunk {
    background-color: lightblue;
    width: 2px;
    margin: 1px;
}
"""

XPROGRESS_COMPLETED_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}
QProgressBar::chunk {
    background-color: #CD96CD;
    width: 2px;
    margin: 1px;
}
"""

class XProgressBar(QtGui.QProgressBar):
    def __init__(self, parent = None):
        QtGui.QProgressBar.__init__(self, parent)
        self.setStyleSheet(XPROGRESS_DEFAULT_STYLE)
        self.step = 0
        self.setMaximumHeight(15)

    def setValue(self, value):
        QtGui.QProgressBar.setValue(self, value)
        if value == self.maximum():
            self.setStyleSheet(XPROGRESS_COMPLETED_STYLE)
        else :
            self.setStyleSheet(XPROGRESS_DEFAULT_STYLE)
