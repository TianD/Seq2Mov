#coding:utf-8
'''
Created on 2016年5月6日 下午3:27:26

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description:

'''
import os, os.path
import sys,time
import re
from _functools import partial

sys.dont_write_bytecode = True

from PyQt4 import QtGui, QtCore

from Seq2Mov import Ui_Seq2MovWin

import Seq2MovThread as s2mThread

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


class Seq2MovWnd(QtGui.QMainWindow, Ui_Seq2MovWin):

    def __init__(self, parent = None):
        super(Seq2MovWnd, self).__init__(parent)
        self.setupUi(self)
        
        ###
        # set ui style
        self.progressBar.setStyleSheet(XPROGRESS_DEFAULT_STYLE)
        ###
        
        self.seqBtn.clicked.connect(partial(self.pathCmd, 'seq'))
        self.movBtn.clicked.connect(partial(self.pathCmd, 'mov'))
        self.runBtn.clicked.connect(self.runCmd)
        
        self.seqLineEdit.editingFinished.connect(self.loadCmd)
                
    def pathCmd(self, seqORmov):
        pathDialog = QtGui.QFileDialog(parent = self)
        
        if seqORmov == 'seq':
            pathDialog.setAcceptMode(0)
            pathDialog.fileSelected.connect(self.seqLineEdit.setText)
            pathDialog.fileSelected.connect(self.seqLineEdit.editingFinished)
        else :
            pathDialog.setAcceptMode(1)
            pathDialog.fileSelected.connect(self.movLineEdit.setText)
            pathDialog.fileSelected.connect(self.movLineEdit.editingFinished)
        
        pathDialog.setFileMode(4)
        
        pathDialog.show()
    
    def loadCmd(self):
        self.loadThread = s2mThread.LoadWorker()
        
        seqPath = u"{0}".format(self.seqLineEdit.text())
        exceptStr = u"{0}".format(self.exceptLineEdit.text())
        exceptLst = exceptStr.split(',')
        self.loadThread.fileSignal.connect(self.fileParseCmd)
        self.loadThread.start(seqPath, exceptLst)
    
    def fileParseCmd(self, right, bad):
        rightModel = QtGui.QStringListModel(right, self.rightListView)
        badModel = QtGui.QStringListModel(bad, self.errorListView)
        self.rightListView.setModel(rightModel)
        self.errorListView.setModel(badModel)
    
    def runCmd(self):
        
        self.subThread = s2mThread.ConvertWorker()
        
        movPath = u"{0}".format(self.movLineEdit.text())

        seqModel = self.rightListView.model()
        seqList = seqModel.stringList()
        self.subThread.progressSignal.connect(self.setProgressCmd)
        self.subThread.start(seqList, movPath)
    
    def setProgressCmd(self, value):
        self.progressBar.setValue(value)
        if value >= 100:
            self.progressBar.setStyleSheet(XPROGRESS_COMPLETED_STYLE)
        else :
            self.progressBar.setStyleSheet(XPROGRESS_DEFAULT_STYLE)          
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui=Seq2MovWnd()
    ui.show()
    app.exec_()
