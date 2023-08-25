from nodo_senal import nodo_senal
from listaSimple import listaSimple
from CPatron import CPatron
from lista_patrones import lista_patrones

class lista_senales:
    def __init__(self):
        self.primero=None
        self.Nombre=""
        self.t=""
        self.A=""
        self.listaSimple=listaSimple
        self.contador_matrices=0
            
    def insertar(self,CSenal):
        if self.primero is None:
            self.primero=nodo_senal(CSenal)
            self.contador_matrices+=1
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_senal(CSenal)
        self.contador_matrices+=1
    
    
    def imprimir_lista(self):
        print("Total matrices almacenadas: " , self.contador_matrices)
        print("")
        
        if self.contador_matrices <= 0:
            print("-----------------------------")
            print("No hay datos para mostrar")
            print("-----------------------------")
            return
        else:
            print("Realizando operaciones...")
            print("")
            nombre_temporal = None
            actual = self.primero
            while actual != None:
                if actual.CSenal.nombre != nombre_temporal:
                    print("---------------------------------------------")
                    print(f"nombre: {actual.CSenal.nombre}, Tiempo: {actual.CSenal.tiempo_senal}, Amplitud: {actual.CSenal.amplitud_senal}")
                    print("---------------------------------------------")
                    nombre_temporal = actual.CSenal.nombre
                actual.CSenal.listaSimple.imprimir_lista()
                
                actual = actual.siguiente
    
    
    def imprimir_lista_binaria(self):
        actual = self.primero
        while actual != None:
            actual.CSenal.listaSimple.imprimir_lista_bin()
            actual = actual.siguiente
        print("---------------------------------------")
        print("")
        
        
    def buscar_nombre(self,nombre):
        actual = self.primero
        verificar = False

        while actual:
            if actual.CSenal.nombre == nombre:
                verificar = True
                break
            actual = actual.siguiente

        if verificar:
                actual.CSenal.listaSimple.generar_grafica(actual.CSenal.nombre,str(actual.CSenal.amplitud_senal),str(actual.CSenal.tiempo_senal))
                aux=aux.siguiente
        else:
            print("Nombre no encontrado!")
    
    
    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.CSenal.listaSimple.generar_grafica(actual.CSenal.nombre,
                                                    str(actual.CSenal.amplitud_senal),
                                                    str(actual.CSenal.tiempo_senal))
            #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente
    
    def eliminar_datos(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
            self.contador_matrices-=1
    
    
    def calcular_los_patrones(self,nombre):
        # recorremos la lista de carceles hasta encontrar una coincidencia
        actual = self.primero
        while actual != None:
        # Si entra al if, es por que encontramos la carcel que queremos
            if actual.CSenal.nombre==nombre:
                # Obtenemos sus patrones
                actual.CSenal.lista_grupos = actual.CSenal.listaSimple.devolver_patrones_por_nivel(actual.CSenal.lista_grupos)
                # Imprimimos todos sus patrones
                actual.CSenal.lista_grupos.recorrer()
                # obtenemos los grupos
                lista_grupos_temporal=actual.CSenal.lista_grupos
                grupos_sin_analizar=lista_grupos_temporal.encontrar_coincidencias()
                # Este es un string, por ejemplo "1,2--3,5--4"
                print(grupos_sin_analizar)
                # por cada grupo recorrer la matriz original e ir devolviendo las coordenadas especificadas
                #recordando que por cada coincidencia encontrada, se va borrando para dejar solo las que no tienen grupo.
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.CSenal.listaSimple.devolver_cadena_del_grupo(buffer)
                        actual.CSenal.lista_patrones.insertar_dato(CPatron(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.CSenal.lista_patrones.recorrer_e_imprimir_lista()

                return
            actual=actual.siguiente
        print ("No se encontró la Senal")