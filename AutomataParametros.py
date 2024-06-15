class AutomataParametros():
    """Automata para indenticar parametros"""
    indicidencia={}
    def __init__(self):
        self.estado_inicial ="q0"
        self.estado_final=["q4"]
        #Armamos tres categorias para las letras, los numeros y el espacio
        """
            num: Cualquier caracter de numero sin incluir el cero
            num0: Caracter 0
            nomb: Cualquier letra del alfabeto español
            z: Caracter de espacio
        """
        self.Alfabeto ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.indicidencia={
            "q0":{
                "z":"q1"
            },
            "q1":{
                "num":"q2" #Por un numero va hacia el q2
            },
            "q2":{
                "num":"q2",
                "z":"q3" #Por un caracter vacion puede ir a q3
            },
            "q3":{
                "nomb":"q4", #Por una letra del alfabeto (que representa el nombre) va hacia q4
                "num":"q5"
            },
            "q5":{
                "z":"q6",
                "num":"q5",
                "num0":"q5" #Por el numero cero vuelve de nuevo al estado q5
            },
            "q6":{
                "nomb":"q4"
            }
        }
    def transiciones(self,estado,caracter:str)->str:
        """
        Metodo para realizar las transiciones dentro del automata
        estado->str
        caracter->str
        """
        if caracter.isnumeric(): #Si el caracter es un numero 
            return self.indicidencia[estado]["num"]
        elif caracter == "0": #Si el caracter es un numero y es 0
            return self.indicidencia[estado]["num0"]
        elif caracter == " ": #Si el caracter es un espacio vacio
            return self.indicidencia[estado]["z"]
        else: #Si el caracter es un letra
            return self.indicidencia[estado]["nomb"]

    def reconocerCadena(self, cadena:str)->str:
        """
        Metodo para reconocer la cadena ingresada por parametros
        cadena->str
        """
        q=self.estado_inicial
        for i in cadena:
            if not i in self.Alfabeto:
                return "rechazada"
        
        for i in cadena:
            try:
                q=self.transiciones(q,i)
            except KeyError as e:
                return "Rechazada"
            
        return "aceptada" if q in self.estado_final else "rechazada"