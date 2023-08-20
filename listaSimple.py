from nodo import nodo
import sys
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

    def generar_grafica(self,nombre,amplitud,tiempo):
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
        os.system('dot -Tpng bb.dot -o grafica.png')
        print("terminado")
