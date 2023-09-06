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
        print(">>>Generando Matriz...")
        
        

    def imprimir_lista_bin(self):
        print(">>>-Generando Matriz Binaria...")
        # # print("Total De cárceles almacenadas: ",self.contador_carceles)
        # print("")
        # print("")
        # print("*******************************************************************************************")
        # actual = self.primero
        # actual = self.primero
        # while actual != None:
        #     print(" T: ",actual.CDato.tiempo,"A: ",actual.CDato.amplitud," Valor Binario:",actual.CDato.valorBinario)
        #     actual = actual.siguiente
        # print("")
        # print("")
        # print("*******************************************************************************************")
        # print("")

    def devolver_patrones_por_nivel(self,lista_grupos):
        actual = self.primero
        sentinela_de_filas=actual.CDato.tiempo 
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
        text ="""
            digraph G {"Amplitud="""+amplitud+"""","Tiempo="""+tiempo+""""->" """+nombre+ """" bgcolor="#b6ccf2" style="filled"
            subgraph cluster1 {fillcolor="orange:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="orange:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.CDato.tiempo 
        fila_iniciada=False
        while actual != None:
            if  sentinela_de_filas!=actual.CDato.tiempo:
                sentinela_de_filas=actual.CDato.tiempo
                fila_iniciada=False
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
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
        os.system(f"dot -Tpng bb.dot -o {nombre_archivo}.png")
        print("")
        print("Grafica creada exitosamente")

    def generar_grafica_bin(self,nombre,amplitud,tiempo,nombre_archivo):
        f = open('bb.dot','w')
        text ="""
            digraph G {"Amplitud="""+amplitud+"""","Tiempo="""+tiempo+""""->" """+nombre+ """" bgcolor="#b6ccf2" style="filled"
            subgraph cluster1 {fillcolor="orange:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="orange:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.CDato.tiempo 
        fila_iniciada=False
        while actual != None:
            if  sentinela_de_filas!=actual.CDato.tiempo:
                sentinela_de_filas=actual.CDato.tiempo
                fila_iniciada=False
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.CDato.valorBinario)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.CDato.valorBinario)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o {nombre_archivo}.png")
        print("")
        print("Grafica de Patrones creada exitosamente!")

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
        for digito in grupo:
            if digito.isdigit():
                buffer+=digito
            else:
                string_temporal=""
                actual = self.primero
                while actual != None:
                    if actual.CDato.tiempo==int(buffer):
                        string_temporal+=str(actual.CDato.valor)+","
                    actual = actual.siguiente

                string_resultado+=string_temporal+"\n"
                buffer=""
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