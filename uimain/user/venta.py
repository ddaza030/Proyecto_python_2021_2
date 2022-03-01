"""Funcion encargada para la ventana de venta de tiquetes, en la cual podemos evidenciar la inscripción de 
clientes al sistema
by: Daniel Daza, Daniel Cadavid, Juan Ochoa, Marlon Calle
"""

from ast import NotIn
from tkinter import *
from uimain.user.fieldFrame import FieldFrame
from gestionAplicacion.cinemas.cliente import Cliente
from gestionAplicacion.cinemas.cine import Cine
from gestionAplicacion.boleteria.funcion import Funcion
from gestionAplicacion.boleteria.pelicula import Pelicula
from gestionAplicacion.boleteria.horario import Horario
from gestionAplicacion.salas.sala2D import Sala2D
from uimain.user.excepciones.notipo import NoTipo
from uimain.user.excepciones.notin import NotIn
from uimain.user.excepciones.notchair import NotChair




def ventana(variable, window, cine):
    venta = Frame()                   # aca creamos la ventana principal, en la que guardaremos los diferentes frames durante el proceso
    cliente = None                    # se define la variable cliente para alvergar al cliente


    frame = FieldFrame("Cedula Cliente", ["Cedula"], "Ingrese Dato", None, None, window)# se crea el primer frame, el cual recibe la identificacion del cliente

    def vender(existente):
        #se crean la variables necesarias para que funcione esta función
        nonlocal frame
        nonlocal venta
        nonlocal cliente
        nonlocal cine

        boton_recomendada = None
        boton_funcion = None
        boton_pelicula = None
        label = None

        frame.pack_forget()
        frame = Frame(window)
        frame.pack()
        venta = Frame(frame)
        venta.pack()
        texto = Label(venta, text="Busqueda por : ")
        

        nueva = None

        def mostrar_sillas(funcion):
            nonlocal nueva
            nonlocal cliente
            nonlocal cine
            nonlocal label

            sillas = funcion.verDisponibilidad()        #esto es una lista de tuplas con (disponibilidad: boolean, y número)
            filas = funcion.getSala().getFilas()        #columnas para más adelante
            columnas = funcion.getSala().getColumnas()  #columnas para más adelante
            nueva.pack_forget()
            label.pack_forget()
            label = Label(venta, text="Seleccione la silla que desea")
            label.pack()
            nueva = Frame(venta)
            nueva.pack()

            def vender_boleto(numero):
                nonlocal nueva
                funcion.getBoletos()[numero].calcularPrecioDefinitivo(cliente)
                funcion.VentaBoleto(funcion.getBoletos()[numero], cliente)
                
                nueva.pack_forget()
                nueva = FieldFrame("Se ha vendido el boleto",                #aca se copia el precio de la boleta en pantalla 
                                   [],
                                   "numero " + str(numero + 1),
                                   [], None, venta)
                precio = Label(venta,text = "El precio es "+str(funcion.getBoletos()[numero].getPrecioTotal()))
                
                nueva.pack()
                precio.pack()
                nueva.button.bind('<ButtonRelease>', lambda x=variable: variable.cambiar())
                descuento_aplicado = Label(venta, text = "Descuento aplicado \n" + str((cliente.getDescuento())*funcion.getBoletos()[numero].calcularPrecio())) # se muestra el descuento aplicado
                descuento_aplicado.pack()

            def holi():
                raise NotChair


            #El siguiente bloque de código se usa para poner los botones de las sillas disponibles en pantalla

            num = 0
            botones = []    #comenzamos con una variable para guardar los botones
            funciones = []  #y una para guardar las funciones
            for i in range(filas):          #se recorren las filas
                for j in range(columnas):   #se recorren las columnas

                    if (num < funcion.getSala().getCantidadSillas()): #si el num de botones creados no supera el de cantidad de sillas 
                                                                      #se continua
                        
                        if (sillas[num][0] == True):                   #si la silla se encuentra disponible se crea un botón con funcionalidad y gris
                            funciones.append(lambda: vender_boleto(num))
                            a = Button(master=nueva, text=str(sillas[num][1]), height=2, width=4,
                                       command=lambda x=(columnas * i + j): vender_boleto(x))
                        else:                                           # de lo contrario se crea un botón que llame una excepción y azul
                            a = Button(master=nueva, text=str(sillas[num][1]), height=2, width=4, bg="blue",
                                       command=holi)
                        botones.append(a)
                        botones[num].grid(column=j, row=i, padx=3, pady=3)
                        num += 1

        def mostrar_funciones(funciones):
            # se usa funciones para mostrar en pantalla las funciones disponibles
            nonlocal nueva
            nonlocal texto
            nonlocal cliente
            nonlocal cine
            nonlocal label
            
            try:
                nueva.pack_forget()     # se intenta borrar nueva
                label.pack_forget()     # se intenta borrar label
            except AttributeError:
                pass


            nueva = FieldFrame("Mostrar", ["Número de Funcion"], "Ingrese Dato", None, None, venta) # se recoge el número de la función
            nueva.pack()                                                                            
            texto.pack_forget()

            def obtenerFuncion():
                nonlocal nueva
                numero = nueva.getValue("Número de Funcion")  # aca obtenemos el número de la función que que queremos ver
                try:
                    cine.BuscadorFuncion(numero).getHorario() # se revisa que el número de la función escogida exista en la base de datos
                except: 
                    raise NotIn                                # de lo contrario se lanza la excepción

                mostrar_sillas(cine.BuscadorFuncion(numero))   # y acá llamamos la función que nos muestra las sillas

            nueva.button.bind('<ButtonRelease>', lambda x: obtenerFuncion())        #se le añade la función al botón para obtenerlafuncion
            label = Label(venta, text=str(Funcion.formatearFunciones(funciones)))
            label.pack()

            try:
                boton_recomendada.pack_forget()
                boton_funcion.pack_forget()
            except AttributeError:
                boton_funcion.pack_forget()

        def llamar_funcion():
            nonlocal label
            nonlocal nueva
            nonlocal cine

            label.pack_forget()
            funcion = FieldFrame("Fecha", ["Dia", "Mes"], "Ingrese datos", None, None, venta)# se reciben los datos del cliente
            funcion.pack()
            try:
                nueva.pack_forget()                                                          # si existe otra nueva la quita
            except AttributeError:
                pass
            nueva = funcion                                                                   #y se reasigna
            funciones = None

            def funcionesxfuncion():
                nonlocal funciones

                funciones = cine.verFuncion(int(funcion.getValue("Dia")), int(funcion.getValue("Mes")))
                mostrar_funciones(funciones)

            nueva.button.bind('<ButtonRelease>', lambda x: funcionesxfuncion())

        if (existente):                         # si el cliente existe en la base de datos se le permite buscar por recomendadas
                                                #o por día
            
            nombre = cliente.getNombre()
            puesto = cliente.getOcupacion()

            label = Label(venta, text = str(nombre)+" / "+ str(puesto))# con este label añadimos el nombre y la profesión del cliente en la
                                                                        #parte superior
            label.pack()
            texto.pack()
            boton_recomendada = Radiobutton(venta, text="Recomendada", value=1,
                                            command=lambda: mostrar_funciones(cine.verFuncion(cliente)))#si se busca por recomendada se llama   
            boton_recomendada.pack()                                                                    #a mostrar_funciones con estas funciones
            boton_funcion = Radiobutton(venta, text="Funcion", value=3, command=llamar_funcion)         #y acá muestra los datos para llenar los ´dias
            boton_funcion.pack()
        else:                                   # De lo contrario solo le permite buscar po día
            
            nombre = cliente.getNombre()
            puesto = cliente.getOcupacion()

            label = Label(venta, text = str(nombre)+" / "+ str(puesto))
            label.pack()

            boton_funcion = Radiobutton(venta, text="Funcion", value=3, command=llamar_funcion)
            boton_funcion.pack()

    def cedula(numero):
        nonlocal cine
        nonlocal frame
        nonlocal cliente

        try:                #Acá se realiza la excepción, si el número ingresado no se puede convertir a entero, lanza error, por lo que 
                            #llama al raise NoTipo
            int(numero)
        except:
            raise NoTipo

        if (cine.buscadorCliente(numero) == None):  #Si el cliente no se encuentra en la base de datos se crea el frame que recibe todos los datos del 
                                                    #cliente

            frame.pack_forget()
            frame = FieldFrame("Inscripción", ["Cedula referido", "Nombre", "Edad", "Ocupacion"], "ingrese datos", None,
                               None, window)
            frame.pack()

            def crearCliente():
                nonlocal cliente
                if (int(frame.getValue("Cedula referido")) != 0):#si el cliente no cuenta con ningún referido se verifica que los datos correspondan 
                                                                 #a los pedidos
                    try:
                        [int(i) / 0 for i in frame.getValue("Nombre") if i in list("123456789")]
                        [int(i) / 0 for i in frame.getValue("Ocupacion") if i in list("123456789")]
                        int(frame.getValue("Edad"))
                        cine.buscadorCliente(int(frame.getValue("Cedula referido"))).getDescuento()

                    except:
                        raise NoTipo

                    cliente = Cliente(numero, str(frame.getValue("Nombre")), int(frame.getValue("Edad")),# acá creamos al cliente
                                      frame.getValue("Ocupacion"), cine)
                    cliente.referidos()                                                                 #y se le aplica su respectivo descuento por 
                                                                                                        #referido 
                    vender(False)
                else:                                                                                   #y este es el caso en el que 
                    try:                                                                                #no tiene referido
                        [int(i) / 0 for i in frame.getValue("Nombre") if i in list("123456789")]       
                        [int(i) / 0 for i in frame.getValue("Ocupacion") if i in list("123456789")]
                        int(frame.getValue("Edad"))

                    except:
                        raise NoTipo

                    cliente = Cliente(numero, str(frame.getValue("Nombre")), int(frame.getValue("Edad")),
                                      frame.getValue("Ocupacion"), cine)
                    vender(False)

            frame.button.bind('<ButtonRelease>', lambda x: crearCliente())#ademas le añadimos la función de crearCliente

        else:
            
            cliente = cine.buscadorCliente(numero)
            vender(True)

    frame.pack()
    #se empaqueta el frame y abajo se le añade una función al boton dle frame que llame a la función cedula
    frame.button.bind('<ButtonRelease>', lambda x: cedula(frame.getValue("Cedula")))



