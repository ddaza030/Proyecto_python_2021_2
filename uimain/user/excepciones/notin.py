from uimain.user.excepciones.ingresodatos import IngresoDatos
from tkinter import messagebox

"""
Clase de excepcion relacionada a los datos ingresados
Centrada en datos no encontrados en la base de datos al ser ingresados

"""


class NotIn(IngresoDatos):
    def __init__(self):
        super().__init__()
        messagebox.showerror(
            title="Error de ingreso",
            message="Los datos ingresados no se encuentran en la base de datos")