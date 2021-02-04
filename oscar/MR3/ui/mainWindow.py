# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import (Qt, QDir, QFile, QFileInfo, QPropertyAnimation, QRect, QAbstractAnimation, QTranslator, QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QFrame, QLabel, QFileDialog)

from .Ui_mainWindow import Ui_MainWindow
import sys
import os 
import vlc
import time 

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_exit_btn_clicked(self):
        sys.exit()
    
    def Mostrar_Musica (self,  lista):
        print("Tus Canciones son:")
        for i in lista:
            print(i)
        instance = vlc.Instance()
        player = instance.media_player_new()
        for i in lista:
            media = instance.media_new(i)
            player.set_media(media)
            player.toggle_fullscreen()
            player.play()
            time.sleep(5)
            while player.is_playing():
                time.sleep(1)
        player.stop()
        
    def Mostrar_Video(self, video):
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(video)
        player.set_media(media)
        player.toggle_fullscreen()
        player.play()
        time.sleep(5)
        while player.is_playing():
            time.sleep(1)
        player.stop()
 
    def Mostrar_Fotos(self,  lista):
        print("Tus Fotos son:")
        for i in lista:
            print(i)
        instance = vlc.Instance()
        player = instance.media_player_new()
        for i in lista:
            media = instance.media_new(i)
            player.set_media(media)
            player.toggle_fullscreen()
            player.play()
            time.sleep(5)
            while player.is_playing():
                time.sleep(1)
        player.stop()
  
    @pyqtSlot()
    def on_f_local_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        with os.scandir( "/home/pi/Documents/FSE/FinalProject/fotos") as ficheros:
            fotos = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.jpg')]
        for i in range(len(fotos)):
            fotos[i]  = "/home/pi/Documents/FSE/FinalProject/fotos/"+ fotos[i]
        self.Mostrar_Fotos(fotos)
        
    
    @pyqtSlot()
    def on_v_local_btn_clicked(self):
        """
        Slot documentation goes here.
        """ 
        nombreVideo, _ = QFileDialog.getOpenFileName(self, "Seleccionar video", "/home/pi/Documents/FSE/FinalProject/videos", "Archivos de video (*.mp4)")
        print("NombreImagen: " + nombreVideo)          
        self.Mostrar_Video(nombreVideo)
    
    @pyqtSlot()
    def on_m_local_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        with os.scandir("/home/pi/Documents/FSE/FinalProject/musica") as ficheros:
            musica = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp3')]
        for i in range(len(musica)):
            musica[i]  = "/home/pi/Documents/FSE/FinalProject/musica/"+ musica[i]
        self.Mostrar_Musica(musica)
    
    @pyqtSlot()
    def on_f_usb_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        with os.scandir( "/media/pi/OSCARMT") as ficheros:
            fotos = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.jpg')]
        for i in range(len(fotos)):
            print(fotos[i])
            fotos[i]  = "/media/pi/OSCARMT/"+ fotos[i]
        #self.Mostrar_Fotos(fotos)
