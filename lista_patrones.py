from nodo_patron import nodo_patron

class lista_patrones:
    def __init__(self):
        self.primero = None
        self.contador_grupos=0

    def print_me():
        print('ok')

    def insertar_dato(self,CPatron):
            if self.primero is None:
                self.primero = nodo_patron(CPatron)
                self.contador_grupos+=1
                return
            
            actual= self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            
            actual.siguiente = nodo_patron(CPatron)
            self.contador_grupos+=1
            # print(CPatron)


    def recorrer_e_imprimir_lista(self):
        print("===========================================================================================")
        actual = self.primero
        while actual != None:
            print(" Grupo: ",actual.CPatron.grupo_tiempos,"Cadena-grupo: ",actual.CPatron.grupo_valores)
            actual = actual.siguiente
        print("===========================================================================================")
        
