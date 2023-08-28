from nodo_datos_suma import nodo_datos_suma
import os

class lista_datos_suma:
    def __init__(self):
        self.primero = None
        self.contador_grupos=0
    
    def insertar_dato(self,CDatosSuma):
        if self.primero is None:
            self.primero = nodo_datos_suma(CDatosSuma)
            self.contador_grupos+=1
            return
        
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = nodo_datos_suma(CDatosSuma)
        self.contador_grupos+=1
    
    def recorrer_e_imprimir_lista(self):
        print("===========================================================================================")
        actual = self.primero
        while actual != None:
            print(" amplitud: ",actual.CDatosSuma.amplitud,"Tiempo: ",actual.CDatosSuma.tiempo, 
                "Cadena Suma:",actual.CDatosSuma.cadena_suma, "Grupo: ",actual.CDatosSuma.grupo)
            actual = actual.siguiente
        print("===========================================================================================")
        
        
    # def generar_grafica(self):
    #     texto = ""
    #     actual = self.primero

    #     sentinela = actual.CGrupo.grupo
        
    #     fila = False
    #     while actual != None:
            
    #         self.datos += actual.CGrupo.datos_grupo.generar_grafica(f"G = {actual.CGrupo.grupo} (t = {actual.CGrupo.tiempos})")
    #         actual = actual.siguiente
    #     texto += "\n"+self.datos+"\n"
    #     return texto
        
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

    def generar_grafica_sumas(self,nombre,amplitud,tiempo,nombre_archivo):
        f = open('bb.dot','w')

        text ="""
            digraph G {"Amplitud="""+amplitud+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.CDatosSuma.grupo
        fila_iniciada=False
        
        text+="""<TR><TD border="3"  bgcolor="lavender" gradientangle="315">"""+"Grupo="+str(actual.CDatosSuma.grupo)+" t="+str(actual.CDatosSuma.tiempo)+"""</TD>\n"""
        while actual != None:

            
            if sentinela_de_filas!=actual.CDatosSuma.grupo:
                
                sentinela_de_filas=actual.CDatosSuma.grupo
                
                fila_iniciada=False

                text+="""</TR>\n""" 
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+"Grupo="+str(actual.CDatosSuma.grupo)+" t="+str(actual.CDatosSuma.tiempo)+"""</TD>\n"""
            if fila_iniciada==False:
                fila_iniciada=True
                
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+str(actual.CDatosSuma.cadena_suma)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="lavender" gradientangle="315">"""+str(actual.CDatosSuma.cadena_suma)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o {nombre_archivo}.png")
        print("terminado...")