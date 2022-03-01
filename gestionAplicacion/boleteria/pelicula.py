from tokenize import String
"""
Funcionalidad de la clase: Este contiene anadir la cantidad de Boletos, en este se guardan los atributos de la pelicula 
 entre los que se encuentran nombre, genero, duracion, lenguaje y clasificacion

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa


"""

class Pelicula:
    def __init__(self,nombre="",genero="",duracion=0,lenguaje="",clasificacion=0,  cine= None):
        self._nombre:str = nombre
        self._genero:str = genero
        self._duracion:int = duracion
        self._lenguaje:str = lenguaje
        self._clasificacion:int = int(clasificacion)
        self._cine= cine
        self._cantidadTotalBoletosVendidos:int =0
        self._expectativaVentas:int =0
        cine.agregarPelicula(self)

    def anadirCantidadBoletos(self):
        
        #No recibe nada y tampoco devuelve nada, este metodo se usa para sumar la cantidad de boletos vendidos	
        
        self._cantidadTotalBoletosVendidos+=1   #Sumar 1 al atributo de la cantidad de total de boletos



    ##Getter y setter
    
    def getNombre(self)->str:
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre


    def getGenero(self)->str:
        return self._genero
    def setGenero(self, genero):
        self._genero = genero


    def getDuracion(self)->int:
        return self._duracion
    def setDuracion(self, duracion):
        self._duracion = duracion


    def getLenguaje(self)->str:
        return self._lenguaje
    def setLenguaje(self, lenguaje):
        self._lenguaje = lenguaje


    def getClasificacion(self):
        return self._clasificacion
    def setClasificacion(self, clasificacion):
        self._clasificacion = clasificacion


    def getCine(self):
        return self._cine
    def setCine(self, cine):
        self._cine = cine