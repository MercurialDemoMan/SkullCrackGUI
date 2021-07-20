#!/usr/bin/env python3
# coding=utf-8

import sys
import os
import subprocess as sp

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5 import QtGui

from SkullCrack.Configuration import Configuration

class MainView(QtWidgets.QMainWindow):

    LevelNames = [
        "1 - Level: Skullmonkeys Gate",
        "2 - Level: Science Center",
        "3 - Movie: Beans + Level: Monkey Shrines",
        "4 - Level: The Incredible Drivy Finn",
        "5 - Boss: Shriney Guard",
        "6 - Level: Hard Boiler",
        "7 - Movie: Root + Level: Sno",
        "8 - Level: SkullMonkeys Brand HotDogs",
        "9 - Boss: Joe-Head-Joe",
        "10 - Level: Elevated Structure of Terror",
        "11 - Movie: Victoid + Level: Ynt Death Garden",
        "12 - Level: Ynt Mines", 
        "13 - Level: Ynt Weeds",
        "14 - Movie: Ynt + Level: Ynt Eggs",
        "15 - Boss: Glenn Yntis",
        "16 - Level: Monk Rushmore",
        "17 - Level: 1970's",
        "18 - Level: Soar Head",
        "19 - Level: Shards",
        "20 - Movie: Hamster + Level: Castle De Los Muertos",
        "21 - Boss: Monkey Mage",
        "22 - Level: The Incredible Drivy Runn",
        "23 - Level: Worm Graveyard",
        "24 - Boss: Klogg",
        "25 - Movie: Evil Engine #9 + Level: Evil Engine #9"
    ]

    def _getUiPath(self, ui_file_name):
        """Get absolute ui path"""

        script_path = os.path.realpath(__file__)
        parent_dir = os.path.dirname(script_path)
        return os.path.join(parent_dir, ui_file_name)

    def __init__(self):

        super().__init__()

        uic.loadUi(self._getUiPath('MainView.ui'), self)
        
        self.levelComboBox.addItems(MainView.LevelNames);
        self.livesEdit.setValidator(QtGui.QIntValidator())
        self.birdsEdit.setValidator(QtGui.QIntValidator())
        self.phartsEdit.setValidator(QtGui.QIntValidator())
        self.enemasEdit.setValidator(QtGui.QIntValidator())
        self.williesEdit.setValidator(QtGui.QIntValidator())
        self._1970sEdit.setValidator(QtGui.QIntValidator())
        self.setWindowIcon(Configuration.WindowIcon())
        self.generateButton.clicked.connect(lambda: self.generatePassword())
                
        self.show()
    
    def generatePassword(self):
        
        out = sp.run(["skullcrack", "-e", str(self.levelComboBox.currentIndex() + 1), self.livesEdit.text(), self.birdsEdit.text(), self.phartsEdit.text(), self.enemasEdit.text(), self.williesEdit.text(), self._1970sEdit.text(), "0"], capture_output=True)
        self.outputEdit.setPlainText(out.stdout.decode("utf-8"))
        
            
            
        