# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Users\td_training\script_dev\import_derivative\ui\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(425, 349)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb_obj = QtGui.QCheckBox(Form)
        self.cb_obj.setObjectName(_fromUtf8("cb_obj"))
        self.horizontalLayout.addWidget(self.cb_obj)
        self.cb_fbx = QtGui.QCheckBox(Form)
        self.cb_fbx.setObjectName(_fromUtf8("cb_fbx"))
        self.horizontalLayout.addWidget(self.cb_fbx)
        self.cb_abc = QtGui.QCheckBox(Form)
        self.cb_abc.setObjectName(_fromUtf8("cb_abc"))
        self.horizontalLayout.addWidget(self.cb_abc)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lw_derivative = QtGui.QTreeWidget(Form)
        self.lw_derivative.setObjectName(_fromUtf8("lw_derivative"))
        self.verticalLayout.addWidget(self.lw_derivative)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_import = QtGui.QPushButton(Form)
        self.button_import.setObjectName(_fromUtf8("button_import"))
        self.horizontalLayout_3.addWidget(self.button_import)
        self.button_cancel = QtGui.QPushButton(Form)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.horizontalLayout_3.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Import Derivative", None))
        self.cb_obj.setText(_translate("Form", "obj", None))
        self.cb_fbx.setText(_translate("Form", "fbx", None))
        self.cb_abc.setText(_translate("Form", "abc", None))
        self.button_import.setText(_translate("Form", "Import", None))
        self.button_cancel.setText(_translate("Form", "Cancel", None))
        self.lw_derivative.setColumnWidth(0, 195)
        self.lw_derivative.resizeColumnToContents(1)
        self.lw_derivative.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.lw_derivative.headerItem().setText(0, _translate("Form", "Derivative", None))
        self.lw_derivative.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.lw_derivative.headerItem().setText(1, _translate("Form", "Source Directory", None))
