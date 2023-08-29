from nodo_grupo import nodo_grupo

class lista_grupos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

            
    def insertar(self,CGrupo):
        if self.primero is None:
            self.primero=nodo_grupo(CGrupo)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_grupo(CGrupo)

    
    def eliminar_grupo(self,tiempo):
        actual = self.primero
        anterior = None
        while actual and actual.CGrupo.tiempo != tiempo:
            anterior=actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None


    def encontrar_coincidencias(self):
        coincidencia = "" 

        while self.primero:
            actual = self.primero  
            temp_coincidencia = ""        
        
            while actual:
                if actual.CGrupo.grupo == self.primero.CGrupo.grupo:
                    temp_coincidencia+=(str(actual.CGrupo.tiempo))+","  
                actual=actual.siguiente
            
            buffer=""
            for digito in temp_coincidencia:
                if digito.isdigit():
                    buffer+=digito
                else:
                    if buffer!="":
                        self.eliminar_grupo(int(buffer))
                        buffer=""
                    else:
                        buffer=""
            coincidencia+=temp_coincidencia+"--"
        return coincidencia  


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

