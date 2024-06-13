class AutomataParametros():
    """Automata para indenticar parametros"""
    def __init__(self):
        self.estados={0,1,2,3,4}
        self.estado_inicial ={0}
        self.estado_final={4}
        self.Alfabeto = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        self.incidencia = {
            (0,' '):0,
            (0, 'n'): 1,
            (1, ' '): 2,
            (1, 'n'): 1,
            (2, ' '): 2,
            (2, 'n'): 2,
            (2, 'n'): 3,
            (3, ' '): 3,
            (3, 'l'): 4,
            (3, 'n'): 3,
        }
    def transicion(self, estado, symbolo):
        if symbolo in "0123456789":
            symbolo_tipo = 'n'
        elif symbolo in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            symbolo_tipo = 'l'
        elif symbolo == ' ':
            symbolo_tipo = ' '
        else:
            return None
    
        return self.incidencia.get((estado, symbolo_tipo), None)
    

    def reconocerCadena(self, cadena:str)->str:
        q=self.estado_inicial
        for i in cadena:
            if not i in self.Alfabeto:
                return "rechazada"
        
        for i in cadena:
            q = self.transicion(q,i)
            if q is None:
                return "rechazada"
        return "aceptada" if q in self.estado_final else "rechazada"