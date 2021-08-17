#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# Fundamentos de Sistemas Embebidos - UNAM, FI, 2021-2
# usb_lector.py
# Contains the tools to read a usb
#
# Autor: Charlie Brian Monterrubio Lopez
# License: MIT
#
# ## ###############################################

import vlc
import time
import glob
import webbrowser
import pyautogui

tiempoPorSlide = 4
def reproducirFotos(mymedia,tiempo):
#instancia del reproductor
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_list_player_new()#funcion para hacer slideshow
    Media = vlc_instance.media_list_new(mymedia)
    player.set_media_list(Media)

#cada elemento de la lista se reproduce en pantalla por 4 segundos
    for index, name in enumerate(mymedia):
        player.play_item_at_index(index)
        time.sleep(tiempo)#el tiempo de reproduccion de las fotos, videos o musica
#Media.close()#IMPORTANTE, debe cerrarse el reproductor

tiempoPorSlide = 4
def reproducirFotos(mymedia,tiempo):
	#instancia del reproductor
	vlc_instance = vlc.Instance()
	player = vlc_instance.media_list_player_new()#funcion para hacer slideshow
	Media = vlc_instance.media_list_new(mymedia)
	player.set_media_list(Media)

	#cada elemento de la lista se reproduce en pantalla por 4 segundos
	for index, name in enumerate(mymedia):
	    player.play_item_at_index(index)
	    time.sleep(tiempo)#el tiempo de reproduccion de las fotos, videos o musica
	#Media.close()#IMPORTANTE, debe cerrarse el reproductor

def reproducirMusicaVideo(file):
    while True:
        for f in file:
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            media = vlc_instance.media_new(f)
            player.set_media(media)
            player.play()
            time.sleep(1.5)
            duration = player.get_length() / 1000
            time.sleep(duration)
            player.stop()
    player.close()


def playUSB(directory):
	#se guardan los nombres de los archivos tipo png en una lista
	varPhotoFiles = glob.glob(directory+"/Media/Fotos/*.jpg")#En carpeta fotos
	#se guardan los nombres de los archivos tipo mp4 en una lista
	varVideoFiles = glob.glob(directory+"/Media/Musica/*.mp4")#EN carpeta videos
	#se guardan los nombres de los archivos tipo mp3 en una lista
	varMusicFiles = glob.glob(directory+"/Media/Videos/*.mp3")#EN carpeta musica

	print('varPhotoFiles: ',varPhotoFiles)
	print('varVideoFiles: ',varVideoFiles)
	print('varMusicFiles: ',varMusicFiles)
    
	if(len(varPhotoFiles)>0):
		reproducirFotos(varPhotoFiles,2)
	if(len(varMusicFiles)>0):
		reproducirMusicaVideo(varMusicFiles)
	if(len(varVideoFiles)>0):
		reproducirMusicaVideo(varVideoFiles)	
		
def playMedia(directory):
	#se guardan los nombres de los archivos tipo png en una lista
	varPhotoFiles = glob.glob(directory+"/*.jpg")#En carpeta fotos
	#se guardan los nombres de los archivos tipo mp4 en una lista
	varVideoFiles = glob.glob(directory+"/*.mp4")#EN carpeta videos
	#se guardan los nombres de los archivos tipo mp3 en una lista
	varMusicFiles = glob.glob(directory+"/*.mp3")#EN carpeta musica

	print('varPhotoFiles: ',varPhotoFiles)
	print('varVideoFiles: ',varVideoFiles)
	print('varMusicFiles: ',varMusicFiles)
    
	if(len(varPhotoFiles)>0):
		reproducirFotos(varPhotoFiles,2)
	if(len(varMusicFiles)>0):
		reproducirMusicaVideo(varMusicFiles)
	if(len(varVideoFiles)>0):
		reproducirMusicaVideo(varVideoFiles)
		
def playNetflix():
	webbrowser.open("https://www.netflix.com/browse",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')
	
def playSpotify():
	webbrowser.open("https://www.spotify.com/mx/",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	


