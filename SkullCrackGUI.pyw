#!/usr/bin/env python3
# coding=utf-8

import sys
import os
from PyQt5 import QtWidgets

from SkullCrack.Views.MainView import MainView
from SkullCrack.Configuration import Configuration

def main(args):
    """main entry point"""
    
    # create and launch main window
    app = QtWidgets.QApplication(sys.argv)
    window = MainView()
    app.exec()

if __name__ == '__main__':
    main(sys.argv)
