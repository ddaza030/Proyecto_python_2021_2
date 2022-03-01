'''
Funcionalidad de la clase: En este se crea la silleteria y se puede observar la cantidad de sillas que posee esta Sala 3D

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa
'''


from fileinput import filename
from importlib.metadata import FileHash

from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.salas.silla import Silla

class Sala3D(Sala):

    def __init__(self, *args):

        if(len(args) == 4):
            filas, columnas,candidadgafas, cine = args
            super().__init__(filas, columnas, 0, 5000,cine)
            self._cantidadgafas = candidadgafas
        elif(len(args) == 3):
            filas, columnas, cine = args
            super().__init__(filas, columnas, 0,5000, cine)
            self._cantidadgafas = filas*columnas
        
    def cantidadSillas(self) -> int:
        '''
        No recibe nada y devuelve un entero el cual corresponde a la cantidad de sillas
	    disponibles para la creacion de los boletos de la funcion
	    esta se encuentra limitada por la cantidad de gafas 3d disponibles para dicha sala
        '''

        totalsillas: int = len(self._sillas)    #Cantidad de sillas del cine

        if (totalsillas<int(self._cantidadgafas)): #Si la cantidad de sillas es menor que las gafas,se devuelve la cantidad de sillas
            return totalsillas
        return int(self._cantidadgafas) #De lo contrario devuelve cantidad de gafas 

    def crearSilleteria(self):
        '''
        No recibe ningun parametro y no retorna nada
	    Es la encargada de crear cada silla dependiendo la cantidad de filas, y columnas
	    por ser la sala 3D crea	todas las sillas vip
        '''

        total: int = int(self._filas)*int(self._columnas)

        tipo: str = "VIP"

        for i in range(total):                  #Crear silas dependiendo del total
            silla: Silla = Silla(tipo, i+1)

            self._sillas.append(silla)

    def getCantidadSillas(self):
        return self._cantidadgafas
    def setCantidadSillas(self, funciones):
        self._cantidadgafas = funciones
    def getTipo(self):
        return("3D")