#Funcionalidad de la clase: Enum con la intencion de limitar los horarios del cine
	#Son seis horarios, cada uno con una hora relacionada

#Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa

from enum import Enum

class Horario(Enum):
    UNO="12:00"
    DOS="14:00"
    TRES="16:00"
    CUATRO="18:00" 
    CINCO="20:00" 
    SEIS="22:00"

    def __init__(self,hora):
        self._hora = hora       #Asociar a cada horario una hora

    @classmethod
    def getHorario(cls,hora)->"Horario": #Metodo Statico que devuelve una hora en Horario y devuelve esa misma hora en String
        horarios=[cls.UNO,cls.DOS,cls.TRES,cls.CUATRO,cls.CINCO,cls.SEIS]
        for horario in horarios:        #Recorrer horarios para realizar la comparación
            if(hora==horario.getHora()):    #Si coincide con la hora 
                return horario      #Retorna el horario  en string
        return Horario(None)

    def getHora(self)->str:    
        return self._hora
    def setHora(self,hora):
        self._hora=hora