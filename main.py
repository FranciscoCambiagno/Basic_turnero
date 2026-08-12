
#---------Declaración de la clase Cliente
class Cliente():

    def __init__(self, nombre:str, telefono:str):
        self.nombre:str =  nombre
        self.telefono:str = telefono

    def get_nombre(self) -> str:
        return self.nombre

    def get_telefono(self) -> str:
        return self.telefono



#---------Declaración de estructuras de datos

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



#---------Funciones

def mostrar_menu() -> None:
    print("""=========================================
SISTEMA DE TURNOS
=========================================

1. Registrar cliente
2. Buscar cliente
3. Reservar turno
4. Cancelar turno
5. Ver agenda completa
6. Ver turnos de un cliente
7. Mostrar servicios
8. Estadísticas
0. Salir

Seleccione una opción:""")


#registrar_cliente()
#buscar_cliente()
#reservar_turno()
#cancelar_turno()
#mostrar_agenda()
#mostrar_turnos_cliente()
#mostrar_servicios()
#mostrar_estadisticas()

def main() -> None:
    mostrar_menu()

if __name__ == "__main__":
    main()