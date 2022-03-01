"""Funcionalidad de la clase: En esta clase esta lo del frame principal de la ventana
    en donde se mostraran los procesos principales de la aplicacion, donde se pediran los datos
    y en donde están los botones que permiten enviar la informacion


Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa
"""




from dataclasses import field
from textwrap import fill
from tkinter import *
from tkinter import messagebox
from uimain.user.excepciones.notchair import NotChair
from uimain.user.zonaa import ZonaA
from gestionAplicacion.cinemas.cine import Cine
from gestionAplicacion.boleteria.pelicula import Pelicula
from gestionAplicacion.boleteria.funcion import Funcion
from uimain.user.fieldFrame import FieldFrame
from gestionAplicacion.salas.sala2D import Sala2D
from gestionAplicacion.salas.sala3D import Sala3D
from uimain.user.fieldFrame import FieldFrame
import uimain.user.venta as venta
from gestionAplicacion.boleteria.horario import Horario
from uimain.user.excepciones.notin import NotIn
from uimain.user.excepciones.notipo import NoTipo
from uimain.user.excepciones.rangonoper import RangoNoPer
from uimain.user.excepciones.nodisp import NoDisp

class ZonaB: 
   
    def __init__(self, user,cine):
        
        self.cine=cine
        self.todo = Frame(user,  bg = "#FAFAD2") #Este es lo que contiene toda la zona 2
        self.todo.pack(fill=X)

        self.funciones = {"Venta":self.venta,
                         "Agregar Pelicula":self.agregarPelicula,
                         "Quitar Pelicula":self.quitarPelicula, 
                         "Agregar Funcion":self.agregarFuncion,
                         "Generar Funcion Auto":self.agregarAuto,
                         "Rifar Boleto":self.rifa,
                         "Agregar Sala":self.agregarSala} #aca se guardan las los procesos y las consultas

        self.titulo_texto = Frame(self.todo)   
        self.titulo_texto.pack()

        self.titulo = Label(self.titulo_texto,font=('Microsoft Himalaya', 32), bg="#FAFAD2",text = "¡Bienvenido a la ventana de usuario!")  #label del titulo
        self.titulo.pack(fill=X)

        self.texto = Label(self.titulo_texto,font=('Microsoft Himalaya', 24 ), bg = "#FAFAD2",text = "Por favor selecciona una opción del menú para continuar")   #label del titulo
        self.texto.pack(fill=X)



        self.cuerpo = Frame(self.todo,width=800, height = 350, bg= "#FAFAD2") #este es el cuerpo, se inicializa vacio
        self.cuerpo.pack(fill=X)
        
    #Metodo para devolverse a la ventana inicial de usuario
    def cambiar(self):
        self.cuerpo.pack_forget()
        self.cuerpo = Frame(self.todo,width=800, height = 350, bg= "#FAFAD2")

        self.titulo.configure(text = "Cine Bahía")
        self.texto.configure(text = "Bienvendio al cine, seleccione lo que quiera hacer")

        self.cuerpo.pack()

    ## Procesos y consultas

    #Metodo para la ejecucion de lo respectivo a la venta de boletos
    def venta(self):
        self.cambiar()
        self.titulo.configure(text = "Venta")
        self.texto.configure(text = "Permite vender buscando por diferentes peliculas")
        venta.ventana(self, self.cuerpo, self.cine)         #Se llama a la clase venta pasandole frame y cine como argumentos
       
    #Metodo para agregar pelicula
    def agregarPelicula(self):

        self.cambiar()

        self.titulo.configure(text = "Agregar Pelicula")
        self.texto.configure(text = "Permite agregar películas a la base de datos")

        nomCriterios="Pelicula"
        criterios=["Nombre","Genero","Duración","Idioma","Edad mínima"]
        nomValores="Información"
        valIniciales=None
        valHabilitados=None     #Los valores son editables
        agregarPelicula = FieldFrame(nomCriterios, criterios,nomValores,valIniciales,valHabilitados,self.cuerpo)
        
        agregarPelicula.pack()

        #Metodo para crear un objeto de tipo pelicula
        def addPeli(action):
            pelicula=Pelicula(agregarPelicula.getValue("Nombre"),
                agregarPelicula.getValue("Genero"),
                int(agregarPelicula.getValue("Duración")),
                agregarPelicula.getValue("Idioma"),
                int(agregarPelicula.getValue("Edad mínima")),
                self.cine) 
            
            
            try:

                [int(i)/0 for i in agregarPelicula.getValue("Genero") if i in list("123456789")]        #Se verifica que el genero y el idioma no tengan numero en lo ingresado
                [int(i)/0 for i in agregarPelicula.getValue("Idioma") if i in list("123456789")]        #para lo cual si está en la lista se genera un error y se llama la excepcion
                int(agregarPelicula.getValue("Duración"))
                int(agregarPelicula.getValue("Edad mínima"))
            except:
                raise NoTipo
            

            
            self.cambiar()      #Se devuelva a la ventana inicial
            messagebox.showinfo(title="Información",message="Pelicula creada con éxito")     #Se muestra un messagebox al crear la pelicula

        agregarPelicula.button.bind('<ButtonRelease>',addPeli)      #Se liga el boton con el metodo para crear las peliculas

        
    #Metodo para quitar una pelicula de las que están disponibles en el cine
    def quitarPelicula(self):
        
        
        self.cambiar()

        self.titulo.configure(text = "Quitar pelicula")
        self.texto.configure(text = "Permite quitar películas de la base de datos")

        nomCriterios="Pelicula"
        criterios=["Nombre"]
        nomValores="Información"
        valIniciales=None
        valHabilitados=None     #Los valores son editables
        quitarPelicula = FieldFrame(nomCriterios, criterios,nomValores,valIniciales,valHabilitados,self.cuerpo)
        
        quitarPelicula.pack()

        def removePeli(action):
            titles=[i.getNombre() for i in self.cine.getPeliculas()]        #Se hace una lista con las peliculas que hay en el cine
            try:
                self.cine.getPeliculas().pop(titles.index(quitarPelicula.getValue("Nombre")))       #Si no se puede quitar el nombre ingresado es porque no está en el cine entonces
            except:                                                                                 #Se lanza la excepción
                raise NotIn()

            
            self.cambiar()  #Se devuelve a la ventana principal
            messagebox.showinfo(title="Información",message="Pelicula eliminada del cine con éxito!")   #Se muestra un messagebox al crear la pelicula

        quitarPelicula.button.bind('<ButtonRelease>',removePeli)    #Se liga el boton al metodo que elimina la pelicula

        peliculasdisponibles = "Peliculas disponibles en el cine:\n"
        for p in self.cine.getPeliculas():
            peliculasdisponibles += p.getNombre() + "\n"        #Se muestran los nombres de las peliculas disponibles para que se sepa cuales son las que existen

        disponibles=Label(self.cuerpo,text=peliculasdisponibles)
        disponibles.pack()



    #Metodo para agregar una funcion manualmente ingresando los valores requeridos
    def agregarFuncion(self):
        self.cambiar()

        self.titulo.configure(text = "Agregar función")
        self.texto.configure(text = "Permite agregar funciones")

        nomValores="Información"
        valIniciales=None
        valHabilitados=None
        diames = FieldFrame("Fecha", ["Dia","Mes"],nomValores,valIniciales,valHabilitados,self.cuerpo)      #Primero se pide el día y el mes
        diames.pack()
        diames.button.configure(text="Siguiente")

        info=[]      #[0]=dia, [1]=mes, [2]=sala, [3]=hora, [4]=pelicula


        def salasdia(action):       ##Aca se muestran las salas disponibles segun el dia y mes seleccionado
            info.append(diames.getValue("Dia"))
            info.append(diames.getValue("Mes"))
            
            
            try:
                int(info[0])        #Se verifica que lo ingresado en dia y mes si sean enteros
                int(info[1])
            except:
                info.pop()          #Se eliminan para que los vuelva a ingresar si no son y se lanza la excepcion
                info.pop()
                raise NoTipo()

            try:
                [i for i in range(1, 13)].index(int(info[1]))       #Se verifica que sea un mes valido, sino se lanza la excepcion
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            try:
                [i for i in range(1, 32)].index(int(info[0]))       #Se verifica que sea un dia valido, sino se lanza la excepcion
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            
            diames.pack_forget()        #se elimina el fielfframe para pedir el dia y el mes

            salasdispo=FieldFrame("Sala",["Numero"],nomValores,valIniciales,valHabilitados,self.cuerpo)     #Se crea un fieldframe para pedir la sala
            salasdispo.pack()
            salasdispo.button.configure(text="Siguente")

            def horariosala(action):        ##Aca se muestran los horarios disponibles de la sala escogida en la fecha escogida
                info.append(salasdispo.getValue("Numero"))

                try:
                    disp = self.cine.salasDisponibles(int(info[0]), int(info[1])).copy()        #se hace una lista de las salas disponibles
                    disp.remove(self.cine.buscarSala(int(info[2])))         #si no se puede quitar es que no está disponible y se lanza la excepción
                except:
                    info.pop()
                    raise NotIn()

                salasdispo.pack_forget()        #Se elimina el fieldframe para pedir las salas
                disponibles.pack_forget()       #Se elimina el label que muestra las salas disponibles

                horariodispo=FieldFrame("Horarios",["Hora"],nomValores,valIniciales,valHabilitados,self.cuerpo)     #Se hace un fieldframe para pedir el horario para la funcion
                horariodispo.pack()
                horariodispo.button.configure(text="Siguiente")

                #print(self.cine.buscarSala(int(info[2])))

                horarioslibres=self.cine.buscarSala(int(info[2])).verHorarios(int(info[0]),int(info[1]))        #Se almacenan los horarios libres de la sala
                
                disponibles.configure(text="Horarios disponibles de la sala " + str(info[2])+":" + "\n"+horarioslibres)     #Se muestran los horarios disponibles
                disponibles.pack()

                def peliscine(action):        ###Peliculas disponibles en el cine
                    info.append(horariodispo.getValue("Hora"))

                    try:
                        if info[3] not in self.cine.buscarSala(int(info[2])).verHorarios(int(info[0]),int(info[1])):        #Si el horario seleccionado no está entre los disponibles, se genera un error y se lanza la excepcion
                            x=1/0
                    except:
                        info.pop()
                        raise NotIn()

                    horariodispo.pack_forget()          #Se elimina el fieldframe para las horas disponibles
                    disponibles.pack_forget()           #Se elimina el label con los horarios disponibles

                    pelisdispo=FieldFrame("Titulo",["Pelicula"],nomValores,valIniciales,valHabilitados,self.cuerpo)     #Se hace un fieldframe para pedir el nombre de la pelicula para la funcion
                    pelisdispo.pack()
                    pelisdispo.button.configure(text="Finalizar creacion")
                    
                    peliculasdisponibles=""
                    for p in self.cine.getPeliculas():              #Se almacenan las peliculas disponibles en el cine
                        peliculasdisponibles+=p.getNombre()+"\n"

                    disponibles.configure(text=peliculasdisponibles)        #Se muestran
                    disponibles.pack()

                    def creacionfinal(action):
                        info.append(pelisdispo.getValue("Pelicula"))
                        titles = [i.getNombre() for i in self.cine.getPeliculas()]      #Se hace una lista con las peliculas del cine
                        try:
                            self.cine.getPeliculas().copy().pop(titles.index(pelisdispo.getValue("Pelicula")))      #Se mira si se puede quitar de la lista de disponibles, sino se lanza la excepcion
                        except:
                            raise NotIn()
                        a = self.cine.BuscadorPelicula(info[4])
                        Funcion.crearFuncion(int(info[0]),int(info[1]),Horario.getHorario(info[3]), self.cine.BuscadorPelicula(info[4]), self.cine.buscarSala(int(info[2])).getNumero(),self.cine)      #Se llama al metodo de crear funcion


                        self.cambiar()      #Se devuelve a la principal
                        messagebox.showinfo(title="Información",message="Funcion creada con éxito!")    #Se muestra un mensaje cuando se completó la transacción

                    pelisdispo.button.bind("<ButtonRelease>", creacionfinal)       #Cuarto boton

                horariodispo.button.bind("<ButtonRelease>",peliscine)      ##Tercer boton

            salasdispo.button.bind("<ButtonRelease>",horariosala)       #Segundo boton

            salaslibres=self.cine.salasDisponibles(int(diames.getValue("Dia")),int(diames.getValue("Mes")))         #Se guardan las salas disponibles
            textosalas="Salas disponibles del dia/mes "+str(diames.getValue("Dia"))+"/"+str(diames.getValue("Mes"))+" :\n"
            for d in salaslibres:
                textosalas+="Sala "+str(d.getNumero())+"\n"     #Se almacenan en un string

            disponibles=Label(self.cuerpo,text=textosalas)      #Se muestran
            disponibles.pack()

        diames.button.bind("<ButtonRelease>",salasdia)      ###Primer boton





    #Metodo para añadir una funcion automaticamente
    def agregarAuto(self):
        self.cambiar()

        self.titulo.configure(text="Programación automática")
        self.texto.configure(text = "Permite agregar funciones de un día en una sala")

        
        nomValores="Información"
        valIniciales=None
        valHabilitados=None

        diames = FieldFrame("Fecha", ["Dia","Mes"],nomValores,valIniciales,valHabilitados,self.cuerpo)      #Se hace un fieldframe para pedir el dia y el mes
        diames.button.configure(text="Siguiente")
        diames.pack()
        

        info=[]

        def salasDisponibles(action):
            info.append(diames.getValue("Dia"))
            info.append(diames.getValue("Mes"))

            try:                #Se verifica que los datos ingresados si sean enteros
                int(info[0])
                int(info[1])
            except:
                info.pop()
                info.pop()
                raise NoTipo()

            try:
                [i for i in range(1, 13)].index(int(info[1]))       #Se verifica que el mes sea válido
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            try:
                [i for i in range(1, 32)].index(int(info[0]))       #Se verifica que le día sea válido
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            diames.pack_forget()        #Se elimina el fieldframe para el dia y mes

            salas = FieldFrame("Sala",["Numero"],nomValores,valIniciales,valHabilitados,self.cuerpo)    #Se hace un field frame para la sala
            salas.button.configure(text="Siguiente")

            salas.pack()

            textosalas=""

            for sala in self.cine.getSalas():

                if sala.verificarDisponibilidad(int(info[0]),int(info[1])):     #Se hace un string con las salas disponibles
                    textosalas+= "Sala "+ str(sala.getNumero()) +"\n"
            disponibles=Label(self.cuerpo,text=textosalas)
            disponibles.pack()                      #Se muestran las salas disponibles en un label

            try:
                if textosalas=="":
                    x=1/0
            except:
                raise NotChair()

            def funcionesAuto(action):
                info.append(salas.getValue("Numero"))

                try:
                    disp=[]
                    for sala in self.cine.getSalas():
                        if sala.verificarDisponibilidad(int(info[0]), int(info[1])):        #Se verifica que la sala escogida en efecto sea de las disponibles para ese dia
                            disp.append(sala)                                               #Si no, se lanza la excepcion
                    disp.remove(self.cine.buscarSala(int(info[2])))
                except:
                    info.pop()
                    raise NotIn()

                self.cine.programarFuncionesAuto(int(info[1]),int(info[0]),self.cine.buscarSala(int(info[2])))  #TODO: Revisar que funcione


                messagebox.showinfo(title="Información",message="Función generada con éxito")   #Se muestra el mensaje cuando se termina la operacion
                self.cambiar()


            
            salas.button.bind("<ButtonRelease>",funcionesAuto)      ##Boton 2

        diames.button.bind("<ButtonRelease>", salasDisponibles)     ##Boton 1

        
        #TODO: Revisar que esté funcionando

    
    #Metodo para realizar la rifa entre los clientes fieles
    def rifa(self):

        self.cambiar()

        self.titulo.configure(text = "Rifar Boleto")
        self.texto.configure(text = "Permite rifar un boleto a una función deseada entre los clientes mas fieles")


        nomValores="Información"
        valIniciales=None
        valHabilitados=None
        info=[]

        diames=FieldFrame("Fecha", ["Dia","Mes"],nomValores,valIniciales,valHabilitados,self.cuerpo)        #Se hace un fieldframe para el dia y el mes
        diames.pack()
        diames.button.configure(text="Siguiente")

        def funcdispo(action):
            info.append(diames.getValue("Dia"))
            info.append(diames.getValue("Mes"))

            try:
                int(info[0])            #Se verifica que los datos ingresados si sean enteros
                int(info[1])
            except:
                info.pop()
                info.pop()
                raise NoTipo()

            try:
                [i for i in range(1, 13)].index(int(info[1]))       #Se verifica que sea un mes valido
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            try:
                [i for i in range(1, 32)].index(int(info[0]))       #Se verifica que sea un dia valido
            except:
                info.pop()
                info.pop()
                raise RangoNoPer()

            diames.pack_forget()        #Se elimina el field frame para el mes y el dia

            funcdia=FieldFrame("Funcion", ["Numero"],nomValores,valIniciales,valHabilitados,self.cuerpo)    #Se crea un fieldframe para el numero de la funcion
            funcdia.pack()
            funcdia.button.configure(text="Rifar")

            if len(self.cine.verFuncion(int(info[0]),int(info[1])))==0:         #Si no hay funciones disponibles para ese dia, se lanza la excpecion y se devuelve a la parte principal de la ventana
                info.pop()
                info.pop()
                self.cambiar()
                raise NoDisp()

            else:
                funcioneslibres="Funciones del dia\n"+Funcion.formatearFunciones(self.cine.verFuncion(int(info[0]),int(info[1])))       #Se muestran las funciones del dia en un label
                textofunc=Label(self.cuerpo,text=funcioneslibres)
                textofunc.pack()

            def resultado(action):
                info.append(funcdia.getValue("Numero"))

                try:
                    fdeldia=self.cine.verFuncion(int(info[0]),int(info[1]))         #Se verifica que el numero ingresado si corresponda a una de las funciones disponibles
                    fdeldia.remove(self.cine.BuscadorFuncion(int(info[2])))
                except:
                    info.pop()
                    raise NotIn()

                candidatos="Clientes fieles candidatos a la rifa: "

                for c in self.cine.clientesValiosos():
                    candidatos+=c.getNombre()+" "

                ganador="GANADOR: "+self.cine.rifarBoleto(int(info[2]))     #Se rifa el boleto para la funcion seleccionada pasandole el numero de funcion como argumento

                messagebox.showinfo(title='Rifa de Boleto!', message=candidatos,    #Se hace un messagebox donde se muestran los clientes fieles candidatos a la rifa y se meustra el nombre del ganador
                                    detail=ganador)
                self.cambiar()

            funcdia.button.bind("<ButtonRelease>",resultado)        ##Segundo boton

        diames.button.bind("<ButtonRelease>",funcdispo)  ##Primer boton

    #Metodo para la adicion de salas al cine
    def agregarSala(self):
        self.cambiar()

        self.titulo.configure(text = "Agregar una sala")
        self.texto.configure(text = "Permite agregar una sala segun su tipo (2D o 3D)")

        checked=IntVar()    #Se haceuna variable para ver que radiobutton esta seleccionado

        global nueva        #Se hace una variable global para los fieldframe

        def create(action):
            if checked.get()==2:    #Si la sala seleccionada es 2D

                try:                #Se revisa que los datos ingresados sean enteros
                    int(nueva.getValue("Filas"))
                    int(nueva.getValue("Columnas"))
                    int(nueva.getValue("Filas VIP"))
                except:
                    raise NoTipo()

                try:            #Se revisa que no sean más filas VIP que filas normales, sino se genera un error y se lanza la excepcion
                    if int(nueva.getValue("Filas"))<int(nueva.getValue("Filas VIP")):
                        x=1/0
                except:
                    raise RangoNoPer()

                Sala2D(int(nueva.getValue("Filas")),int(nueva.getValue("Columnas")),int(nueva.getValue("Filas VIP")),self.cine)    #se crea la sala cuando se cumplan las condiciones


            elif checked.get()==3:  #Si la sala seleccionada es 3D

                try:        #Se revisa que los datos ingresados sean enteros
                    int(nueva.getValue("Filas"))
                    int(nueva.getValue("Columnas"))
                    int(nueva.getValue("Gafas disponibles"))
                except:
                    raise NoTipo()

                try:        #Se revisa que no sean más gafas disponibles que asientos, sino se genera un error y se lanza la excepcion
                    total=int(nueva.getValue("Filas"))*int(nueva.getValue("Columnas"))
                    if total<int(nueva.getValue("Gafas disponibles")):
                        x=1/0
                except:
                    raise RangoNoPer()
                Sala3D(int(nueva.getValue("Filas")), int(nueva.getValue("Columnas")),int(nueva.getValue("Gafas disponibles")), self.cine)      #se crea la sala cuando se cumplan las condiciones


            messagebox.showinfo(title="Información",message="Sala creada con éxito!")       #Se muestra un messagebox cuando se termina la operacion
            #for i in self.cine.getSalas():
            #    print(i.getNumero())
            self.cambiar()      #Se devuelve al inicio

        #Metodo para la creacion del fieldframe cuando se selecciona 3D
        def tres():
            global nueva
            try:
                nueva       #Si no existe un fieldframe, que lo cree con los atributos para sala 3D
            except NameError:
                nueva = FieldFrame("Tamaño", ["Filas","Columnas","Gafas disponibles"],"Cantidad",None,None,self.cuerpo)
                nueva.pack()

                nueva.button.bind('<ButtonRelease>',create)
            else:
                nueva.pack_forget()     #Si si existe, que borre el que habia y cree uno nuevo para sala 3D
                nueva = FieldFrame("Tamaño", ["Filas","Columnas","Gafas disponibles"],"Cantidad",None,None,self.cuerpo)
                nueva.pack()
                nueva.button.bind('<ButtonRelease>',create)

        # Metodo para la creacion del fieldframe cuando se selecciona 3D
        def dos():
            global nueva
            try:
                nueva       #Si no existe un fieldframe, que lo cree con los atributos para sala 2D
            except NameError:
                nueva = FieldFrame("Tamaño", ["Filas","Columnas","Filas VIP"],"Cantidad",None,None,self.cuerpo)
                nueva.pack()
                nueva.button.bind('<ButtonRelease>',create)
            else:
                nueva.pack_forget()     #Si si existe, que borre el que habia y cree uno nuevo para sala 2D
                nueva = FieldFrame("Tamaño", ["Filas","Columnas","Filas VIP"],"Cantidad",None,None,self.cuerpo)
                nueva.pack()
                nueva.button.bind('<ButtonRelease>',create)

        tresd=Radiobutton(self.cuerpo,text="3D",variable=checked,value=3,command=tres)      #Radiobutton para seleccionar sala 3D que ejecuta su respectivo metodo
        tresd.pack()
        dosd=Radiobutton(self.cuerpo,text="2D",variable=checked,value=2,command=dos)    #Radiobutton para seleccionar sala 2D que ejecuta su respectivo metodo
        dosd.pack()



        