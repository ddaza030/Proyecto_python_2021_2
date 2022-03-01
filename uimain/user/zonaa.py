"""Funcionalidad de la clase: En esta clase se alberga lo correspondiente a la barra superior
    donde estan los menus de archivo, procesos y consultas y ayuda


Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa
"""


from tkinter import *

class ZonaA(Menu):
    def __init__(self, user,zona2):
        super().__init__(user)
        self.user = user
        self.zona2 = zona2
        self.archivos()     #Se ejecuta cada uno de los metodos que crean cada menu de la barra
        self.procesos()
        self.ayuda()
        self.user["menu"] = self

## ventanita de proceso
    def procesos(self):
        self.procesos = Menu(self)
        dic = self.zona2.funciones
        for key,value in dic.items():
            self.procesos.add_command(label = key, command = value)
        
        self.add_cascade(menu = self.procesos, label = "Procesos y Consultas")


## ventanita de archivos
    def archivos(self):
        archivos = Menu(self)
        archivos.add_command(label = "Aplicacion",command=self.aplicacion)
        archivos.add_command(label = "Salir", command = self.user.destroy )
        self.add_cascade(menu = archivos, label = "Archivos")

    #Ventana  de dialogo de aplicacion

    def aplicacion(self):
        
        ventana_nueva=Toplevel()
        ventana_nueva.title("Aplicacion")
        ventana_nueva.geometry("900x300")
        titulo = Label(ventana_nueva, text="Cine Bahía")
        titulo.pack(anchor=NW)
        titulo.config(fg="#009ACD",  font=("Cambria",23),pady=15) 

        informacion=Label(ventana_nueva, text="Esta aplicación fue creada con la finalidad de venta y administración de un cinema.\n Para esto se tiene a la disposicion un menú en donde se tendrán las siguientes opciones:",font=("Microsoft Himalaya",19),width=85)
        informacion.pack(anchor=W)

        i2=Label(ventana_nueva, text="1.Archivos:En el que se se podrá escoger entre Aplicación(Ver información básica) y Salir para regresar al inicio del programa\n      2. Procesos y consultas: Para realizar diversas funciones como son la rifa/venta  de un boleto,\n agregar/quitar una función, programación automática de funciones, entre otras.\n3.Ayuda: Se encontrará los autores del excelente programa",font=("Microsoft Himalaya",19),width=200)
        i2.pack(anchor=W)

        exit_button = Button(ventana_nueva, text="Salir",font=("Microsoft Himalaya",15), command=ventana_nueva.destroy) 
        exit_button.pack(pady=10) 



## ventanita de ayuda
    def ayuda(self):
        ayuda = Menu(self)
        ayuda.add_command(label = "Acerca de",command=self.acerca)
        self.add_cascade(menu = ayuda, label = "Ayuda")

    #Ventana de dialogo de Acerca de 
    def acerca(self):
        ventanacerca=Toplevel()
        ventanacerca.title("Acerca de los POOfantasticos ")
        ventanacerca.geometry("400x550")   

        titulo = Label(ventanacerca, text="Acerca del proyecto")
        titulo.pack(anchor=NW)
        titulo.config(fg="#009ACD",font=("Cambria",23)) 

        tlugar=Label(ventanacerca,text="Materia y Ubicación:",font=("Cambria",17),fg="#EE3B3B",width=20)
        tlugar.pack(anchor=W,pady=10)
        ilugar=Label(ventanacerca,text="Programacion orientada a objetos\nProfesor: Jaime Alberto Guzmán\n\nUniversidad Nacional de Colombia\nSede Medellin\nAño: 2022",font=("Microsoft Himalaya",20),width=30)
        ilugar.pack(anchor=W)


        tinfo=Label(ventanacerca,text="Desarrolladores:",font=("Cambria",17),fg="#EE3B3B",width=20)
        tinfo.pack(anchor=W,pady=10)
        info=Label(ventanacerca,text="\nMarlon Calle Areiza\nDaniel Santiago Cadavid Montoya\nDaniel Daza Macias\nJuan Esteban Ochoa Gomez",font=("Microsoft Himalaya",20),width=30)

        info.pack(anchor=W)

        exit_button = Button(ventanacerca, text="Salir",font=("Microsoft Himalaya",20), command=ventanacerca.destroy) 
        exit_button.pack(anchor=S,pady=30) 

