# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Scripts\Eclipse\Seq2Mov\source\Seq2Mov.ui'
#
# Created: Fri May 20 14:10:28 2016
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Seq2MovWin(object):
    def setupUi(self, Seq2MovWin):
        Seq2MovWin.setObjectName(_fromUtf8("Seq2MovWin"))
        Seq2MovWin.resize(460, 390)
        Seq2MovWin.setMinimumSize(QtCore.QSize(460, 390))
        Seq2MovWin.setMaximumSize(QtCore.QSize(460, 390))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/winIcon/file-movie-clip.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Seq2MovWin.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Seq2MovWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rightListView = QtGui.QListView(self.centralwidget)
        self.rightListView.setGeometry(QtCore.QRect(10, 122, 211, 141))
        self.rightListView.setObjectName(_fromUtf8("rightListView"))
        self.movLabel = QtGui.QLabel(self.centralwidget)
        self.movLabel.setGeometry(QtCore.QRect(10, 270, 61, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movLabel.setFont(font)
        self.movLabel.setObjectName(_fromUtf8("movLabel"))
        self.movLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.movLineEdit.setGeometry(QtCore.QRect(80, 280, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movLineEdit.setFont(font)
        self.movLineEdit.setObjectName(_fromUtf8("movLineEdit"))
        self.movBtn = QtGui.QPushButton(self.centralwidget)
        self.movBtn.setGeometry(QtCore.QRect(411, 270, 41, 41))
        self.movBtn.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:none;\n"
"}"))
        self.movBtn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/folderIcon/folder_invoices.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.movBtn.setIcon(icon1)
        self.movBtn.setIconSize(QtCore.QSize(20, 20))
        self.movBtn.setObjectName(_fromUtf8("movBtn"))
        self.runBtn = QtGui.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(11, 315, 441, 41))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.seqLabel = QtGui.QLabel(self.centralwidget)
        self.seqLabel.setGeometry(QtCore.QRect(10, 0, 61, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seqLabel.setFont(font)
        self.seqLabel.setObjectName(_fromUtf8("seqLabel"))
        self.seqLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.seqLineEdit.setGeometry(QtCore.QRect(80, 10, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seqLineEdit.setFont(font)
        self.seqLineEdit.setObjectName(_fromUtf8("seqLineEdit"))
        self.seqBtn = QtGui.QPushButton(self.centralwidget)
        self.seqBtn.setGeometry(QtCore.QRect(410, 0, 41, 41))
        self.seqBtn.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:none;\n"
"}"))
        self.seqBtn.setText(_fromUtf8(""))
        self.seqBtn.setIcon(icon1)
        self.seqBtn.setIconSize(QtCore.QSize(20, 20))
        self.seqBtn.setObjectName(_fromUtf8("seqBtn"))
        self.errorListView = QtGui.QListView(self.centralwidget)
        self.errorListView.setGeometry(QtCore.QRect(240, 120, 211, 141))
        self.errorListView.setObjectName(_fromUtf8("errorListView"))
        self.rightLabel = QtGui.QLabel(self.centralwidget)
        self.rightLabel.setGeometry(QtCore.QRect(10, 90, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rightLabel.setFont(font)
        self.rightLabel.setObjectName(_fromUtf8("rightLabel"))
        self.errorLabel = QtGui.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(240, 90, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 441, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.exceptLabel = QtGui.QLabel(self.centralwidget)
        self.exceptLabel.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exceptLabel.setFont(font)
        self.exceptLabel.setObjectName(_fromUtf8("exceptLabel"))
        self.exceptLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.exceptLineEdit.setGeometry(QtCore.QRect(80, 50, 321, 20))
        self.exceptLineEdit.setObjectName(_fromUtf8("exceptLineEdit"))
        Seq2MovWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Seq2MovWin)
        QtCore.QMetaObject.connectSlotsByName(Seq2MovWin)

    def retranslateUi(self, Seq2MovWin):
        Seq2MovWin.setWindowTitle(_translate("Seq2MovWin", "Seq2Mov", None))
        self.movLabel.setText(_translate("Seq2MovWin", "输出路径：", None))
        self.runBtn.setText(_translate("Seq2MovWin", "运行", None))
        self.seqLabel.setText(_translate("Seq2MovWin", "序列路径：", None))
        self.rightLabel.setText(_translate("Seq2MovWin", "正确路径", None))
        self.errorLabel.setText(_translate("Seq2MovWin", "错误路径", None))
        self.exceptLabel.setText(_translate("Seq2MovWin", "剔    除：", None))

import Seq2Mov_rc
