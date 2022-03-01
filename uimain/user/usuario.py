'''Funcionalidad de la clase: La clase usuario es donde estará la ventana de usuario del programa

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa
'''

from tkinter import *
from uimain.user.zonaa import ZonaA
from uimain.user.zonab import ZonaB
    

class Usuario:
    def __init__(self,cine):
        self.cine=cine
        self.user = Toplevel()
        self.user.title("Ventana de Usuario")
        self.user.geometry("1000x600")  #Tamaño de la ventana 
        self.user.option_add("*tearOff",False)  #Quitar la raya de las opciones de los menus

        self.frame = ZonaB(self.user,cine)
        self.zona1 = ZonaA(self.user, self.frame)

# Usuario().user.mainloop()