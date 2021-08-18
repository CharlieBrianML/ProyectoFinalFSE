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
	player.stop()#IMPORTANTE, debe cerrarse el reproductor

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
	varVideoFiles = glob.glob(directory+"/Media/Videos/*.mp4")#EN carpeta videos
	#se guardan los nombres de los archivos tipo mp3 en una lista
	varMusicFiles = glob.glob(directory+"/Media/Musica/*.mp3")#EN carpeta musica

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
	webbrowser.open("https://www.netflix.com/mx/Login",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')
	
def playHBO():
	webbrowser.open("https://play.hbomax.com/page/urn:hbo:page:home",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	
	
def playBlim():
	webbrowser.open("https://www.blim.com/cuenta/ingresar?gclid=Cj0KCQjwvO2IBhCzARIsALw3ASq4nBXhINiZmvdURJlh8LcZZmXWvlVstdnbcGqsWsqXVWU3D6mi3RcaAjSxEALw_wcB",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	

def playDisney():
	webbrowser.open("https://www.disneyplus.com/es-419/login",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	

def playPrimeVideo():
	webbrowser.open("https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=132-2111988-0815517&language=es_ES&openid.assoc_handle=amzn_prime_video_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fref%253Ddv_auth_ret",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	
	
def playClaro():
	webbrowser.open("https://www.clarovideo.com/mexico/renta?gclid=Cj0KCQjwvO2IBhCzARIsALw3ASpKqiEAQFmYQeMAbE-NrxD9LNbBKzKs4XM1z5eiV31xUuvDyfzNItsaAjKqEALw_wcB",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')		

def playSpotify():
	webbrowser.open("https://accounts.spotify.com/es/login",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	

def playDeezer():
	webbrowser.open("https://www.deezer.com/es/login?utm_source=adwords&utm_campaign=acq_mx_sea-brd_web_search_perf_tnb-directsub&utm_medium=search&utm_content=brd_premium&utm_term=deezer&gclid=Cj0KCQjwvO2IBhCzARIsALw3ASrF6P0X4r4c0D3qRLbhsp_iN4aPENcHb7BretasSRkoFRKsgWhqnNwaAvZtEALw_wcB",new=2, autoraise=True)
	time.sleep(5)
	pyautogui.press('f11')	


