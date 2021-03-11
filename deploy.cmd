pyrcc5 -o resources.py resources.qrc

pyuic5 -o finddata_dialog_base.py finddata_dialog_base.ui

pb_tool deploy -y
