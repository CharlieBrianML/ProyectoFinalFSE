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

from tkinter import messagebox
import numpy as np
import interfaceTools as it
	
#Se crea la ventana principal del programa
it.createWindowMain()
#Se crea menu desplegable
menu = it.createMenu()
#Se añaden las opciones del menu
opc1 = it.createOption(menu)
it.createCommand(opc1, "Open", it.openFile)
it.createCommand(opc1, "Save", it.saveFile)
it.createCommand(opc1, "Exit", it.mainWindow.quit)
it.createCascade(menu, 'File', opc1)

opc2 = it.createOption(menu)
it.createCascade(menu, 'Media', opc2)

it.mainWindow.mainloop()