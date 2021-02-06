# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
##############################################
#
# mainWindow.py
# Contiene la lógica para reproducir los archivos seleccionados por el usuario,
# y la lógica para abrir las páginas web solicitadas 
#
# Autores: Mendoza Toledo Oscar 
#          Hernandez Rendon Luis Roberto
#
##############################################
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import (QFileDialog)

from .Ui_mainWindow import Ui_MainWindow
import sys
import os 
import vlc
import time 
import webbrowser

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
        """
        Reproduce las canciones de un directorio haciendo uso de la libreria VLC,
        creando una instancia de la libreria y recorriendo la lista de canciones,
        se le pasa al reproductor el nombre de todas las canciones de la lista

        Parametros
        ----------
        lista: lista de string
               lista que contiene el nombre de las canciones que se van a reproducir

        """
        print("Tus Canciones son:")
        for i in lista:
            print(i)
        instance = vlc.Instance() #Crear nueva instancia vlc
        player = instance.media_player_new() #Crear nuevo reproducto
        # Reproducimos todas las canciones
        for i in lista: # Para cada cancion en la lista
            media = instance.media_new(i) 
            player.set_media(media)
            player.toggle_fullscreen()
            player.play()
            time.sleep(2)
            while player.is_playing():
                time.sleep(1)
        player.stop() #Una vez que terminen las canciones cierra el reproductor
        
    def Mostrar_Video(self, video):
        """
        Reproduce el video seleccionado usando la libreria VLC, se crea el reproductor
        y se le pasa el nombre del video que será reproducido

        Parametros
        ----------
        video: string
               nombre del video que será reproducido
            
        """
        instance = vlc.Instance() #Crear nueva instancia vlc
        player = instance.media_player_new() #Crear nuevo reproducto
        # Se reproduce el video seleccionado
        media = instance.media_new(video)
        player.set_media(media)
        player.toggle_fullscreen()
        player.play()
        time.sleep(5)
        #Espera a que termine el video
        while player.is_playing():
            time.sleep(1)
        player.stop() #Cierra el reproductor
 
    def Mostrar_Fotos(self,  lista):
        """
        Reproduce las fotos de un directorio haciendo uso de la libreria VLC,
        creando una instancia de la libreria y recorriendo la lista de fotos,
        se reproduce cada una a manera de presentación

        Parametros
        ----------
        lista: lista de string
               lista que contiene el nombre de las fotos que se van a reproducir
            
        """
        print("Tus Fotos son:")
        for i in lista:
            print(i)
        instance = vlc.Instance() #Crear nueva instancia vlc
        player = instance.media_player_new() #Crear nuevo reproducto
        # Reproducimos todas las canciones
        for i in lista:# Para cada cancion en la lista
            media = instance.media_new(i)
            player.set_media(media)
            player.toggle_fullscreen()
            player.play()
            time.sleep(3)
            while player.is_playing():
                time.sleep(1)
        player.stop() #Una vez que terminen las canciones cierra el reproductor
  
    @pyqtSlot()
    def on_f_local_btn_clicked(self):
        """
        Al hacer click busca fotos en carpeta local y llama función para reproducirlas
        """
        #Buscamos en la carpeta local de fotos archivos con extension jpg y los guarda en una lista
        with os.scandir( "/home/pi/Documents/FSE/FinalProject/fotos") as ficheros:
            fotos = [fichero.path for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.jpg')]
        for i in range(len(fotos)):
            print("Foto " + str(i) + ": "+ str(fotos[i]))
        self.Mostrar_Fotos(fotos)
        
    
    @pyqtSlot()
    def on_v_local_btn_clicked(self):
        """
        Al hacer click abre menu para seleccionar video en directorio local y llama función para reproducirlo
        """
        #Se guarda en una variable la ruta del archivo local de video seleccionado en el explorador de archivos
        nombreVideo, _ = QFileDialog.getOpenFileName(self, "Seleccionar video", "/home/pi/Documents/FSE/FinalProject/videos", "Archivos de video (*.mp4)")
        print("NombreImagen: " + nombreVideo)          
        self.Mostrar_Video(nombreVideo)
    
    @pyqtSlot()
    def on_m_local_btn_clicked(self):
        """
        Al hacer click busca musica en carpeta local y llama función para reproducirla
        """
        #Buscamos en la carpeta local de musica archivos con extension mp3 y los guarda en una lista
        with os.scandir("/home/pi/Documents/FSE/FinalProject/musica") as ficheros:
            musica = [fichero.path for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp3')]
        for i in range(len(musica)):
            print("Cancion " + str(i) + ": "+ str(musica[i]))
        self.Mostrar_Musica(musica)
    
    @pyqtSlot()
    def on_f_usb_btn_clicked(self):
        """
        Al hacer click busca fotos en usb y llama función para reproducirlas
        """
        # Busca en cada directorio dentro de media/pi
        # Ya que en esta ruta se encuentran los medios extraibles
        # De esta forma sin importar el nombre del USB podrá acceder a el
        with os.scandir("/media/pi") as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    print(entry.name)
                    
        with os.scandir("/media/pi") as ficheros:
            directorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
        for i in range(len(directorios)):
            print("Directorio ["+ str(i) + "]: "+ directorios[i])
            with os.scandir("/media/pi/" + directorios[i]) as ficheros:
                fotos = [fichero.path for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.jpg')]
        for i in range(len(fotos)):
            print("Foto " + str(i) + ": "+ str(fotos[i]))
        self.Mostrar_Fotos(fotos)
        
    @pyqtSlot()
    def on_m_usb_btn_clicked(self):
        """
        Al hacer click busca musica en usb y llama función para reproducirla
        """
        # Busca en cada directorio dentro de media/pi
        # Ya que en esta ruta se encuentran los medios extraibles
        # De esta forma sin importar el nombre del USB podrá acceder a el
        with os.scandir("/media/pi") as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    print(entry.name)
                    
        with os.scandir("/media/pi") as ficheros:
            directorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
        for i in range(len(directorios)):
            print("Directorio ["+ str(i) + "]: "+ directorios[i])
            with os.scandir("/media/pi/" + directorios[i]) as ficheros:
                musica = [fichero.path for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp3')]
        for i in range(len(musica)):
            print("Foto " + str(i) + ": "+ str(musica[i]))
        self.Mostrar_Musica(musica)
    
    @pyqtSlot()
    def on_v_usb_btn_clicked(self):
        """
        Al hacer click abre menu para seleccionar video en medio usb y llama función para reproducirlo
        """
        #Se guarda en una variable la ruta del archivo de video en la usb seleccionado en el explorador de archivos
        nombreVideo, _ = QFileDialog.getOpenFileName(self, "Seleccionar video", "/media/pi/", "Archivos de video (*.mp4)")
        print("NombreImagen: " + nombreVideo)          
        self.Mostrar_Video(nombreVideo)
  
    @pyqtSlot()
    def on_spotify_btn_clicked(self):
        """
        Invoca al navegador para abrir una pagina web indicada, se hace uso de 
        la libreria WEBBROWSER 
        """
        webbrowser.open("https://open.spotify.com/", new=2, autoraise=True)
  
    @pyqtSlot()
    def on_netlfix_btn_clicked(self):
        """
        Invoca al navegador para abrir una pagina web indicada, se hace uso de 
        la libreria WEBBROWSER
        """
        webbrowser.open("https://www.netflix.com/", new=2, autoraise=True)


