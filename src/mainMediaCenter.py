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

# from tkinter import messagebox
# import numpy as np
#import interfaceTools as it

import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import filedialog as fd
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

def eventButton():
	print('Button press')
	import time
	time.sleep(10)
	print('ya termine')
	
def eventUSB():
	print('Abriendo multimedios')
	
def checkUSBconnection(var):
	d={}
	while True:
		for l in open('/proc/mounts'):
			if(l[0] == '/'):
				l = l.split()
				d[l[0]] = l[1]
			
		if('/dev/sdb1' in d):
			eventUSB()

# #Se crea la ventana principal del programa
# it.createWindowMain()
# #Se crea menu desplegable
# menu = it.createMenu()
# #Se añaden las opciones del menu
# opc1 = it.createOption(menu)
# it.createCommand(opc1, "Open", it.openFile)
# it.createCommand(opc1, "Save", it.saveFile)
# it.createCommand(opc1, "Exit", it.mainWindow.quit)
# it.createCascade(menu, 'File', opc1)

# opc2 = it.createOption(menu)
# it.createCascade(menu, 'Media', opc2)

# #it.createButtonXY('Netflix', eventButton, 100, 100, 'src_img/Netflix-logo.jpg')
# it.createButtonXY('Netflix', eventButton, 100, 100, 'src_img/Netflix-logo.jpg')

# it.mainWindow.mainloop()


def interface():

	mainWindow = tk.Tk()  
	mainWindow.geometry("960x600")
	#mainWindow.configure(bg = 'black')
	img3 = Image.open('src_img/background.jpg')
	img3 = img3.resize((960, 600), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	img3 = ImageTk.PhotoImage(img3)
	panel = tk.Label(mainWindow, image = img3)
	panel.image = img3
	panel.pack()

	img = Image.open('src_img/Netflix-logo.jpg')
	img = img.resize((350, 250), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	img = ImageTk.PhotoImage(img)
	tk.Button(mainWindow, command=ml.playNetflix, image=img, text="Netflix").place(x=100, y=50)

	img2 = Image.open('src_img/Spotify-logo.jpg')
	img2 = img2.resize((350, 250), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	img2 = ImageTk.PhotoImage(img2)
	tk.Button(mainWindow, command=ml.playSpotify, image=img2, text="Spotify").place(x=500, y=50)

	img4 = Image.open('src_img/Media-logo.jpg')
	img4 = img4.resize((350, 250), Image.ANTIALIAS) # Redimension (Alto, Ancho)
	img4 = ImageTk.PhotoImage(img4)
	tk.Button(mainWindow, command=openDireactory, image=img4, text="Media").place(x=300, y=320)

	process = multiprocessing.Process(target=checkUSBconnection, args=(None,))
	process.start()

	mainWindow.mainloop()
	process.terminate()

if __name__ == '__main__':
	interface()