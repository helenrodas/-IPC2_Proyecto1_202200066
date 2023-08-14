from nodo import nodo

class listaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    

    def insertar(self,CDato):
        nuevoNodo = nodo(CDato)
        if self.primero==None:
            self.primero = nuevoNodo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevoNodo
            
    def recorrer(self):
        actual = self.primero
        while actual != None:
            print(f"t: {actual.CDato.tiempo}, A: {actual.CDato.amplitud}, Valor: {actual.CDato.valor}")
            actual = actual.siguiente

    def recorrerListaBinaria(self):
        actual = self.primero
        while actual != None:
            print(f"t: {actual.CDato.tiempo}, A: {actual.CDato.amplitud}, Valor: {actual.CDato.valorBinario}")
            actual = actual.siguiente

