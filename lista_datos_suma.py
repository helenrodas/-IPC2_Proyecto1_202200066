from nodo_datos_suma import nodo_datos_suma

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
            while actual.siguiente != None:
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
        
    # def generar_grafica(self,nombre,amplitud,tiempo):
    #     f = open('bb.dot','w')
    #     # configuraciones del grafo
    #     text ="""
    #         digraph G {"Amplitud="""+amplitud+"""","Tiempo="""+tiempo+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
    #         subgraph cluster1 {fillcolor="blue:red" style="filled"
    #         node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
    #         a0 [ label=<
    #         <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
    #     actual = self.primero
    #     sentinela_de_filas=actual.CDato.tiempo #iniciaria en 1
    #     fila_iniciada=False
    #     while actual != None:
    #         # Si mi fila actual es diferente a la que viene
    #         if  sentinela_de_filas!=actual.CDato.tiempo:
    #             #print(sentinela_de_filas,actual.celda.nivel,"hola")
    #             sentinela_de_filas=actual.CDato.tiempo
    #             fila_iniciada=False
    #             # Cerramos la fila
    #             text+="""</TR>\n"""  
    #         if fila_iniciada==False:
    #             fila_iniciada=True
    #             #Abrimos la fila
    #             text+="""<TR>"""  
    #             text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.CDato.valor)+"""</TD>\n"""
    #         else:
    #             text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.CDato.valor)+"""</TD>\n"""
    #         actual = actual.siguiente
    #     text+=""" </TR></TABLE>>];
    #             }
    #             }\n"""
    #     f.write(text)
    #     f.close()
    #     os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    #     os.system('dot -Tpng bb.dot -o grafica.png')
    #     print("terminado")