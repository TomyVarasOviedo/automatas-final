class AutomataComandos():
    """Automata que reconoce los comandos ingresado en la cadena"""
    estado_inicial=""
    estado_final=""
    Alfabeto=[]
    inicidencia={}
    def __init__(self):
        self.estado_inicial = "q0"
        self.estado_final = "qf"
        self.Alfabeto =["c","i","r","l","e","b","o","x","m","v","s","a","t"]
        self.incidencia ={
            "q0":{
                "c":"qc1",
                "r":"qr1",
                "b":"qb1",
                "m":"qm1",
                "s":"qs1"
            },
            # Comando: circle
            "qc1":{
                "i":"qc2"
            },
            "qc2":{
                "r":"qc3"
            },
            "qc3":{
                "c":"qc4"
            },
            "qc4":{
                "l":"qc5"
            },
            "qc5":{
                "e":"qf"
            },
            #Comando: box
            "qb1":{
                "o":"qb2"
            },
            "qb2":{
                "x":"qf"
            },
            # Comando: move
            "qm1":{
                "o":"qm2"
            },
            "qm2":{
                "v":"qm3"
            },
            "qm3":{
                "e":"qf"
            },
            # Comando: scale
            "qs1":{
                "c":"qs2"
            },
            "qs2":{
                "a":"qs3"
            },
            "qs3":{
                "l":"qc5"
            },
            # Comando: rotate
            "qr1":{
                "o":"qr2"
            },
            "qr2":{
                "t":"qr3"
            },
            "qr3":{
                "a":"qr4"
            },
            "qr4":{
                "t":"qr5"
            },
            "qr5":{
                "e":"qf"
            },
        }
    def reconocerCadena(self,cadena:str)->str:
        """
        Metodo para que el automata reconozca una cadena de comandos
        """
        i=0
        q=self.estado_inicial
        for j in cadena:
            if j in self.Alfabeto:
                continue
            else:
                return "rechazada"
        
        while i<len(cadena):
            try:
                q = self.incidencia[q][cadena[i]]
                i=i+1
            except KeyError as e:
                return "rechazada"
        return "aceptada" if q in self.estado_final else "rechazada"

                


    