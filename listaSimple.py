from nodo import nodo
from CGrupo import CGrupo
import os

class listaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
            
    def insertar(self,CDato):
        if self.primero is None:
            self.primero=nodo(CDato)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo(CDato)
            
    def imprimir_lista(self):
        print("------------Lista Normal------------")
        actual = self.primero
        while actual != None:
            print(f"t: {actual.CDato.tiempo}, A: {actual.CDato.amplitud}, Valor: {actual.CDato.valor}")
            actual = actual.siguiente

    def imprimir_lista_bin(self):
        actual = self.primero
        print("------------Lista Binaria------------")
        while actual != None:
            print(f"t: {actual.CDato.tiempo}, A: {actual.CDato.amplitud}, Valor: {actual.CDato.valorBinario}")
            actual = actual.siguiente

    def devolver_patrones_por_nivel(self,lista_grupos):
        actual = self.primero
        sentinela_de_filas=actual.CDato.tiempo #iniciaria en 1
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
            if  sentinela_de_filas!=actual.CDato.tiempo:
                fila_iniciada=False
                lista_grupos.insertar(CGrupo(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                sentinela_de_filas=actual.CDato.tiempo

            if fila_iniciada==False:
                fila_iniciada=True
                recolector_patron+=str(actual.CDato.valorBinario)+"-"
            else:
                recolector_patron+=str(actual.CDato.valorBinario)+"-"
            actual = actual.siguiente
        lista_grupos.insertar(CGrupo(sentinela_de_filas,recolector_patron))
        return lista_grupos

    def generar_grafica(self,nombre,amplitud,tiempo,nombre_archivo):
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"Amplitud="""+amplitud+"""","Tiempo="""+tiempo+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.CDato.tiempo #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.CDato.tiempo:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=actual.CDato.tiempo
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.CDato.valor)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.CDato.valor)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o {nombre_archivo}.png')
        print("terminado")

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
        
    def devolver_cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        # viene un parametro llamado grupo, es un string con este formato "1,2"
        # recorremos caracter por caracter
        for digito in grupo:
        #si es digito
            if digito.isdigit():
                #añadimos al buffer
                buffer+=digito
            else:
                # si no es buffer, lo vaciamos
                string_temporal=""
                #recorremos la lista y recuperamos los valores para este grupo
                actual = self.primero
                while actual != None:
                    # si encontramos coincidencia del digito y el nivel , obtenemos su valor
                    if actual.CDato.tiempo==int(buffer):
                        string_temporal+=str(actual.CDato.valor)+","
                    actual = actual.siguiente

                string_resultado+=string_temporal+"\n"
                buffer=""
        #devolvemos el string resultado
        return string_resultado

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return 
    
    def actualizar_datos(self,t,A,valor,valorBinario):
        actual = self.primero

        while actual:
            actual.CDato.tiempo = t
            actual.CDato.amplitud = A
            actual.CDato.valor = valor
            actual.CDato.valorBinario = valorBinario
            actual = actual.siguiente