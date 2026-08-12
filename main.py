import subprocess

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

clientes: list[Cliente] = [] # Lista de clientes

turnos: list[dict[str, str | dict[str,str|tuple[int]]  ]] = [] # Lista de turnos
# Turno:
#   {"cliente":str,
#    "dia":,
#    "hora":,
#    "servicio": servicio}

servicios: list[dict[str,str|tuple[int]]] = [] # Lista de servicios
# Servicio:
# {"nombre":str,
#  "precio":tuple[int]}



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
0. Salir

Seleccione una opción:""")


def _mostrar_titulo(titulo:str) -> None:
    """
    Muestra los titulos de cada seccion indicandolo por parametros:
     menu -> Sistema de turnos
     cliente -> Registro de clientes
    """


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

    elif titulo == "":
        pass


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

        subprocess.run(["clear"])

        _mostrar_titulo("cliente")
        print("El nombre ingresado no es valido.")
        print("Vuelva a ingresar el nombre del cleinte: ")

    subprocess.run(["clear"])
    _mostrar_titulo("cliente")

    print("Ingrese el telefono del cliente: ")
    while True: #Ciclo de verificacion telefono
        telefono = input()

        if _validar_telefono(telefono):
            break                   #El telefono es valido

        subprocess.run(["clear"])

        _mostrar_titulo("cliente")
        print("El numero de telefono no es valido")
        print("Vuelva a ingresar el telefono: ")

    subprocess.run(["clear"])
    _mostrar_titulo("cliente")

    if not buscar_cliente(telefono):
        cliente:Cliente = Cliente(nombre,telefono)
        clientes.append(cliente)

        print(cliente)
        print()
        print("Cliente registrado correctamente.")
    else:
        print("Ya existe un cliente registrado con ese numero de telefono.")

    input()
    subprocess.run(["clear"])



def buscar_cliente(telefono:str) -> Cliente:
    """
    Busca un cliente en la lista de clientes por numero de telefono y lo devuelve.
    """
    cliente_buscado:Cliente = None

    for cliente in clientes:
        if cliente.get_telefono() == telefono:
            cliente_buscado = cliente
            break

    return cliente_buscado


#reservar_turno()
#cancelar_turno()
#mostrar_agenda()
#mostrar_turnos_cliente()
#mostrar_servicios()
#mostrar_estadisticas()


def _mostrar_clientes() -> None:
    """
    Muestra los clientes guardados en la lista clientes.
    """
    _mostrar_titulo("clientes")
    for cliente in clientes:
        print(cliente)
        print("--------")
        print()

    input()
    subprocess.run(["clear"])


#-----------------------------------------------
#---------Main
#-----------------------------------------------

def main() -> None:
    selection: int = 0

    while True:
        mostrar_menu()

        selection = input()

        subprocess.run(["clear"])

        if selection == "1":
            registrar_cliente()
        elif selection == "2":
            pass
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "7":
            pass
        elif selection == "8":
            pass
        elif selection == "9":
            _mostrar_clientes()
        elif selection == "0":
            break
        else:
            print("EL NUMERO SELECCIONADO NO ES VALIDO.")

        




if __name__ == "__main__":
    main()