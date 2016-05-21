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

import core as co

sys.dont_write_bytecode = True

from PyQt4 import QtGui, QtCore

from Seq2Mov import Ui_Seq2MovWin

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
        self.loadThread = LoadWorker()
        
        seqPath = "{0}".format(self.seqLineEdit.text())
        exceptStr = "{0}".format(self.exceptLineEdit.text())
        exceptLst = exceptStr.split(',')
        self.loadThread.fileSignal.connect(self.fileParseCmd)
        self.loadThread.start(seqPath, exceptLst)
    
    def fileParseCmd(self, right, bad):
        rightModel = QtGui.QStringListModel(right, self.rightListView)
        badModel = QtGui.QStringListModel(bad, self.errorListView)
        self.rightListView.setModel(rightModel)
        self.errorListView.setModel(badModel)
    
    def runCmd(self):
        
        self.subThread = ConvertWorker()
        
#         seqPath = "{0}".format(self.seqLineEdit.text())
        movPath = "{0}".format(self.movLineEdit.text())
#         batName = 'seq2mov'
#         batPath = os.path.dirname(__file__)
        seqModel = self.rightListView.model()
        seqList = seqModel.stringList()
        self.subThread.progressSignal.connect(self.progressBar.setValue)
        self.subThread.start(seqList, movPath)
        #co.convert(seqPath, movPath, batName, batPath)
            
class ConvertWorker(QtCore.QThread):
    progressSignal = QtCore.pyqtSignal(int)
    
    def __init__(self, parent = None):
        super(ConvertWorker, self).__init__(parent)
        self.working = True

    def __del__(self):
        self.working = False
        self.wait()
            
    def start(self, lst, path):
        super(ConvertWorker, self).start()
        self.working = True
        self.lst = lst
        self.path = path
        self.length = len(self.lst)
        

    
    def run(self):
        while self.working :
            for i in range(self.length):
                #for i in range(100):
            #co.convert(self.lst[0], self.lst[1], self.lst[2], self.lst[3])
                    #self.msleep(100) 
                    #self.progressSignal.emit(i+1, "running: %s" %l, 0)
                pathStr = u"{0}".format(self.lst[i])
                percent = float(i)/self.length*100
                self.progressSignal.emit(percent)
                os.system(convertCmd(pathStr, self.path))
            self.working = False
            self.progressSignal.emit(100)
            
class LoadWorker(QtCore.QThread):
    fileSignal = QtCore.pyqtSignal(list, list)
    
    def __init__(self, parent = None):
        super(LoadWorker, self).__init__(parent)
        self.working = True

    def __del__(self):
        self.working = False
        self.wait()
            
    def start(self, path, lst):
        super(LoadWorker, self).start()
        self.working = True
        self.path = path
    
    def run(self):
        while self.working :
            right, bad = parseCmd(self.path)
            self.working = False
            self.fileSignal.emit(right, bad)


def parseCmd(path):
    right = []
    bad = []
    for root, dirs, files in os.walk(path):
        """将序列文件转换成项目需要的ffmpeg格式"""
        projFile = co.SequenceFileDetection()
        projFile.setSequenceFiles(files)
        dic = projFile.getSequenceInfo(1)
        for key, value in dic.iteritems():
            if key == 'separateFiles':
                for i in value:
                    bad.append(os.path.join(root, i))
            else :
                if value[-1]:
                    bad.append(os.path.join(root, key))
                else :
                    right.append(os.path.join(root, key))
    
    return right, bad  

def convertCmd(source, destPath):
    sourceFile = os.path.basename(source)
    sourceName, ext = os.path.splitext(sourceFile)
    destFile = "{0}.mov".format(sourceName)
    dest = os.path.join(destPath, destFile)
    return co.convertCmd.format(co.ffmpegPath, source, dest)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui=Seq2MovWnd()
    ui.show()
    app.exec_()
