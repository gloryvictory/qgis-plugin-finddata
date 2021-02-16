# -*- coding: utf-8 -*-
"""
/***************************************************************************
 finddataDialog
                                 A QGIS plugin
 find any spatial data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-01-18
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Viacheslav Zamaraev
        email                : zamaraev@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the MIT License
 *                                                                         *
 ***************************************************************************/
"""

import os

#from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
#from finddata_dialog_base import Ui_finddataDialogBase
#import finddata_dialog_base
from .finddata_dialog_base import Ui_finddataDialogBase


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
# FORM_CLASS, _ = uic.loadUiType(os.path.join(
#     os.path.dirname(__file__), 'finddata_dialog_base.ui'))


#class finddataDialog(QtWidgets.QDialog, FORM_CLASS):
class finddataDialog(QtWidgets.QDialog, Ui_finddataDialogBase):
    def __init__(self, parent=None):
        """Constructor."""

        super(finddataDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
