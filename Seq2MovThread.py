#coding:utf-8
'''
Created on 2016年5月23日 上午10:41:55

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description:

'''
import os, os.path

from PyQt4 import QtGui, QtCore

import Seq2MovCore as co

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
    destFile = u"{0}.mov".format(sourceName.split(".")[0])
    dest = os.path.join(destPath, destFile)
    return co.convertCmd.format(co.ffmpegPath, source, dest)