from nodoMatriz import nodoMatriz

class listaSimpleMatriz:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarMatrices(self,listaSimple):
        nuevoNodo = nodoMatriz(listaSimple)
        if self.primero==None:
            self.primero = nuevoNodo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevoNodo
    
    # def recorrerListaMatrices(self):
    #     if self.primero is None:
    #         print("La lista se encuentra vacia")
    #         return
    #     actual = self.primero
    #     print(f"Nombre Matriz: {actual.listaSimple}")
        
    #     while actual:
    #         print(f"Nombre Matriz: {actual.listaSimple}")
    #         actual = actual.siguiente

    def recorrerListaMatrices(self):
        if self.primero is None:
            print("La lista se encuentra vacia")
            return
        
        actual = self.primero
        while actual:
            print("Nombre Matriz:", actual.listaSimple)
            lista_simple = actual.listaSimple
            if lista_simple.primero:
                nodo_lista_simple = lista_simple.primero
                while nodo_lista_simple:
                    nombre_lista = nodo_lista_simple.CDato.nombre
                    print("  Nombre de lista:", nombre_lista)
                    nodo_lista_simple = nodo_lista_simple.siguiente
            actual = actual.siguiente