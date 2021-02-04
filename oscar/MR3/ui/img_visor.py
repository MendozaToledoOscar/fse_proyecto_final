# -*- coding: utf-8 -*-

"""
Module implementing Frame.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFrame

from .Ui_img_visor import Ui_Frame


class Frame(QFrame, Ui_Frame):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Frame, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(QPoint)
    def on_graphicsView_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        
        @param pos DESCRIPTION
        @type QPoint
        """
        # TODO: not implemented yet
        raise NotImplementedError
