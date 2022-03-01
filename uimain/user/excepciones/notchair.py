from uimain.user.excepciones.funcionamiento import Funcionamiento
from tkinter import messagebox

"""
Clase de excepcion relacionada al funcionamiento del programa
Centrada en la selección de botones disponibles

"""


class NotChair(Funcionamiento):
    def __init__(self):
        super().__init__()
        messagebox.showerror(
            title="Error de funcionamiento",
            message="No se ha seleccionado una opción con disponiblidad")