"""
Funcionalidad de la clase: Albergar las salas, funciones, peliculas, clientes y metodos para
    la creacion , modificacion y observacion de los clientes, peliculas y funciones

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa


"""

import random

from gestionAplicacion.boleteria.funcion import Funcion
from gestionAplicacion.boleteria.pelicula import Pelicula
from gestionAplicacion.boleteria.horario import Horario
from gestionAplicacion.boleteria.boleto import Boleto
from gestionAplicacion.salas.sala import Sala
from gestionAplicacion.cinemas.cliente import Cliente


class Cine: 

    def __init__(self,nombre):
        self._nombre = nombre
        self._clientes = []
        self._cartelera = []
        self._peliculas = []
        self._salas= []
        self._dineroGanado= 0
        self._DESCUENTOMVC = 0.2



    def programarFuncionesAuto( self, mes: int, dia: int, sala: Sala):
        '''
        Recibe los parametros mes, dia y sala, devuelve una lista de funciones. Su proposito es recibir un dia, un mes y una sala para 
		 programar de forma automatica en esa sala, para todos los horarios disponibles de acuerdo al numero de peliculas con mayor 
		 cantidad de boletos vendidos, una funcion para ese dia.
        '''
        
        programadas  = []
        funciones : list = self.verFuncion(mes) #realizo una lista de las funciones dadas ese mes
        peliculasMes : list = list(set([funcion.getPelicula() for funcion in funciones]))
        pelicula_boletos = []                          # lista que obtiene las peliculas por la cantidad de boletos vendidos por esta pelicula dicho mes
        disponibles = ["22:00","20:00","18:00","16:00","14:00","12:00"]

        for i in range(len(peliculasMes)):
            pelicula_boletos.append([peliculasMes,0])
            for funcion in funciones:                          # se recorren las funciones de dicho mes para hacer cuenta de cuantas boletas ha vendido la pelicula i
                if(peliculasMes[i] == funcion.getPelicula()):
                    pelicula_boletos[i][1]+= funcion.getCantidadBoletosVendidos()       # se suman la cantidad de boletos
                   
        pelicula_boletos.sort(key = lambda x:x[1], reverse = True)
		
        if(len(peliculasMes)>=6):       #Se revisa que hacer para cuando la cantidad de peliculas es menor a la cantidad de horarios disponibles
            for i in range(6):
                p : Pelicula = peliculasMes[i]
                h : Horario = Horario.getHorario(disponibles[i])
                programadas.append( Funcion.crearFuncion(dia, mes, h, p , sala.getNumero(), self))
        else:
            for i in range(len(peliculasMes)):
                p : Pelicula = peliculasMes[i]
                h : Horario = Horario.getHorario(disponibles[i])
                programadas.append(Funcion.crearFuncion(dia, mes, h, p , sala.getNumero(), self))
        
        return programadas



           
    
    def salasDisponibles(self, mes: int, dia: int):
        #Recibe un mes y un dia y retorna una lista de salas que tengan al menos un horario disponible ese dia

        disponibles=list()
        
        for sala in self._salas:
            if sala.almenosUnoDisponible(mes, dia):
                disponibles.append(sala)
        
        return disponibles

    def mostValueClient(self) -> str:
        '''
        No recibe nada y retorna una String con el nombre del cliente mas fiel al que le fue
		 aplicado el descuento. Su proposito es calcular el cliente que más compras ha hecho
		 para dar un descuento del 0.2.
        '''
        clienteList=list()
        
        for client in self._clientes:
            clienteList.append(len(client.getHistorialCompras()))   #Recorre el historial de compras del cliente y anexa el tamano de su historial de compra
        
        valormax=max(clienteList)   #Se establece el mayor numero de boletos comprados por parte de un cliente

        for client in self._clientes:
            if(valormax==len(client.getHistorialCompras())):    #Si la cantidad de boletos comprados es igual a valor max conseguir el nombre de este
                client.setDescuento(self._DESCUENTOMVC)
                return client.getNombre()

        return "Se ha aplicado el descuentos  a nuestro cliente mas fiel "


    def verFuncion(self, *args) -> list:
        funciones: list = []

        # Este es el ver funcion que recibe pelicula, dia, mes
        
        if(len(args) == 3):
            pelicula: Pelicula = args[0]
            dia, mes = args[1:]

            for funcion in self.getCartelera():
                if(funcion.getPelicula() == pelicula and funcion.getDia() >= dia and funcion.getMes() == mes):
                    funciones.append(funcion)
            for funcion in self.getCartelera():
                if(funcion.getPelicula() == pelicula and funcion.getMes() > mes):
                    funciones.append(funcion)

        # Este es el que recibe dia, mes
        elif(len(args) == 2):
            dia, mes = args
            for funcion in self.getCartelera():
                if(funcion.getDia() == dia and funcion.getMes() == mes):
                    funciones.append(funcion)

        elif(len(args) == 1):

            #recibe mes
            if(type(args[0]) == int):
                mes = args[0]
                for funcion in self.getCartelera():
                    if(funcion.getMes() == mes):
                        funciones.append(funcion)
                        
            #recibe cliente 
            else:
                cliente: Cliente = args[0]
                for funcion in self.getCartelera():
                   if(funcion.getPelicula().getGenero() == cliente.mostWatchedGenre()):
                       funciones.append(funcion)
            

        return funciones


    #Al 10 por ciento de los clientes mas fieles aplicarle un 10% de descuento a cada uno de ellos 

    def clientesValiosos(self)-> list:
        '''
        Recibe nada y retorna una List des objetos tipo Cliente. Su proposito es calcular
	    de entre la lista de clientes el 0.1 que tiene mayor cantidad de compras en historialCompras
        '''    
        clienteList=[]		#Aca estaran los tamanos de historial de compra de cada cliente
        
        for cliente in self._clientes:
            clienteList.append(len(cliente.getHistorialCompras())) 	#Recorre el historial de compras del cliente y anexa el tamano de su historial de compra
        
        cantidad= len(clienteList)				#Cantidad de clientes que se tiene
        
        clienteList.sort(reverse=True)		#Ordenar la lista de mayor a menor
        top10= round(cantidad/10)								# El 10% de los clientes 
        mejoresCompas=[]			                                    #Clientes mas fieles
        
        for i in range(0, top10) :					
            valor =clienteList[i]								#Conseguir el 10% de los tamanos de historial de compra mas grandes
            for client in self._clientes:
                
                if(len(client.getHistorialCompras())==valor):				#Si el tamano de historial de compra es igual al valor agregar a los mejores clientes (mejoresCompas)
                    if not client in mejoresCompas:
                        mejoresCompas.append(client)
        
        return mejoresCompas


    def verificarCliente(self, num: int) -> bool:
        '''
        Recibe un numero de cedula, retorna un boolean. Su proposito es verificar
		que un cliente este en la lista de clientes de acuerdo a su numero de cedula
        '''

        lista : list = []   #Lista de cédulas
        
        for cliente in self.getClientes():
            lista.append(cliente.getCedula())
        
        return num in lista
    
    
    
    def rifarBoleto(self, numeroFuncion: int):
        '''
        Recibe el numero de la funcion que se va a rifar y retorna un String con el ganador. 
		Su proposito es de entre los clientes valiosos, rifar un boleto a una funcion deseada
        '''
        top10: list= self.clientesValiosos();	#Saco la lista del 10% de los clientes mas fieles
        
        tamano: int= len(top10)			#tamano de esa lista
        
        ganador: int= random.randint(0,tamano-1)	#Un numero aleatorio entre 0 y el tamano de la lista
        
        panitaGanador: Cliente= top10[ganador]  #Con el numero conseguido sacar al cliente escogido

        aleatoriofuncion: int = random.randint(0,len(self._cartelera)-1)	#Numero aleatorio de la lista de cartelera
        
        fescogida: Funcion  = self.BuscadorFuncion(numeroFuncion)	#Funcion escogida de la cartelera con el numero de la funcion
        
        aleatorioboleto: int  = random.randint(0,fescogida.getSala().cantidadSillas()-1)	#Otro numero aleatorio con base al tamano de la lista de boletos
        
        bescogido: Boleto = fescogida.getBoletos()[aleatorioboleto]	#Boleto escogido con el numero aleatorio
        
        if(bescogido.isDisponibilidad()):	#Si este boleto esta disponible se puede rifar ese boleto al cliente ganador
            
            fescogida.VentaBoleto(bescogido,panitaGanador)
            fescogida.setCantidadBoletosVendidos(fescogida.getCantidadBoletosVendidos()-1)		# Cada vez que se aplica la venta de boletos se suma al atributo, como se esta rifando
														# Se tendria que anular esa suma
        else:
			#Se puede ser muy demalas y que se escoja aleatoriamente un boleto que ya esta comprado
            
            for boleto in fescogida.getBoletos():
                if (boleto.isDisponibilidad()):	    #Se va recorriendo los boletos de la funcion escogida aleatoriamente 
                                                    #hasta encontrar el primero disponible 
                    
                    fescogida.VentaBoleto(boleto, panitaGanador)	#Se vende el boleto
                    fescogida.setCantidadBoletosVendidos(fescogida.getCantidadBoletosVendidos()-1)
                    break;		#Solo voy a rifar uno entonces rompo el for
                    
        return panitaGanador.getNombre()

    def buscadorCliente(self, num : int):
        '''
        Recibe un numero de cedula, retorna un objeto de clase Cliente. Su proposito es retornar el
		cliente cuyo numero de cedula concuerde con el ingresado al metodo
        '''

        lista = self.getClientes()
        for cliente in lista:
            if (int(cliente._cedula)== int(num)):
                return cliente
        return None

    def buscarSala(self, num):
        '''
        Recibe el numero de una sala, retorna un objeto de clase Sala. Su proposito es retornar la
		sala cuyo numero coincida con el numero ingresado
        '''
        lista = self.getSalas()
        for sala in lista:
            if (int(sala.getNumero())== int(num)):
                return sala
        return None

    
    def BuscadorPelicula(self, nombre):
        '''
        Recibe el nombre de una pelicula, retorna un objeto de clase Pelicula. Su proposito es retornar la
		pelicula cuyo nombre coincida con el nombre ingresado
        '''
        lista = self.getPeliculas()
        for pelicula in lista:
            if (str(pelicula.getNombre())==nombre):
                return pelicula
        return None



    def BuscadorFuncion(self,numero):
        '''
        Recibe un numero de funcion, retorna un objeto de clase Funcion. Su propósito es retornar la
		funcion cuyo numero de cedula concuerde con el ingresado al metodo
        '''
        lista=[]
        for funcion in self._cartelera:
            lista.append(funcion.getNumero())

            if funcion.getNumero()==int(numero):    #Si el numero de la funcion es igual al numero que se ingreso es la que se estaba buscando
                return funcion
        return None

    def BuscadorBoleto (self,num_silla: int,funcion:Funcion):
        '''
        Recibe un numero de silla y una funcion, retorna un objeto de clase Boleto. Su proposito es retornar el
		boleto cuyo numero de silla asociado a una funcion ingresada concuerde con el ingresado.
        '''
        lista=[]
        for boleto in funcion.getBoletos():
            lista.append(boleto.getNum_silla())

            if boleto.getNum_silla==num_silla:  #Si el numero que se ingreso concuerda con el numero de la silla del boleto es el que se estaba buscando
                return boleto
        return None

        
                
	#Metodos para agregar elementos a las listas de la clase Cine

    def agregarCliente(self,nuevo: Cliente):
       self._clientes.append(nuevo)

    def agregarPelicula(self,nuevo: Pelicula):
        self._peliculas.append(nuevo)

    def agregarSala(self,nuevo: Sala):
        self._salas.append(nuevo)

    def agregarFuncion(self,nuevo:Funcion):
        self._cartelera.append(nuevo)     


	
    #
    #Getting and setting
    #



    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getClientes(self):
        return self._clientes
    def setClientes(self, clientes):
        self._clientes = clientes


    def getCartelera(self):
      return self._cartelera
    def setCartelera(self, cartelera):
      self._cartelera = cartelera


    def getPeliculas(self):
     return self._peliculas
    def setPeliculas(self, peliculas):
        self._peliculas = peliculas


    def getSalas(self):
        return self._salas
    def setSalas(self, salas):
        self._salas = salas


    def getDineroGanado(self):
        return self._dineroGanado
    def setDineroGanado(self, dineroGanado):
        self._dineroGanado = dineroGanado


    def getDescuentomvc(self):
        return self._DESCUENTOMVC
    def setDescuentomvc(self, DESCUENTOMVC):
        self._DESCUENTOMVC = DESCUENTOMVC