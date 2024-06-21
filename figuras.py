import turtle as turtle
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
screen.title("Dibujo de Figuras con Turtle")
screen.bgcolor("white")
figuras = []

#Buscar una figura en concreto
def buscar(nombre: str):
    global figuras
    for i in figuras:
        if(i.nombre == nombre):
            return i
    return False

#Funcion para decidir la forma de la figura
def elegir():
    while(True):
        print(">> Que forma quiere que tenga?\n>> 1. Circulo.\n>> 2. Box")
        ans = input(">> ")
        if(ans == "1"):
            forma = "circulo"
            return forma
        elif(ans == "2"):
            forma = "box"
            return forma
        else:
            print("No valido intente de nuevo.")
#Funcion para dibujar todas las figuras contenidas en la lista figuras
def drawAll():
    global figuras
    global screen
    screen.clearscreen()
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

nombre = ""
forma = ""
largo = ""
ancho = ""
#Bucle
print("Bienvenido")
while(True):
    print(">> 1. Crear una figura.\n>> 2. Ampliar el tamaño de alguna figura\n>> 3. Mover alguna figura.\n>> 4. Rotar figura. \n>> 5. Salir." )
    ans = input(">> ")
    if(ans == "1"):
        nombre = input(">> Ingrese el nombre de su figura:\n>> ")
        forma = elegir()
        if(forma == "circulo"):
            largo = (int) (input(">> Ingrese el radio de su figura:\n>> "))
            ancho = 0
        else: 
            largo = (int) (input(">> Ingrese el largo de su figura:\n>> "))
            ancho = (int) (input(">> Ingrese el ancho de su figura:\n>> "))
        x = Figuras(nombre, forma, largo, ancho)
        figuras.append(x)
    elif(ans == "2"):
        nombre = input(">> Ingrese el nombre de la figura:\n>> ")
        x = buscar(nombre)
        if(x == False):
            print("Esa figura no existe.")
        else:
            fact = (int) (input(">> Ingrese el factor de cuanto la va a ampliar:\n>> "))
            x.extend(fact)
    elif(ans == "3"):
        nombre = input(">> Ingrese el nombre de la figura:\n>> ")
        x = buscar(nombre)
        if(x == False):
            print("Esa figura no existe.")
        else:
            posX = (int) (input(">> Ingrese cuanto quiere moverlo en el eje X (Positivos y negativos son validos):\n>> "))
            posY = (int) (input(">> Ingrese cuanto quiere moverlo en el eje Y (Positivos y negativos son validos):\n>> "))
            x.move(posX, posY)
    elif(ans == "4"):
        nombre = input(">> Ingrese el nombre de la figura:\n>> ")
        x = buscar(nombre)
        if(x == False):
            print("Esa figura no existe.")
        else:
            angle = (int) (input(">> Ingrese en cuantos grados quiere girar la figura:\n>> "))
            x.girar(angle)
    elif(ans == "5"):
        print(">> HASTA LUEGO")
        break
    else:
        print(">> Invalido. Intente de nuevo")
    
    drawAll()