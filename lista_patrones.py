from nodo_patron import nodo_patron

class lista_patrones:
    def __init__(self):
        self.primero = None
        self.contador_grupos=0
        self.contador = 1
        

    def insertar_dato(self,CPatron):
            if self.primero is None:
                self.primero = nodo_patron(CPatron)
                self.contador_grupos+=1
                self.contador+=1
                return
            
            actual= self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            
            actual.siguiente = nodo_patron(CPatron)
            self.contador_grupos+=1
            self.contador+=1

    def imprimir_proceso(self):
        print(">>>Creando Grupos...")
        print("")
        print(">>>Realizando sumas...")
    
        
    def getSize(self):
        return self.contador_grupos

    def __iter__(self):
            self.actual = self.primero
            return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration
    
    
    def get_contador_grupos(self):
        return self.contador_grupos
    
    def get_contador(self):
        return self.contador
