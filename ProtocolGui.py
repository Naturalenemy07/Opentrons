"""This file starts a GUI where you can change the settings for each of the protocols. The protocol settings
    are loaded via their settings file, which is generated and read in their settings class."""

import sys
import os
from PyQt5 import QtWidgets, Qt, QtGui, QtCore, uic


class protocolGui(QtWidgets.QMainWindow):
    def __init__(self):
        super(protocolGui, self).__init__()
        uic.loadUi('Opentrons_Settings.ui', self)
        settings_file_location = 'Volumes/Seagate_Drive/Settings_Files'

        self.show()

class ContainerImage:
    def __init__(self):
        identity = 0 # Index for

    def create_plate(self):

    def create_well_circle(self):
        well = QtGui.QPolygon()


app = Qt.QApplication(sys.argv)
startup = protocolGui()
sys.exit(app.exec_())
