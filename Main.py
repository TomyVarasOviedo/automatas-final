from AutomataComandos import AutomataComandos
from AutomataParametros import AutomataParametros
import turtle

# ----Funciones----
def crearCirculo(parametros:str):
    """
    Metodo para crear un circulo en la pantalla
    """
    parametros = parametros.split(" ")
    try:
        circulo = turtle.circle(int(parametros[0]))
        figuras[parametros[1]] =circulo
    except KeyError as e:
        print(e)

def crearBox(parametros:str):
    """
    Metodo para crear un rectangulo en la pantalla
    """
    parametros = parametros.split(" ")
    # Dibujando la caja
    print(parametros)
    # figuras[parametros[2]]=turtle.shape("square")
    turtle.forward(int(parametros[0]))
    turtle.left(90)
    turtle.forward(int(parametros[1]))
    turtle.left(90)
    turtle.forward(int(parametros[0]))
    turtle.left(90)
    turtle.forward(int(parametros[1]))

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
                if len(comando[1].split(" ")) == 2:
                    crearCirculo(comando[1])
                else:
                    print("Parametros incorrectos para ese comando")
            case "box":
                if len(comando[1].split(" ")) == 3:
                    crearBox(comando[1])
                else:
                    print("Parametros incorrectos para ese comando")
            case "move":
                if len(comando[1].split(" ")) == 3:
                    crearBox(comando[1])
                else:
                    print("Parametros incorrectos para ese comando")
# ----Funciones----
figuras = {}

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

