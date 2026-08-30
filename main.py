import subprocess
from datetime import date, time, timedelta
from datetime import datetime

#-----------------------------------------------
#---------Declaración de la clase Cliente
#-----------------------------------------------

class Cliente():

    def __init__(self, nombre:str, telefono:str):
        self.nombre:str =  nombre
        self.telefono:str = telefono

    def get_nombre(self) -> str:
        return self.nombre

    def get_telefono(self) -> str:
        return self.telefono

    def __str__(self) -> str:
        return f"""Nombre : {self.nombre}\nTeléfono : {self.telefono}"""



#-----------------------------------------------
#---------Declaración de estructuras de datos
#-----------------------------------------------

servicios: list[dict[str,str|tuple[int]]] = [
    {"nombre":"Corte de pelo",
     "precio":(10000,)},
    {"nombre":"Barba",
     "precio":(5000,)}] 
# Lista de servicios
# Servicio:
# {"nombre":str,
#  "precio":tuple[int]}


clientes: list[Cliente] = [Cliente("Ariel","4823167"),Cliente("Martina","2917536481")] # Lista de clientes


turnos: list[ dict[str, str | dict[str,str|tuple[int]] ] ] = [
    {"cliente":clientes[1],
     "dia":datetime.strptime("21/09/2026", "%d/%m/%Y").date(),
     "hora":datetime.strptime("16:00", "%H:%M").time(),
     "servicio":servicios[1]},
    {"cliente":clientes[0],
     "dia":datetime.strptime("10/11/2026", "%d/%m/%Y").date(),
     "hora":datetime.strptime("10:30", "%H:%M").time(),
     "servicio":servicios[0]},
    {"cliente":clientes[1],
     "dia":datetime.strptime("22/09/2026", "%d/%m/%Y").date(),
     "hora":datetime.strptime("17:00", "%H:%M").time(),
     "servicio":servicios[1]}] 
# Lista de turnos
# Turno:
#   {"cliente":str,
#    "dia": date,
#    "hora": time,
#    "servicio": servicio}


#-----------------------------------------------
#---------Funciones
#-----------------------------------------------

def mostrar_menu() -> None:
    _mostrar_titulo("menu")
    print("""1. Registrar cliente
2. Buscar cliente
3. Reservar turno
4. Cancelar turno
5. Ver agenda completa
6. Ver turnos de un cliente
7. Mostrar servicios
8. Estadísticas
9. Mostrar clientes
10. Agregar servicios
0. Salir

Seleccione una opción:""")


def _mostrar_titulo(titulo:str, limpiar_pantalla:bool = True) -> None:
    """
    Muestra los titulos de cada seccion indicandolo por parametros:
     menu -> Sistema de turnos
     cliente -> Registro de clientes
    """

    if limpiar_pantalla:
        subprocess.run(["clear"])

    if titulo == "menu":
        print("=========================================")
        print("SISTEMA DE TURNOS")
        print("=========================================")
        print()

    elif titulo == "cliente":
        print("-----------------------------------------")
        print("Registrar Cliente")
        print("-----------------------------------------")
        print()

    elif titulo == "clientes":
        print("-----------------------------------------")
        print("Lista De Clientes")
        print("-----------------------------------------")
        print()

    elif titulo == "mostrar_servicios":
        print("-----------------------------------------")
        print("Lista De Servicios")
        print("-----------------------------------------")
        print()

    elif titulo == "agregar_servicios":
        print("-----------------------------------------")
        print("Agregar Servicios")
        print("-----------------------------------------")
        print()

    elif titulo == "reservar_turno":
        print("-----------------------------------------")
        print("Reserva De Turnos")
        print("-----------------------------------------")
        print()

    elif titulo == "mostrar_agenda":
        print("-----------------------------------------")
        print("Agenda")
        print("-----------------------------------------")
        print()

    elif titulo == "buscar_cliente":
        print("-----------------------------------------")
        print("Buscar Un Cliente")
        print("-----------------------------------------")
        print()

    elif titulo == "seleccionar_servicio":
        print("-----------------------------------------")
        print("Seleccion De Servicio")
        print("-----------------------------------------")
        print()

    elif titulo == "cancelar_turno":
        print("-----------------------------------------")
        print("Cancelacion De Turno")
        print("-----------------------------------------")
        print()

    elif titulo == "buscar_turno_fecha":
        print("-----------------------------------------")
        print("Seleccion Turno")
        print("-----------------------------------------")
        print()

    elif titulo == "mostrar_estadisticas":
        print("-----------------------------------------")
        print("Estadisticas")
        print("-----------------------------------------")
        print()


def _validar_nombre(nombre:str) -> bool:
    """
    Proceso de validacion de nombre pasado por parametro.
    """
    es_correcto:bool = True

    if len(nombre) < 2:     # El nombre debe tener mas de 2 caracteres
        es_correcto = False
    else:
        for caracter in nombre:         # EL nombre no puede tener digitos
            if caracter.isdigit():
                es_correcto = False
                break

    return es_correcto


def _validar_telefono(telefono:str) -> bool:
    """
    Proceso de validacion de numero de telefono pasado por parametro.
    """
    es_correcto:bool = True
    telefono = str(telefono.strip())    # Se le sacan los espacios

    if len(telefono) != 7 and len(telefono) != 10 and len(telefono) != 13: # El numero de teelfono solo puede tener 7, 10 o 13 caracteres
        es_correcto = False
    else:
        if len(telefono) == 13:
            if telefono[0] == "+":
                telefono = telefono[1:]     #Si tiene 13 caracteres y un + adelante se le saca el +
            else:
                es_correcto = False

        if not telefono.isnumeric():        #Solo puede contener numeros el telefono sin el +
            es_correcto = False

    return es_correcto



def _validar_precio(precio:str) -> bool:
    """
    Verifica que el precio sea mayor a 0 y solo contenga digitos.
    """
    es_correcto = True

    if len(precio) == 0:
        es_correcto = False
    else:
        for caracter in precio:
            if not caracter.isdigit():
                es_correcto = False
                break

    return es_correcto
        

def _anio_bisiesto(anio:int) -> bool:
    bisiesto:bool = False

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        bisiesto == True

    return bisiesto


def _validar_fecha(anio:int, mes:str, dia:str) -> bool:
    es_valido:bool = True

    for caracter in mes:
        if not caracter.isdigit():
            es_valido = False
            #print("El mes ingresado no es valido")

    for caracter in dia:
        if not caracter.isdigit():
            es_valido = False
            #print("El dia ingresado no es valido")

    if es_valido:
        dia = int(dia)
        mes = int(mes)

    if es_valido and (mes < 1 or mes > 12):
        es_valido = False

    if es_valido:
        if mes >= 1 and mes <= 12 and dia >= 1:
            if mes == 2:
                if _anio_bisiesto(anio):
                    if dia > 29:
                        es_valido = False
                else:
                    if dia > 28:
                        es_valido = False

            elif mes % 2 == 0:
                if dia > 30:
                    es_valido = False

            else:
                if dia > 31:
                    es_valido = False

                    
        else:
            es_valido = False
    
    return es_valido    
    


def registrar_cliente() -> None:
    """
    Proceso de regisitro de cliente ingresando el nombre y el telefono.
    """
    nombre:str = ""
    telefono:str = ""

    _mostrar_titulo("cliente")
    print("Ingrese el nombre del cliente:")
    while True: #Ciclo de verificacion nombre
        nombre = input()

        if _validar_nombre(nombre):
            break                   #El nombre es valido

        

        _mostrar_titulo("cliente")
        print("El nombre ingresado no es valido.")
        print("Vuelva a ingresar el nombre del cleinte: ")

    
    _mostrar_titulo("cliente")

    print("Ingrese el telefono del cliente: ")
    while True: #Ciclo de verificacion telefono
        telefono = input()

        if _validar_telefono(telefono):
            break                   #El telefono es valido

        

        _mostrar_titulo("cliente")
        print("El numero de telefono no es valido")
        print("Vuelva a ingresar el telefono: ")

    
    _mostrar_titulo("cliente")

    if not _buscar_cliente_telefono(telefono):
        cliente:Cliente = Cliente(nombre,telefono)
        clientes.append(cliente)

        print(cliente)
        print()
        print("Cliente registrado correctamente.")
    else:
        print("Ya existe un cliente registrado con ese numero de telefono.")

    input()

  
def _buscar_cliente_nombre() -> Cliente:
    """
    Busca un cliente por nombre parcial y devuelve ese cliente.
    """
    _validar_numero = _validar_precio   # Le agrega un alias a la funcion _validar_precio ya que sirve apra validar numeros

    ingreso:str = ""
    nombre_parcial:str = ""
    cliente_buscado:Cliente = None
    clientes_aux:list[Cliente] = []
    indice:int = 0

    subprocess.run(["clear"])

    while True:
        if ingreso != ".":
            _mostrar_titulo("buscar_cliente")
            print("Ingrese el nombre completo o parcial del cliente buscado y precione enter:")
            print("Ingrese un punto (.) si ya ve el nombre buscado en la lista. O si ya no ve ingun nombre.")
        
        print()

        if not ingreso == "":

            if not ingreso == ".":
                clientes_aux = []
                indice = 0
                nombre_parcial += ingreso
                print("----------")

                for cliente in clientes:
                    if nombre_parcial.lower() in cliente.get_nombre().lower():  # Muestra los nombres que coinciden parcialmente
                        print()
                        print(f"Posicion: {indice}")
                        print(f"Nombre: {cliente.get_nombre()}")
                        print(f"Telefono: {cliente.get_telefono()}")
                        print("----------")
                        clientes_aux.append(cliente)
                        indice += 1
            elif ingreso == ".": 
                while True:
                    print("Escriba el numero de posicion del cliente que desea seleccionar")
                    print("Ingrese R para buscar de nuevo o S para salir")
                    ingreso = input().strip().lower()

                    if _validar_numero(ingreso) or ingreso == "s" or ingreso == "r":
                        if ingreso != "s" and ingreso != "r":       # Si no es s o r es un nuemro en el rango valido
                            if 0 <= int(ingreso) <= indice:
                                cliente_buscado = clientes_aux[int(ingreso)]

                        break   # En caualquier caso corta el bucle while

                if ingreso == "s" or cliente_buscado:  # Si elligio s (salir) corta el bucle while exterior sino es s ingreso un numero o caracter invalido
                    break
                elif ingreso == "r":
                    nombre_parcial = ""
                    ingreso = ""

        ingreso = input(f"Nombre: {nombre_parcial}").strip()
        #if ingreso != ".":
        #    subprocess.run(["clear"])

    return cliente_buscado


def _buscar_cliente_telefono(telefono:str) -> Cliente:
    """
    Busca un cliente en la lista de clientes por numero de telefono y lo devuelve.
    """
    cliente_buscado:Cliente = None

    for cliente in clientes:
        if cliente.get_telefono() == telefono:
            cliente_buscado = cliente
            break

    return cliente_buscado


def _buscar_turno_fecha(fecha:date) -> dict[str, str|tuple[int]]:
    """
    Permite buscar un turno por fecha y lo devuelve
    """

    turno_buscado:dict[str, str|tuple[int]] = {}
    turnos_ocupados:list[dict[str, str|tuple[int]]] = []
    indice:int = 0
    seleccion:str = ""
    _validar_indice = _validar_precio   # Agrega un alias a la funcion _validar_precio ya que funciona para validar numeros

    _mostrar_titulo("buscar_turno_fecha")

    while True:
        indice = 0
        for turno in turnos:
            if turno["dia"] == fecha:
                print()
                print(f"Posicion: {indice}")
                print(f"{turno["dia"].strftime("%d/%m")} - {turno["hora"].strftime("%H:%M")}")
                print(f"Cliente: {turno["cliente"].get_nombre()}")        
                print(f"Servicio: {turno["servicio"].get("nombre")}")
                print("----------")
                turnos_ocupados.append(turno)
                indice += 1
        print()
        print("Ingrese el numero de posicion del tunro que desee seleccionar")
        print("Si el turno que esa buscando no esta en la lista ingrese 'S'")
        seleccion  = input().strip().lower()

        if _validar_indice(seleccion) and 0 <= int(seleccion) < indice:
            turno_buscado = turnos_ocupados[int(seleccion)]
            break
        elif seleccion == "s":
            break
        else:
            _mostrar_titulo("buscar_turno_fecha")
            print("El vlaor ingresado no es valido")

    return turno_buscado


def _seleccionar_servicio() -> dict[str, str|tuple[int]]:
    """
    Permite seleccionar uno de los servicios disponibles y devolverlo
    """
    seleccion:str = ""
    servicio_seleccionado:dict[str, str|tuple[int]] = {}
    _validar_indice = _validar_precio   # Agrega un alias a la funcion _validar_precio ya que funciona para validar numeros


    _mostrar_titulo("seleccionar_servicio")
    while True:

        for i, servicio in enumerate(servicios):
            print("----------")
            print(f"Nombre : {servicio["nombre"]}")
            print(f"Precio : {servicio.get("precio")[0]}")
            print()

        print("Seleccione uno de los servicios con su numero de posicion")
        print("O ingrese S para salir sin seleccionar uno")
        seleccion = input().lower().strip()

        _mostrar_titulo("seleccionar_servicio")

        if _validar_indice(seleccion) or seleccion == "s":
            break
        else:
            print("Valor ingresado invalido")

    if seleccion != "s":
        servicio_seleccionado = servicios[int(seleccion)]

    return servicio_seleccionado


def _ordenar_turnos() -> None:
    """
    Ordena los turnos por fecha y hora
    """
    global turnos   # Para que reconozca la variable como global y no local y efectvamente ordene la lista

    turnos_ordenado:list[dict[str, str | dict[str,str|tuple[int]]]] = []

    turnos_ordenado = sorted(turnos, key=(lambda x: datetime.combine(x["dia"], x["hora"])))

    turnos = turnos_ordenado


def mostrar_estadisticas() -> None:
    """
    Muestras estadisiticas
    """

    cant_clientes:int = 0
    cant_turnos:int = 0
    servicio_mas_pedido:str = ""
    count_turno_por_servicio = {}
    recaudacion:int = 0
    servicio_turno:str = ""

    cliente:str = ""
    count_turno_por_cliente:dict[str, int] = {}
    cliente_mas_turnos:str = ""


    _mostrar_titulo("mostrar_estadisticas")

    cant_clientes = len(clientes)
    cant_turnos = len(turnos)

    for turno in turnos:
        servicio_turno = turno["servicio"].get("nombre")        
        cliente = turno["cliente"].get_nombre()

        if servicio_turno in count_turno_por_servicio.keys():
            count_turno_por_servicio[servicio_turno] += 1
        else:
            count_turno_por_servicio[servicio_turno] = 1

        if cliente in count_turno_por_cliente.keys():
            count_turno_por_cliente[cliente] += 1
        else:
            count_turno_por_cliente[cliente] = 1

        recaudacion += turno["servicio"].get("precio")[0]

    servicio_mas_pedido_cant:int = max(count_turno_por_servicio.values())
    posicion:int = list(count_turno_por_servicio.values()).index(servicio_mas_pedido_cant)
    servicio_mas_pedido = list(count_turno_por_servicio.keys())[posicion]

    cliente_mas_turnos_cant:int = max(count_turno_por_cliente.values())
    posicion = list(count_turno_por_cliente.values()).index(cliente_mas_turnos_cant)
    cliente_mas_turnos = list(count_turno_por_cliente.keys())[posicion]

    #-------------Muestra

    # Cantidad de clientes registrados.
    print(f"Cantidad de clientes registrados: {cant_clientes}")
    # Cantidad de turnos reservados.
    print(f"Cantidad de turnos reservados: {cant_turnos}")
    print()

    # Cantidad de turnos por servicio.
    print("Cantidad de turnos por servicio:")
    for servicio in count_turno_por_servicio.keys():
        print(f"  Servicio: {servicio}")
        print(f"  Turnos: {count_turno_por_servicio[servicio]}")
        print("  -----")
    print()

    # Servicio más solicitado.
    print(f"Servicio mas solicitado: {servicio_mas_pedido}")
    print()

    # Cliente con mas turnos reservados
    print(f"Cleinte con mas turnos reservados: {cliente_mas_turnos}")
    print()

    # Recaudación estimada.
    print(f"Recaudacion estimada: ${recaudacion}")

    input()



def cancelar_turno() -> None:
    """
    Permite buscar el turno por fecha y hora y cancelarlo.
    """
    turno:datetime = None
    turno_fecha:date = None
    anio:int = datetime.now().year
    mes:str = ""
    dia:str = ""
    seleccion:str = ""

    _mostrar_titulo("cancelar_turno")

    while True:
        print("El tunro es para este año?")
        print("Ingrese 's' en caso afirmativo 'n' en caso negativo")
        seleccion = input().strip().lower()

        _mostrar_titulo("cancelar_turno")

        if seleccion == "s":
            break
        elif seleccion == "n":
            anio += 1
            break
        else:
            print("Valor ingresqado invalido.")

    while True:
        print("Ingrese el numero del mes del turno:")
        mes = input().strip()

        print("Ingrese el numero del dia del turno:")
        dia = input().strip()

        _mostrar_titulo("cancelar_turno")

        if _validar_fecha(anio, mes, dia):
            turno_fecha = date(anio, int(mes), int(dia))
            break

        print("Uno de los valores ingresados no es valido")

    turno = _buscar_turno_fecha(turno_fecha)

    if turno:
        print("Turno seleccionado")

        while True:
            print()
            print(f"{turno["dia"].strftime("%d/%m")} - {turno["hora"].strftime("%H:%M")}")
            print(f"Cliente: {turno["cliente"].get_nombre()}")        
            print(f"Servicio: {turno["servicio"].get("nombre")}")
            print("----------")
            print()
            print("¿Seguro que desea eliminar el tunro? Ingrese 'S' para si o 'N' para no")
            seleccion = input().strip().lower()

            if seleccion == "s":
                turnos.remove(turno)
                break
            elif seleccion == "n":
                break
            else:
                _mostrar_titulo("cancelar_turno")
                print("Valor ingresado no valido")

    else:
        print("No se selecciono un tunro para cancelarlo")
        input()



def _ingresar_horario(fecha:date) -> datetime:
    """
    Permite hacer la seleccion de un horario valido disponible para el dia de la fecha pasada por parametro y devuelve la fecha y hora del turno en datetime
    """
    hora:datetime = datetime.strptime("09:00", "%H:%M")
    horarios_disponibles:list[datetime] = []    # Lista con los horarios disponibles
    seleccion:str = ""
    indice_seleccion:int = 0
    horario_ingresado:datetime = None

    while hora <= datetime.strptime("18:00", "%H:%M"):  # Se llena la lista con los horarios disponibles hasta las 18Hs
        horarios_disponibles.append(hora.time())
        hora += timedelta(minutes=30)

    for turno in turnos:
        if turno.get("dia") == fecha:
            horarios_disponibles.remove(turno.get("hora"))  # Se eliminan de la lista los horarios ocupados

    if len(horarios_disponibles) > 0:
        while True:
            print("Los horarios disponibles son: ")
            print()
            for i, horario in enumerate(horarios_disponibles):
                print("------------")
                print(f"{i}. {horario}")

            print()
            seleccion = input("Seleccione el horario deseado ingresando el numero de posicion: ")
            _validar_indice = _validar_precio   # Agrega un alias a la funcion _validar_precio ya que funciona para validar numeros
            if _validar_indice(seleccion):
                indice_seleccion = int(seleccion)
                if indice_seleccion >= 0 and indice_seleccion < len(horarios_disponibles):
                    break

            _mostrar_titulo("reservar_turno")
            print("Valor ingresado no valido")

        horario_ingresado = datetime.combine(fecha, horarios_disponibles[indice_seleccion])
    else:
        print("No hay horarios disponibles para ese dia.")
        input()
    
    return horario_ingresado 

    
 
def reservar_turno() -> None: # Dividir en mas funciones?
    """
    Permite reservar turnos para este año o el siguiente.
    """
    anio:int = datetime.now().year
    seleccion_anio:str = ""
    seleccion_mes:str = ""
    seleccion_dia:str = ""
    fecha:date = None
    turno:datetime = None
    cliente:Cliente = None
    servicio:dict[str, str|tuple[int]] = {}

    _mostrar_titulo("reservar_turno")

    cliente = buscar_cliente()

    servicio = _seleccionar_servicio()

    if cliente and servicio:
        while True:
            print("El turno es para este año?")
            print("1. Si")
            print("2. No")
            seleccion_anio = input().strip()

            _mostrar_titulo("reservar_turno")

            if seleccion_anio == "2":
                anio += 1
                break
            elif seleccion_anio == "1":
                break        
            
            print("El valor ingresado no es valido.")

        while True:
            print("Ingrese el numero del mes:")
            seleccion_mes = input().strip()

            print("Ingrese el numero de dia: ")
            seleccion_dia = input().strip()

            if _validar_fecha(anio, seleccion_mes, seleccion_dia):
                fecha = date(anio, int(seleccion_mes), int(seleccion_dia))
                break

            _mostrar_titulo("reservar_turno")
            print("La fecha ingresada no es valida")

        _mostrar_titulo("reservar_turno")
        
        turno = _ingresar_horario(fecha)

        if turno:
            turnos.append({"cliente":cliente,"dia":turno.date(),"hora":turno.time(),"servicio":servicio})
            _ordenar_turnos()
            print("Turno reservado exitosamente.")
            input()



def agregar_servicios() -> None:
    _mostrar_titulo("agregar_servicios")

    print("Ingrese el nombre del servicio:")

    while True:
        nombre_servicio:str = input()

        if len(nombre_servicio) >= 1:
            break

        

        _mostrar_titulo("agregar_servicios")
        print("El nombre no puede estar vacio.")

    
    _mostrar_titulo("agregar_servicios")

    print("Ingrese el precio del servicio:")
    
    while True:
        entrada:str = input()
        precio_servicio:int = 0

        if _validar_precio(entrada):
            precio_servicio = int(entrada)
            break

        

        _mostrar_titulo("agregar_servicios")
        print("El precio solo uede contener digitos y debe ser mayor a cero.")

    servicio:dict[str,str|tuple[int]] = {
        "nombre":nombre_servicio,
        "precio":(precio_servicio,)
    }

    servicios.append(servicio)

    
    _mostrar_titulo("agregar_servicios")
    print("Servicio agregado correctamente")
    print()
    print(f"Nombre : {servicio["nombre"]}")
    print(f"Precio : {servicio["precio"][0]}")

    input()
    


def mostrar_clientes() -> None:
    """
    Muestra los clientes cargados en la lista clientes.
    """
    _mostrar_titulo("clientes")
    for cliente in clientes:
        print(cliente)
        print("--------")
        print()

    input()
    

def mostrar_servicios() -> None:
    """
    Muestra los servicios cargados.
    """
    _mostrar_titulo("mostrar_servicios")
    for servicio in servicios:
        print(f"Nombre : {servicio["nombre"]}")
        print(f"Precio : {servicio["precio"][0]}")
        print("--------")
        print()

    input()
    

def mostrar_agenda(nombre_cliente:str = None) -> None:
    """
    Muestra la agenda completa o solamente la de un cleinte especifico si se pasa el nombre por parametro.
    """
    _mostrar_titulo("mostrar_agenda")

    if nombre_cliente:
        print(f"Mostrando agenda de {nombre_cliente}")
        print()

    for turno in turnos:
        if turno["cliente"].get_nombre() == nombre_cliente or not nombre_cliente:
            print(f"{turno["dia"].strftime("%d/%m")} - {turno["hora"].strftime("%H:%M")}")
            print(f"Cliente: {turno["cliente"].get_nombre()}")        
            print(f"Servicio: {turno["servicio"].get("nombre")}")
            print()
            print("-----------------------------------------")
            print()

    input()


def mostrar_turnos_cliente() -> None:
    """
    Busca un cliente y muestra sus turnos agendados.
    """
    _mostrar_titulo("mostrar_agenda")

    cliente:Cliente = _buscar_cliente_nombre()

    if cliente:
        mostrar_agenda(nombre_cliente=cliente.get_nombre()) 
    else:
        print("Cliente no seleccionado.")
        input()


def buscar_cliente() -> Cliente:
    """
    Busca un cliente por numero de telefono completo o por nombre parcial o completo
    """
    seleccion:str = ""
    cliente:Cliente = None

    _mostrar_titulo("buscar_cliente")

    while True:
        print("Seleccione el metodo de busqueda del cliente:")
        print("1. Nombre")
        print("2. Telefono")
        seleccion = input().strip()

        if seleccion == "1":
            cliente = _buscar_cliente_nombre()
            break
        elif seleccion == "2":
            print()
            print("Ingrese el numero de telefono completo del cliente:")
            seleccion = input().strip()
            if _validar_telefono(seleccion):
                cliente = _buscar_cliente_telefono(seleccion)

            break

        else:
            _mostrar_titulo("buscar_cliente")
            print("Valor ingresado no valido")

    _mostrar_titulo("buscar_cliente")

    if cliente:
        print("Cliente encontrado.")
        print()
        print(f"Nombre : {cliente.get_nombre()}")
        print(f"Telefono : {cliente.get_telefono()}")
    else:
        print("No se a encontrado el cliente.")

    input()
    return cliente


#-----------------------------------------------
#---------Main
#-----------------------------------------------

def main() -> None:
    seleccion: int = 0

    while True:
        mostrar_menu()

        seleccion = input()        

        if seleccion == "1":
            registrar_cliente()     # Registrar Cliente
        elif seleccion == "2":
            buscar_cliente()    # Buscar Cliente
        elif seleccion == "3":
            reservar_turno()    # Reservar Turno
        elif seleccion == "4":
            cancelar_turno()    # Cancelar Turno
        elif seleccion == "5":
            mostrar_agenda()    # Ver Agenda Completa
        elif seleccion == "6":
            mostrar_turnos_cliente()    # Ver Turnos de un Cliente
        elif seleccion == "7":
            mostrar_servicios() # Mostrar servicios
        elif seleccion == "8":
            mostrar_estadisticas()  # Estadisticas
        elif seleccion == "9":
            mostrar_clientes()  # Mostrar cleintes
        elif seleccion == "10":
            agregar_servicios() # Agregar servicios
        elif seleccion == "0":
            break               # Salir
        else:
            print("EL NUMERO SELECCIONADO NO ES VALIDO.")

        




if __name__ == "__main__":
    main()