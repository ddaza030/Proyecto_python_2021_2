'''
Funcionalidad de la clase: En este se crea la silleteria de la Sala 2D

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa

'''



from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.salas.silla import Silla

class Sala2D(Sala):


    def __init__ (self,*args):
        if(len(args) == 4):
            filas, columnas, filasvip, cine = args
            super().__init__(filas, columnas, filasvip, 2000,cine)
            
        elif(len(args) == 2):
            vip , cine = args
            super().__init__(8, 12, vip, 2000, cine)

    
    def getTipo(self):
        return "2D"

    def cantidadSillas(self):
        '''
        No recibe nada y devuelve un entero el cual corresponde a la cantidad de sillas
	    disponibles para la creacion de los boletos de la funcion es decir la cantidad de 
	    sillas
        '''
        return len(super().getSillas())
    
    def getCantidadSillas(self):
        return len(super().getSillas())
    
    def crearSilleteria(self):
        '''
        No recibe ningun parametro y no retorna nada
	    Es la encargada de crear cada silla dependiendo la cantidad de filasvip, filas, y columnas
        '''
        total: int =  int(self._filas)*int(self._columnas)  #Numero de sillas 
        totalvip: int = int(self._filasvip)*int(self._columnas) #Numero de sillas vip(se va reduciendo con cada nueva silla vip creada)

        tipo : str = "VIP"          #Se cambia el tipo de silla

        for i in range(total):  
            
            if(totalvip<=0):				#Si se acaban las sillas VIP cambiar el tipo por las sencillas 
                tipo = "SENCILLA"

            else:								
                totalvip-=1
                
            silla : Silla = Silla(tipo,i+1) #Se crea un objeto de silla 
            
            self._sillas.append(silla) #Se agrega la silla que creamos 
