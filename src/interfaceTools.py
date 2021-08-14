#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# Fundamentos de Sistemas Embebidos - UNAM, FI, 2021-2
# interfaceTools.py
# Contains all the tools for creating an interface
#
# Autor: Charlie Brian Monterrubio Lopez
# License: MIT
#
# ## ###############################################

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import filedialog as fd
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import messagebox
from PIL import ImageTk, Image

import cv2 
import os

# Define la ventana principal de la aplicación
mainWindow = Tk()

def openFile():
	"""This function open files of type .oib .tif and .bmp"""
	print('openFile')
	
def saveFile():
	"""This function save files of type .oib .tif and .bmp"""
	print('saveFile')
	
def createWindowMain():
	"""Definition of the main window"""
	# Define la ventana principal de la aplicación
	#mainWindow = Tk() 
	mainWindow.geometry('1100x500') # anchura x altura
	# Asigna un color de fondo a la ventana. 
	mainWindow.configure(bg = 'beige')
	# Asigna un título a la ventana
	mainWindow.title('Media Center')
	mainWindow.resizable(width=False,height=False)
	#return mainWindow
	
#def createMenu(mainWindow):
def createMenu():
	"""This function creates a menu"""
	#Barra superior
	menu = Menu(mainWindow)
	mainWindow.config(menu=menu)
	return menu
	
def createOption(menu):
	"""This function creates a menu option"""
	opc = Menu(menu, tearoff=0)
	return opc
	
def createCommand(opc, labelName, commandName):
	"""This function creates a command"""
	opc.add_command(label=labelName, command = commandName)
	
def createCascade(menu, labelName, option):
	"""This function creates a tab main"""
	menu.add_cascade(label=labelName, menu=option)
	
def createButton(text, command, side):
	"""This function creates a button"""
	ttk.Button(mainWindow, text=text, command=command).pack(side=side)
	
def createEntry(stringVar,x,y):
	"""This function creates a entry"""
	entry = ttk.Entry(mainWindow, textvariable=stringVar)
	entry.place(x=x, y=y)
	return entry

def createLabel(text,x,y):
	"""This function creates a label"""
	label = Label(mainWindow, text=text, font=("Arial", 12)).place(x=x, y=y)
	
def createStringVar():
	"""This function creates a StringVar"""
	nombre = StringVar()
	return nombre
	
def createStatusBar():
	"""This function creates a status bar"""
	global statusbar
	statusbar = Label(mainWindow, text='IFC SuperResolution v0.0.11', bd=1, relief=SUNKEN, anchor=W)
	statusbar.pack(side=BOTTOM, fill=X)
	return statusbar
	
class NewWindow:
	"""This class contains the functions to define a window"""
	
	def __init__(self,nameWindow,size = None):
		self.nameWindow = nameWindow
		self.window = Toplevel(mainWindow)
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.window.geometry(size) # anchura x altura
		#self.window.configure(bg = 'beige')
		self.window.resizable(width=False,height=False)
		self.window.title(self.nameWindow)
		
	def on_closing(self):
		print('Se cerro: ', self.nameWindow)
		self.window.destroy()
		if (self.nameWindow in filesName):
			filesName.remove(self.nameWindow)
			
	def destroy(self):
		self.window.destroy()
		
	def placeImage(self,img):

		resized = self.resize_image_percent(img, 60)
		self.img = ImageTk.PhotoImage(image=Image.fromarray(resized))
		self.panel = Label(self.window, image = self.img)
		self.panel.image = self.img
		self.panel.pack()
		
	def createButton(self,text, command, side):
		ttk.Button(self.window, text=text, command=command).pack(side=side)	

	def createButtonXY(self,text, command, x, y):
		ttk.Button(self.window, text=text, command=command).place(x=x,y=y)	
		
	def createLabel(self,text,x,y):
		#Label(self.window, text=text).pack(anchor=CENTER)
		label = Label(self.window, text=text, font=("Arial", 12)).place(x=x, y=y)		