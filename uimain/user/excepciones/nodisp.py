from uimain.user.excepciones.funcionamiento import Funcionamiento
from tkinter import messagebox

"""
Clase de excepcion relacionada al funcionamiento del programa
Centrada en la selección de funciones y la no disponibilidad

"""


class NoDisp(Funcionamiento):

    def __init__(self):
        super().__init__()
        messagebox.showerror(
            title="Error de funcionamiento",
            message="No hay funciones disponibles para ese dia")