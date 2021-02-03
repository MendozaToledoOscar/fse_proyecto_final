#!/usr/bin/env python3
import os 
import vlc
import time 


def menu():
  os.system('clear')
  print("\t\tBIENVENIDO A CENTRO MULTIMEDIA")
  print("Selecciona una de las siguientes opciones:")
  print("\t1 - Entrar a NETFLIX")
  print("\t2 - Entrar a SPOTIFY")
  print("\t3 - REPRODUCIR MEDIO EXTRAIBLE")
  print("\t9 - SALIR")

def menuUSBMixta(v, m, f):
  os.system('clear')
  print("La memoria tiene contenido mixto")
  print("Selecciona una de las siguientes opciones:")
  print("\t1 - Reproducir videos")
  print("\t2 - Reproducir musica")
  print("\t3 - Reproducir fotos")
  opcionMixta = input("inserta el numero de la opcion elegida >> ")

  if opcionMixta == '1':
    reproducirVideos(v)
  elif opcionMixta == '2':
    reproducirMusica(m)
  elif opcionMixta == '3':
    reproducirFotos(f)
  else:
    print("opcion incorrecta") 

  


def medioExtraible():
  with os.scandir("/home/luis/Documents/FSEm/proyecto/") as ficheros:
    musica = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp3')]
    
  with os.scandir("/home/luis/Documents/FSEm/proyecto/") as ficheros:
    videos = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp4')]
    
  with os.scandir("/home/luis/Documents/FSEm/proyecto/") as ficheros:
    fotos = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.jpg')]

  print(len(videos))
  print(len(musica))
  print(len(fotos))
 
  if len(videos) != 0 and len(musica) == 0 and len(fotos) == 0:
    os.system('clear')
    print("MEMORIA CON VIDEOS")
    reproducirVideos(videos)

  elif len(fotos) != 0 and len(videos) == 0 and len(musica) == 0:
    os.system('clear')
    print("MEMORIA CON FOTOS")
    reproducirFotos(fotos)


  elif len(musica) != 0 and len(fotos) == 0 and len(videos) == 0:
    os.system('clear')
    print("MEMORIA CON MUSICA")
    reproducirMusica(musica)

  else:
    os.system('clear')
    print("MEMORIA MIXTA")
    menuUSBMixta(videos, musica, fotos)

def reproducirVideos(lista):
  opcionVideo = '1'
  while opcionVideo != '3':
    os.system('clear')
    print("Elige la opcion que gustes hacer con los videos")
    print("\t1 - Elegir video a reproducir")
    print("\t2 - Reproducir todos los videos en modo presentacion")
    print("\t3 - Regresar al Menu principal")

    opcionVideo = input("inserta el numero de la opcion elegida >> ")

    if opcionVideo == '1':
      print("Tus videos son: ")
      for i in lista:
        print(i)
      video = input("Ingresa el nombre del video a reproducir >> ")
      print("REPRODUCIENDO...")
      instance = vlc.Instance()
      player = instance.media_player_new()
      media = instance.media_new(video)
      player.set_media(media)
      player.play()
      time.sleep(5)
      while player.is_playing():
        time.sleep(1)
      player.stop()
    if opcionVideo == '2':
      instance = vlc.Instance()
      player = instance.media_player_new()
      for i in lista:
        media = instance.media_new(i)
        player.set_media(media)
        player.play()
        time.sleep(5)
        while player.is_playing():
          time.sleep(1)
      player.stop()

def reproducirFotos(lista):
  print("Tus Fotos son:")
  for i in lista:
    print(i)
  instance = vlc.Instance()
  player = instance.media_player_new()
  for i in lista:
    media = instance.media_new(i)
    player.set_media(media)
    player.play()
    time.sleep(5)
    while player.is_playing():
      time.sleep(1)
  player.stop()

def reproducirMusica(lista):
  print("Tus Canciones son:")
  for i in lista:
    print(i)
  instance = vlc.Instance()
  player = instance.media_player_new()
  for i in lista:
    media = instance.media_new(i)
    player.set_media(media)
    player.play()
    time.sleep(5)
    while player.is_playing():
      time.sleep(1)
  player.stop()




while True:
  menu()
  opcionMenu = input("inserta el numero de la opcion elegida >> ")

  if opcionMenu == "1":
    print("Haz elegido la opcion de entrar a NETFLIX")
    input("pulsa una tecla para continuar")

  elif opcionMenu == "2":
    print("Haz elegido la opcion de entrar a SPOTIFY")
    input("pulsa una tecla para continuar")

  elif opcionMenu == "3":
    print("Haz elegido la opcion de REPRODUCIR MEDIO EXTRAIBLE")
    print("Inserta la memoria USB...")
    medioExtraible()
    input("pulsa una tecla para continuar")

  elif opcionMenu == "9":
    print("HASTA LUEGO")
    break

  else:
    print("Opcion incorrecta")
    input("pulsa una tecla para continuar")




