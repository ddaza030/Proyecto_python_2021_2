'''
Funcionalidad de la clase: Es la funcion que se presenta de una pelicula respectiva
esta va asociada a una sala en la que se presenta la pelicula y cuenta con una fecha y
horario, esta cuenta con una cantidad de boletos los cuales son los vendidos a los clientes

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa
'''

from code import interact
from hashlib import new
from tkinter import NONE
from xmlrpc.client import Boolean

from gestionAplicacion.boleteria.horario import Horario
from gestionAplicacion.boleteria.boleto import Boleto
from gestionAplicacion.salas.sala import Sala

class Funcion:
    
    def __init__(self,dia,mes,horario,pelicula,sala,cine):
        self._boletos = []  #lista de los boletos correspondientes a las sillas de la sala de la funcion
        self._dia:int = dia
        self._mes:int = mes
        self._horario = horario
        self._pelicula = pelicula
        self.setSala(sala)  #agrega la funcion a sala y a el cine
        self.setCine(cine)
        
        sala.agregarFuncion(self)
        self._numero = len(cine.getCartelera()) +1 #aumenta la cantidad de funciones creadas
        self._cantidadBoletosVendidos:int=0
        cine.agregarFuncion(self)
        self.crearBoleteria()           #Se crea la boleteria de la funcion

    @classmethod
    def crearFuncion(cls,dia:int,mes:int,horario:Horario,pelicula,num_sala:int,cine): #devuelve una funcion o none
        sala = cine.buscarSala(num_sala)
        if(sala!=None): #Si se encuentra ese número de sala en ese cine se verifica disponibilidad
            if(sala.verificarDisponibilidad(dia,mes,horario.getHora())):
                return Funcion(dia,mes,horario,pelicula,sala,cine)  #Se asigna una función a ese cine 
            else:
                return None
        else:
            return None

    @classmethod
    def formatearFunciones(cls,funciones):
        #Recibe unas funciones y procede a organizarlas de forma adecuada para el cliente

        resultado = ""
        for funcion in funciones:
            formato = "{}|{}|{}|{}"
            fecha = "Fecha: " + "{:>02d}/{:>02d}".format(funcion.getDia(),funcion.getMes())
            resultado += str(funcion.getPelicula().getNombre())+" "+str(funcion.getPelicula().getClasificacion())+"+"+"\n"

            resultado += formato.format(funcion.getHorario().getHora().center(6),
                                        ("Sala "+str(funcion.getSala().getNumero())).center(8),
                                        str(funcion.getSala().getTipo()).center(4),
                                        "{:>3d}".format(funcion.getNumero()).center(5))
            resultado +=  "\n" + fecha
            resultado += "\n\n"
        return resultado

    def crearBoleteria(self):
        #Se crea la boletería de las sillas de una sala

        sillas = self._sala.getSillas()     #lista de las sillas de la sala correspondiente
        disponibles:int=self._sala.cantidadSillas() #ignorar, catidadSillas() se encuentra en cada subclase, por lo que acá marca el error
        total:int=len(self._sala.getSillas())
        for i in range(total):
            if(disponibles>0):
                boleto:Boleto= Boleto(self,sillas[i])       #si es mayor que 0 crea el boleto, lo anade a la lista boletos y disponibles-
                self._boletos.append(boleto)
                disponibles-=1
    
    def verDisponibilidad(self):
        # En este caso la funcion devuelve una lista de strings, para agregar cada strings
        total =[]   #lista de filas

        #for para hacer una lista de listas, cada lista corresponde a una fila de boletos
        for boleto in self._boletos:
            if boleto!=None:                                #si el boleto no es nulo, crea el string y se anade a la fila
                tupla_boleto:tuple=(boleto.isDisponibilidad(),boleto.tipoString()+str(boleto.getNum_silla()))       #se crea un string de la forma disponibilidad/tipo/numerosilla
                total.append(tupla_boleto)

        return total

    def VentaBoleto(self,boleto,cliente)->bool:
        #Retorna un booleano aumenta las ganancias del cine y añade a cantidad de boletos vendidos de la pelicula

        if (boleto.isDisponibilidad()==True and cliente.getEdad()>=self.getPelicula().getClasificacion()):
            boleto.setDisponibilidad(False) #Cuando se vende cambia la disponibilidad del boleto a false
            cliente.getHistorialCompras().append(boleto)    #Se añade al historial de compra del cliente 
            self._cantidadBoletosVendidos+=1        #Se suma uno al atributo cantidadBoletosVendidos
            boleto.calcularPrecioDefinitivo(cliente)    #Se mira si el cliente posee un descuento para aplicar

            ganancia:float=self._cine.getDineroGanado()+boleto.getPrecioTotal()

            self._cine.setDineroGanado(ganancia)
            self._pelicula.anadirCantidadBoletos()

            return True
        else:
            return False


        
#Getter y Setter

    def getDia(self):
        return self._dia
    def setDia(self, dia):
        self._dia = dia


    def getMes(self):
        return self._mes
    def setMes(self, mes):
        self._mes = mes


    def getHorario(self):
        return self._horario
    def setHorario(self, horario):
        self._horario = horario


    def getPelicula(self):
        return self._pelicula
    def setPelicula(self, pelicula):
        self._pelicula = pelicula


    def getSala(self):
        return self._sala
    def setSala(self, sala):
        self._sala = sala


    def getBoletos(self):
        return self._boletos
    def setBoletos(self, boletos):
        self._boletos = boletos


    def getCantidadBoletosVendidos(self):
        return self._cantidadBoletosVendidos
    def setCantidadBoletosVendidos(self, cantidadBoletosVendidos):
        self._cantidadBoletosVendidos = cantidadBoletosVendidos


    def getCine(self):
        return self._cine
    def setCine(self, cine):
        self._cine = cine


    def getCantidadfunciones(self):
        return self._cantidadFunciones
    def setCantidadfunciones(self, cantidadFunciones):
        self._cantidadFunciones = cantidadFunciones


    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero