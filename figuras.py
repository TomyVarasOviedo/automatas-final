import turtle as turtle
from AutomataComandos import AutomataComandos
from AutomataParametros import AutomataParametros

# Clase de las figuras que se van a realizar
class Figuras:
    def __init__(self, nombre: str, forma: str, largo: int, ancho: int):
        self.nombre = nombre
        self.forma = forma
        self.largo = largo
        self.ancho = 0 if forma == "circulo" else ancho
        self.posX = 0
        self.posY = 0
        self.angulo = 0

    def move(self, posX: int, posY: int):
        self.posX += posX
        self.posY += posY

    def extend(self, factor: int):
        self.largo *= factor
        self.ancho *= factor

    def girar(self, angulo: int):
        self.angulo += angulo if (self.angulo + angulo) <= 360 else (angulo - 360)

#Pantalla del turtle
screen = turtle.Screen()
screen.title("Figuras")
screen.bgcolor("black")
figuras = []

#Buscar una figura en concreto
def buscar(nombre: str):
    global figuras
    for i in figuras:
        if(i.nombre == nombre):
            return i
    return False

#Funcion para dibujar todas las figuras contenidas en la lista figuras
def drawAll():
    global figuras
    global screen
    screen.clearscreen()
    screen.bgcolor('black')
    turtle.color('cyan')
    turtle.begin_fill()
    for i in figuras:
        turtle.penup()
        turtle.home()
        turtle.goto(i.posX, i.posY)
        turtle.pendown()
        turtle.right(i.angulo)
        if(i.forma == "circulo"):
            turtle.circle(i.largo)
        else:
            turtle.forward(i.ancho)
            turtle.right(90)
            turtle.forward(i.largo)
            turtle.right(90)
            turtle.forward(i.ancho)
            turtle.right(90)
            turtle.forward(i.largo)
            turtle.right(90)
    turtle.end_fill()

nombre = ""
forma = ""
largo = ""
ancho = ""
def reconocer_cadena(cadena:str)->str:
    """
    Metodo para reconer la cadena ingresada atraves de los automatas
    """
    cadenaModificada = cadena.split(" ", 1)
    comandos = AutomataComandos()
    parametros = AutomataParametros()
    try:
        if comandos.reconocerCadena(cadenaModificada[0]) == "aceptada":
            if parametros.reconocerCadena(" "+cadenaModificada[1]) == "aceptada":
                return "aceptada"
            else:
                return "parametros: rechzados"
        else:
            return "comandos : rechazados"
    except IndexError as e:
        return "Comando incorrecto"

#Bucle
print("""Bienvenido
        comandos:
        => circle (radio) (nombre)
        => box (largo) (ancho) (nombre)
        => move (cordenada x) (cordenada y) (nombre de la figura)
        => scale (factor, ej: 2) (nombre de la figura)
        => rotate (angulo) (nombre de la figura)
        <---------------------------------------------------------->
        """)


while True:
    comandos = input("->")
    reconocimiento = reconocer_cadena(comandos)
    if reconocimiento == "aceptada":
        comando = comandos.split(" ")
        #comando[0] => comando
        #comando[1] => radio if "circulo" | ancho if "box"
        #comando[2] => nombre if "circulo" | alto if "box"
        #comando[3] => nombre if "box" | nombre if "move", "scale" "rotate"
        if comando[0] == "circle":
            x = Figuras(comando[2], "circulo", int(comando[1]), 0)
            figuras.append(x)
        elif comando[0] == "box":
            x = Figuras(comando[3], "box", int(comando[2]), int(comando[1]))
            figuras.append(x)
        elif comando[0] == "move":
                x = buscar(comando[3])
                if x != False:
                    x.move(int(comando[1]), int(comando[2]))
                else:
                    print("Nombre de la figura incorrecto")
        elif comando[0] == "scale":
                x = buscar(comando[2])
                if x != False:
                    x.extend(int(comando[1]))
                else:
                    print("Nombre de la figura incorrecto")
        elif comando[0] == "rotate":
                x = buscar(comando[2])
                if x != False:
                    x.girar(int(comando[1]))
                else:
                    print("Nombre de la figura incorrecto")
        drawAll()
    elif comandos == "exit":
        break
    else:
        print("Comando incorrecto")
    print("""   Nombre   |   Forma   |
-------------------------""")
    for figura in figuras:
        print(f"   {figura.nombre}   |   {figura.forma}   ")

