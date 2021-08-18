#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# Fundamentos de Sistemas Embebdios - UNAM, FI, 2021-2
# mainMediaCenter.py
# File main
#
# Autor: Charlie Brian Monterrubio Lopez
# License: MIT
#
# ## ###############################################

import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox
import mediaLector as ml
import multiprocessing

def openFile():
	"""This function open files of type .bmp .png and .jpg"""
	file = fd.askopenfilename(initialdir = os.getcwd(), title = 'Seleccione archivo', defaultextension = '*.*', filetypes = (('png files','*.png'),('jpg files','*.jpg'),('bmp files','*.bmp')))
	
def openDireactory():
	"""This function open a directory media"""
	directory = fd.askdirectory()
	print('directory: ', directory)
	ml.playMedia(directory)
	
def eventUSB(directory, play):
	print('Abriendo multimedios...')
	if play:
		ml.playUSB(directory)
	
def checkUSBconnection(var):
	play = True
	while True:
		d={}
		for l in open('/proc/mounts'):
			if(l[0] == '/'):
				l = l.split()
				d[l[0]] = l[1]
			
		if('/dev/sdb1' in d):
			eventUSB(d['/dev/sdb1'], play)
			play = False


def interface():

	mainWindow = tk.Tk()  
	mainWindow.geometry("960x600")
	mainWindow.title('Media Player')
	mainWindow.resizable(width=False,height=False)
	imgbackground = Image.open('src_img/background.jpg')
	imgbackground = imgbackground.resize((960, 600), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgbackground = ImageTk.PhotoImage(imgbackground)
	panel = tk.Label(mainWindow, image = imgbackground)
	panel.image = imgbackground
	panel.pack()

	imgNetflix = Image.open('src_img/Netflix-logo.jpg')
	imgNetflix = imgNetflix.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgNetflix = ImageTk.PhotoImage(imgNetflix)
	tk.Button(mainWindow, command=ml.playNetflix, image=imgNetflix, text="Netflix").place(x=50, y=20)

	imgHBO = Image.open('src_img/HBO-logo.png')
	imgHBO = imgHBO.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgHBO = ImageTk.PhotoImage(imgHBO)
	tk.Button(mainWindow, command=ml.playHBO, image=imgHBO, text="HBO").place(x=350, y=20)

	imgBlim = Image.open('src_img/Blim-logo.jpg')
	imgBlim = imgBlim.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgBlim = ImageTk.PhotoImage(imgBlim)
	tk.Button(mainWindow, command=ml.playBlim, image=imgBlim, text="Blim").place(x=650, y=20)	
	
	imgDisney = Image.open('src_img/Disney-logo.jpeg')
	imgDisney = imgDisney.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgDisney = ImageTk.PhotoImage(imgDisney)
	tk.Button(mainWindow, command=ml.playDisney, image=imgDisney, text="Disney").place(x=50, y=220)	

	imgPrime = Image.open('src_img/Primevideo-logo.jpg')
	imgPrime = imgPrime.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgPrime = ImageTk.PhotoImage(imgPrime)
	tk.Button(mainWindow, command=ml.playPrimeVideo, image=imgPrime, text="PrimeVideo").place(x=350, y=220)		
	
	imgClaro = Image.open('src_img/Claro-logo.jpg')
	imgClaro = imgClaro.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgClaro = ImageTk.PhotoImage(imgClaro)
	tk.Button(mainWindow, command=ml.playClaro, image=imgClaro, text="PrimeVideo").place(x=650, y=220)		

	imgSpotify = Image.open('src_img/Spotify-logo.jpg')
	imgSpotify = imgSpotify.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgSpotify = ImageTk.PhotoImage(imgSpotify)
	tk.Button(mainWindow, command=ml.playSpotify, image=imgSpotify, text="Spotify").place(x=50, y=420)
	
	imgDeezer = Image.open('src_img/Deezer-logo.jpg')
	imgDeezer = imgDeezer.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgDeezer = ImageTk.PhotoImage(imgDeezer)
	tk.Button(mainWindow, command=ml.playDeezer, image=imgDeezer, text="Deezer").place(x=350, y=420)

	imgMedia = Image.open('src_img/Media-logo.jpg')
	imgMedia = imgMedia.resize((250, 150), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	imgMedia = ImageTk.PhotoImage(imgMedia)
	tk.Button(mainWindow, command=openDireactory, image=imgMedia, text="Media").place(x=650, y=420)

	process = multiprocessing.Process(target=checkUSBconnection, args=(None,))
	process.start()

	mainWindow.mainloop()
	process.terminate()

if __name__ == '__main__':
	interface()