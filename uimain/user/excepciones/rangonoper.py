from uimain.user.excepciones.ingresodatos import IngresoDatos
from tkinter import messagebox

"""
Clase de excepcion relacionada a los datos ingresados
Centrada para cuando el tipo de datos no se encuentra en el rando de datos esperados

"""


class RangoNoPer(IngresoDatos):

    def __init__(self):
        super().__init__()
        messagebox.showerror(
            title="Error de ingreso",
            message="Los datos ingresados no se encuentran en el rango esperado")