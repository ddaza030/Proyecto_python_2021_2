##Funcionalidad de la clase: Albergar los datos de una silla respectiva a una sala de una funcion 


##Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa

from gestionAplicacion.salas.tipo import Tipo


class Boleto:

    def __init__(self, funcion, silla):
        
        self._disponibilidad : bool= True
        self._funcion = funcion
        self._num_silla = 0
        self._precio_silla = 0
        self.setAtr_silla(silla)
        self._precioTotal =  self.calcularPrecio()
        
    # Funciones

    def calcularPrecio(self) -> float:
        ''' No recibe nada y devuelve un float el cual corresponde al calculo del precio bruto del boleto 
	    el cual depende del precio de la sala y el precio de la silla '''

        bruto: float = self._funcion.getSala().getPrecio()+self._precio_silla   #Se suma el precio de la sala y el precio de la silla
        return bruto

    def calcularPrecioDefinitivo(self, cliente):

        #Recibe a un cliente  y no devuelve nada, este precio se le descuenta un descuento(Si este cliente lo tiene)
        
        total: float = self.calcularPrecio()-(self.calcularPrecio()*(cliente.getDescuento())) #Al precio bruto le resta el descuento del cliente si este lo posee
        self.setPrecioTotal(total)  # Se establece el resultado de la linea anterior al atributo PrecioTotal

    def setAtr_silla(self, silla):

        '''Recibe la silla con la que deseo asignarle los atributos de numero,tipo de silla y precio de silla  y no devuelve nada	
        '''
        self._num_silla = silla.getNumero()     #Se establece al atributo de num_silla  el numero de la silla que recibe
        self.setTipo_silla(silla.getTipo())     # Se establece al atributo tipo_silla el tipo de la silla que recibe 
        self.setPrecio_silla(silla.getPrecio()) # Se establece al atributo precio_silla el precio de la silla que recibe

    def tipoString(self) -> str:
        '''
        No recibe nada  y  devuelve un String el cual indica si el tipo de la silla al cual esta relacionado el boleto
        '''
        if(self._tipo_silla == Tipo.VIP):
            return "V-" #El tipo de la silla es VIP retornara V-
        return "S-"     # En caso de que sea sencilla retornara S-
    # 
    # getter and setters
    # 
    def getNum_silla(self):
        return self._num_silla
    def setNum_silla(self, num_silla):
        self._num_silla = num_silla


    def getTipo_silla(self):
        return self._tipo_silla
    def setTipo_silla(self, tipo_silla):
        self._tipo_silla = tipo_silla


    def getPrecioTotal(self):
        return self._precioTotal
    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal


    def isDisponibilidad(self):
        return self._disponibilidad
    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad


    def getFuncion(self):
        return self._funcion
    def setFuncion(self, funcion):
        self._funcion = funcion

    def getPrecio_silla(self):
        return self._precio_silla
    def setPrecio_silla(self, precio_silla):
        self._precio_silla = precio_silla