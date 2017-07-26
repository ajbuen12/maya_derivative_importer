
from PyQt4 import QtGui
from mainwindow import Ui_Form as Mainwindow_UI
import os
import maya.mel as mel
import maya.cmds as cmds
import alembic_import as abcImp

class MainWindow(QtGui.QDialog, Mainwindow_UI):

    def __init__(self, parent):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # set default source folder
        global source_folder
        # temporary source folder
        source_folder = "C:/Users/aldous/Desktop/test/"

        self.button_import.clicked.connect(self.import_derivative)
        self.cb_abc.clicked.connect(self.list_derivatives)
        self.cb_obj.clicked.connect(self.list_derivatives)
        self.cb_fbx.clicked.connect(self.list_derivatives)

    def reset_tableValues(self):

        self.lw_derivative.clear()

    def list_derivatives(self):

        self.reset_tableValues()

        # derivativeivative_list = {"mesh_name":"directory"}

        # create dictionary to be added in table

        derivative_list = {}
        if self.cb_obj.isChecked():
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    if file.endswith(".obj"):
                        file_directory = os.path.join(root, file).replace("\\", "/")
                        derivative_list[file]= file_directory

        if self.cb_fbx.isChecked():
             for root, dirs, files in os.walk(source_folder):
                for file in files:
                    if file.endswith(".FBX") or file.endswith(".fbx"):
                        file_directory = os.path.join(root, file).replace("\\", "/")
                        derivative_list[file]= file_directory

        if self.cb_abc.isChecked():
             for root, dirs, files in os.walk(source_folder):
                for file in files:
                    if file.endswith(".abc"):
                        file_directory = os.path.join(root, file).replace("\\", "/")
                        derivative_list[file]= file_directory

        for mesh, path in derivative_list.items():
            item = QtGui.QTreeWidgetItem([mesh, path])
            self.lw_derivative.addTopLevelItem(item)

    def import_derivative(self):

        for item in self.lw_derivative.selectedItems():

            path = item.text(1)
            derivative_name = item.text(0)
            mesh_name, mesh_type = derivative_name.split('.')

            if mesh_type == "FBX":
                if not cmds.pluginInfo('fbxmaya', q=True, l=True):
                    try:
                        cmds.loadPlugin('fbxmaya')
                    except:
                        raise MissingPluginError('Unable to load fbxmaya.mll')
                mel.eval('FBXImport -f "%s" -s' % (path))

            elif mesh_type == "abc" :
                if not cmds.pluginInfo('AbcImport', q=True, l=True):
                    try:
                        cmds.loadPlugin('AbcImport')
                    except:
                        raise MissingPluginError('Unable to load AbcImport.mll')

                abcImp.import_alembic(derivative_name, path)
            elif mesh_type == "obj" :
                cmds.file(path, i=True, groupReference=True, groupName=mesh_name)

if __name__ == "__main__":
    w = MainWindow(None)
    w.show()
