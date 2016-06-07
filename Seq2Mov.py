# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Scripts\Eclipse\Seq2Mov\source\Seq2Mov.ui'
#
# Created: Tue May 24 15:07:09 2016
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
        Seq2MovWin.resize(800, 390)
        Seq2MovWin.setMinimumSize(QtCore.QSize(800, 390))
        Seq2MovWin.setMaximumSize(QtCore.QSize(800, 390))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/winIcon/file-movie-clip.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Seq2MovWin.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Seq2MovWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.seqHorizontalLayout = QtGui.QHBoxLayout()
        self.seqHorizontalLayout.setObjectName(_fromUtf8("seqHorizontalLayout"))
        self.seqLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seqLabel.setFont(font)
        self.seqLabel.setObjectName(_fromUtf8("seqLabel"))
        self.seqHorizontalLayout.addWidget(self.seqLabel)
        self.seqLineEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seqLineEdit.setFont(font)
        self.seqLineEdit.setObjectName(_fromUtf8("seqLineEdit"))
        self.seqHorizontalLayout.addWidget(self.seqLineEdit)
        self.seqBtn = QtGui.QPushButton(self.centralwidget)
        self.seqBtn.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:none;\n"
"}"))
        self.seqBtn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/folderIcon/folder_invoices.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.seqBtn.setIcon(icon1)
        self.seqBtn.setIconSize(QtCore.QSize(20, 20))
        self.seqBtn.setObjectName(_fromUtf8("seqBtn"))
        self.seqHorizontalLayout.addWidget(self.seqBtn)
        self.verticalLayout_3.addLayout(self.seqHorizontalLayout)
        self.exceptHorizontalLayout = QtGui.QHBoxLayout()
        self.exceptHorizontalLayout.setObjectName(_fromUtf8("exceptHorizontalLayout"))
        self.exceptLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exceptLabel.setFont(font)
        self.exceptLabel.setObjectName(_fromUtf8("exceptLabel"))
        self.exceptHorizontalLayout.addWidget(self.exceptLabel)
        self.exceptLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.exceptLineEdit.setObjectName(_fromUtf8("exceptLineEdit"))
        self.exceptHorizontalLayout.addWidget(self.exceptLineEdit)
        self.verticalLayout_3.addLayout(self.exceptHorizontalLayout)
        self.viewHorizontalLayout = QtGui.QHBoxLayout()
        self.viewHorizontalLayout.setObjectName(_fromUtf8("viewHorizontalLayout"))
        self.rightVerticalLayout = QtGui.QVBoxLayout()
        self.rightVerticalLayout.setObjectName(_fromUtf8("rightVerticalLayout"))
        self.rightLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rightLabel.setFont(font)
        self.rightLabel.setObjectName(_fromUtf8("rightLabel"))
        self.rightVerticalLayout.addWidget(self.rightLabel)
        self.rightListView = QtGui.QListView(self.centralwidget)
        self.rightListView.setObjectName(_fromUtf8("rightListView"))
        self.rightVerticalLayout.addWidget(self.rightListView)
        self.viewHorizontalLayout.addLayout(self.rightVerticalLayout)
        self.errorVerticalLayout = QtGui.QVBoxLayout()
        self.errorVerticalLayout.setObjectName(_fromUtf8("errorVerticalLayout"))
        self.errorLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.errorVerticalLayout.addWidget(self.errorLabel)
        self.errorListView = QtGui.QListView(self.centralwidget)
        self.errorListView.setObjectName(_fromUtf8("errorListView"))
        self.errorVerticalLayout.addWidget(self.errorListView)
        self.viewHorizontalLayout.addLayout(self.errorVerticalLayout)
        self.verticalLayout_3.addLayout(self.viewHorizontalLayout)
        self.movHorizontalLayout = QtGui.QHBoxLayout()
        self.movHorizontalLayout.setObjectName(_fromUtf8("movHorizontalLayout"))
        self.movLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movLabel.setFont(font)
        self.movLabel.setObjectName(_fromUtf8("movLabel"))
        self.movHorizontalLayout.addWidget(self.movLabel)
        self.movLineEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movLineEdit.setFont(font)
        self.movLineEdit.setObjectName(_fromUtf8("movLineEdit"))
        self.movHorizontalLayout.addWidget(self.movLineEdit)
        self.movBtn = QtGui.QPushButton(self.centralwidget)
        self.movBtn.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:none;\n"
"}"))
        self.movBtn.setText(_fromUtf8(""))
        self.movBtn.setIcon(icon1)
        self.movBtn.setIconSize(QtCore.QSize(20, 20))
        self.movBtn.setObjectName(_fromUtf8("movBtn"))
        self.movHorizontalLayout.addWidget(self.movBtn)
        self.verticalLayout_3.addLayout(self.movHorizontalLayout)
        self.runBtn = QtGui.QPushButton(self.centralwidget)
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.verticalLayout_3.addWidget(self.runBtn)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_3.addWidget(self.progressBar)
        Seq2MovWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Seq2MovWin)
        QtCore.QMetaObject.connectSlotsByName(Seq2MovWin)

    def retranslateUi(self, Seq2MovWin):
        Seq2MovWin.setWindowTitle(_translate("Seq2MovWin", "腾清序列转mov工具", None))
        self.seqLabel.setText(_translate("Seq2MovWin", "序列路径：", None))
        self.exceptLabel.setText(_translate("Seq2MovWin", "剔    除：", None))
        self.rightLabel.setText(_translate("Seq2MovWin", "正确路径", None))
        self.errorLabel.setText(_translate("Seq2MovWin", "错误路径", None))
        self.movLabel.setText(_translate("Seq2MovWin", "输出路径：", None))
        self.runBtn.setText(_translate("Seq2MovWin", "运行", None))

import Seq2Mov_rc
