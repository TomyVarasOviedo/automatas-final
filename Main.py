from AutomataComandos import AutomataComandos
from AutomataParametros import AutomataParametros
import turtle

# ----Funciones----
def crearCirculo(parametros:str):
    """
    Metodo para crear un circulo en la pantalla
    """
    parametros = parametros.split(" ")
    turtle.circle(int(parametros[0]))

def crearBox(parametros:str):
    """
    Metodo para crear un rectangulo en la pantalla
    """
    parametros = parametros.split(" ")
    # turtle.
def reconocerCadena(cadena:str)->str:
    """
    Metodo para reconcer las cadenas enviadas atraves de la linea de comandos
    """
    cadenaModificada=cadena.split(" ", 1)
    comandos = AutomataComandos()
    parametros = AutomataParametros()
    try:
        if comandos.reconocerCadena(cadenaModificada[0]) == "aceptada":
            if parametros.reconocerCadena(" "+cadenaModificada[1]) == "aceptada":
                return "correcta"
            else:
                return "parametros: rechzados"
        else:
            return "comandos: rechazados"
    except IndexError as e:
        return "comando: incorrecto"

def ejecutarComandos(cadena:str):
    if reconocerCadena(cadena):
        comando = cadena.split(" ", 1) #comando[0]: accion, comando[1]: parametros
        match comando[0]:
            case "circle":
                crearCirculo(comando[1])
            case "box":
                crearBox(comando[1])
# ----Funciones----

print("""Comandos:
        > circle (radio:int) (nombre.ej: n,m)
        > box (altura:int) (base:int) (nombre:ej:n,m)
        > move (cordenada x:int) (cordenada y:int) (nombre.ej:n,m)
        """)
while True:
    comandos = input(">")
    ejecutarComandos(comandos)
    if comandos == "exit":
        break

