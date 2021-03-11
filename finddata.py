# -*- coding: utf-8 -*-
"""
/***************************************************************************
 finddata
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
 *   it under the terms of the MIT License.
 *                                                                         *
 ***************************************************************************/
"""

# compile resources and deploy
# pyrcc5 -o resources.py resources.qrc
# pyuic5 -o finddata_dialog_base.py finddata_dialog_base.ui
# pb_tool deploy -y

from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMessageBox   #, QListView
from PyQt5 import QtWidgets # QtCore, QtGui,


# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .finddata_dialog import finddataDialog
import os.path


class finddata:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'finddata_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&finddata')
        self.toolbar = self.iface.addToolBar(u'finddata')
        self.toolbar.setObjectName(u'finddata')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None


        self.search_folder = ""



    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('finddata', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def search_vector_data(self):
        search_folder = self.search_folder

        #self.listView.addItem(search_folder)
        self.dlg.lvLog.addItem("123")
        self.dlg.lvLog.addItem("123")
        self.dlg.lvLog.addItem(search_folder)
        self.dlg.lvLog.addItem("123")

        numRows = self.dlg.tableWidget.rowCount()
        self.dlg.tableWidget.show()

        # Create a empty row at bottom of table
        numRows = self.dlg.tableWidget.rowCount()
        self.dlg.tableWidget.insertRow(numRows)



        # Add text to the row
        self.dlg.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(numRows)))
        self.dlg.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem("2222"))
        self.dlg.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem("333"))

        QMessageBox.information(None, "Info!", search_folder)


        pass




    def select_root_folder(self):
        foldername = QFileDialog.getExistingDirectory(self.dlg, "Select folder ","",)
        #print("select_root_folder(self)")
        if os.path.exists(foldername):
            self.dlg.edtFolder.setText(foldername)
            self.search_folder = foldername
            self.search_vector_data()




    def search_spatial_data(self):
        root_folder = self.dlg.edtFolder.displayText()
        if root_folder == '':
            QMessageBox.information(None, "Warning!", "No root folder selected. Please select a folder.")
            return
        else:
            QMessageBox.information(None, "Warning!", root_folder)



    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/finddata/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'finddata'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&finddata'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = finddataDialog()


        self.dlg.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("filename"))
        self.dlg.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("ext"))
        self.dlg.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("size"))
        self.dlg.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("sizeh"))
        self.dlg.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("cdata"))



        self.dlg.edtFolder.clear()
        #self.dlg

        # signals
        self.dlg.btnSelectFolder.pressed.connect(self.select_root_folder)
        self.dlg.btnApply.pressed.connect(self.search_spatial_data)

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.

            pass
