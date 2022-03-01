# Funcionalidad de la clase: En este se podra verificar las disponibilidades de la sala, agregar funciones y ver horarios disponibles 

#Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa

from sys import int_info

from gestionAplicacion.salas.agregar import Agregar



class Sala(Agregar):


    def __init__(self,filas,columnas,filasvip,precio,cine):
        self._numero = len(cine.getSalas())+1
        self._sillas = []       #contiene objetos silla que corresponden a las sillas de la sala esta depende de las filas y las columnas
        self._funciones = []    #contiene las funciones creadas en dicho cine

        self._filas : int = filas
        self._columnas : int = columnas
        self._filasvip : int = filasvip
        self._precio : float = precio
        self._cine = cine

        self.crearSilleteria()
        cine.agregarSala(self)

        

    #
    #Metodos
    #


    def agregarFuncion(self, funcion):
        '''
        Recibe como parametro la funcion que se agregará a la lista de funciones y no retorna nada
        '''
        self._funciones.append(funcion) #se agrega la funcion a la lista de funciones

    def cantidadSillas(self):
        pass

    def crearSilleteria(self):
        pass

    def verificarDisponibilidad(self, *args) -> bool:
        #sobrecarga de metodos chambona 
        '''Puede recibir varias variables para verificar si la sala esta disponible para 
	    programar una funcion en la fecha dada, devuelve verdadero si cuenta con
	    disponibilidad de lo contrario devuelve falso'''

        if(len(args) == 3):

            dia, mes, hora = args

            consulta: str = str(dia)+"/"+str(mes)+"/"+str(hora) #se crea un string con el dia mes y horario

            fechasfunciones: list[str] = [] #Lista que se usara para guardar las fechas de todas las funcones dadas

            for func in self._funciones:
                info: str = str(func.getDia())+"/"+str(func.getMes())+"/"+str(func.getHorario())
                fechasfunciones.append(info)                #Se crea el string de la fecha de la funcion y se añade las fechas 
                
                info = ""                                   #se resetea el string 

            for i in fechasfunciones:
                if ( i == consulta):                #si el strings igual a la fecha dada por la entrada
                    return False                    #La sala esta ocupada en dicha fecha
            
            return True         #Esta libre
        
        
        elif(len(args) == 2):

            dia, mes = args
            
	
            consulta : str = ""+str(dia)+str(mes);					
            
            fechas: list[str] = []	    #lista para guardar las fechas de todas las funciones dadas en dicha sala

            horarios: list[str] = []    #lista que guarda los horarios en los cuales la sala tiene funcion dicho dia

            
            disponibles: list[str]= ["12:00","14:00","16:00","18:00","20:00","22:00"]   #lista con todos los horarios, a la cual se le restara los horarios disponibles
            
            for func in self._funciones:

                info : str=""+str(func.getDia())+str(func.getMes())		#se crea el string de la fecha de la funcion
                fechas.append(info)								        #y se añade a fechasfunciones
                info=""								                    #se resetea el strin
                
            
            
            for i in range(len(fechas)):
                if (fechas[i] == consulta):				               #si la fecha de las funciones que hay coincide con la fecha y hora de consulta
                    horarios.append(str(self._funciones[i].getHorario().getHora()))     #se almacena
                
            
            
            for horario in horarios:
                disponibles.remove(horario);		#se quita de los horarios disponibles, los que ya estan ocupados en ese dia de ese mes
            
            
            respuesta=""
            
            for d in disponibles:
                respuesta+=d+"\n"       #se hace un string que devuelve los horarios disponibles
            
            
            return respuesta == "12:00\n14:00\n16:00\n18:00\n20:00\n22:00\n"    #devuelve un valor de verdad si todos los horarios estan disponibles
        
        return False
    
    def verHorarios(self,dia,mes):
        '''Recibe un dia y un mes como una fecha y devuelve un String que contiene los horarios disponibles
	        para dicho dia'''
        consulta=""+str(dia)+str(mes)       #String de la fecha
        fechas=[]   #Lista para guardar las fechas de todas las funciones dadas en dicha sala
        horarios=[] # Lista para guardar los horarios en los cuales la sala tiene la funcion de dicho dia 
        disponibles=["12:00","14:00","16:00","18:00","20:00","22:00"]   #Lista de todos los horarios 

        for funcion in self._funciones:
            info=""+str(funcion.getDia())+str(funcion.getMes())     #Almacenar funcion en string
            fechas.append(info)
        
        for i in range (len(fechas)):                   #Si la fecha de las funciones coincide con la fecha y hora de la consulta, se almacena
            if fechas[i]==consulta:
                horarios.append(self._funciones[i].getHorario().getHora())
        
        for horario in horarios:
            disponibles.remove(horario)        # Se quita los horarios disponibles
        
        respuesta=""
    
        for d in disponibles:                   #String con los horarios disponibles 
            respuesta+=d+"\n"
        
        return respuesta

    
    def almenosUnoDisponible(self, dia: int, mes: int) ->  bool:
        """
        recibe dia y mes devueve un boolean diciendo si la sala tiene almenos un horario disponible
	    dicha fecha o no
        """
        consulta: str   =   ""  + str(dia) + str(mes)			#crea un estring con la fecha
        
        fechas : list[str] = []	    #lista para guardar las fechas de todas las funciones dadas en dicha sala
        
        horarios: list[str] = []    #lista que guarda los horarios en los cuales la sala tiene funcion dicho dia
        
        disponibles: list[str] = ["12:00","14:00","16:00","18:00","20:00","22:00"];		#lista con todos los horarios, a la cual se le restara	los horarios disponibles
        
        for func in self._funciones:
            info : str =""+str(func.getDia())+str(func.getMes())	    #del atributo funcion se almacenan en modo string el dia y mes de las funciones
            fechas.append(info)							
            info = ""								
            
        for i in range(len(fechas)):
            if (fechas[i] == consulta):     #si la fecha de las funciones que hay coincide con la fecha y hora de consulta
                horarios.append(str(self._funciones[i].getHorario().getHora()))     #se almacena
                
        for horario in horarios:
            disponibles.remove(horario)     #se quita de los horarios disponibles, los que ya estan ocupados en ese dia de ese mes
            
        respuesta : str =""
        
        for d in disponibles:
            respuesta+=d+"\n"       #se hace un string que devuelve los horarios disponibles
            
        if(len(respuesta) >= 5):    #si el string contiene por lo menos un horario devuelve true
            return True
        else:
            return False
		
	

#Getting y setting


    def getNumero(self):
        return self._numero
    def setNumero(self, numero):
        self._numero = numero


    def getFilas(self):
        return self._filas
    def setFilas(self, filas):
        self._filas = filas

    def getColumnas(self):
        return self._columnas
    def setColumnas(self, columnas):
        self._columnas = columnas


    def getFilasvip(self):
        return self._filasvip
    def setFilasvip(self, filasvip):
        self._filasvip = filasvip


    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio = precio


    def getCine(self):
        return self._cine
    def setCine(self, cine):
        self._cine = cine


    def getSillas(self):
        return self._sillas
    def setSillas(self, sillas):
        self._sillas = sillas


    def getFunciones(self):
        return self._funciones
    def setFunciones(self, funciones):
        self._funciones = funciones