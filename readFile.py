import xml.etree.ElementTree as ET
from listaSimple import listaSimple
from lista_senales import lista_senales
from CSenal import CSenal
from CDato import CDato
from lista_grupos import lista_grupos
from CGrupo import CGrupo
from lista_patrones import lista_patrones


# lista_Simple = listaSimple()
# lista_senal = lista_senales()
# lista_dato_temporal = listaSimple()

class readFile():
    
    def __init__(self):
        self.lista_senal_temporal = lista_senales()
        self.lista_dato_temporal = listaSimple()
    
    def cargarXml(self):
        try:
            with open('datosPrueba.xml', encoding='utf-8') as xml_file:
                root = ET.fromstring(xml_file.read())
                NodoPadre = root.findall('senal') 
                self.lista_senal_temporal = lista_senales()
                for nodo in NodoPadre:
                    nombre_prueba = nodo.get('nombre')  
                    tiempo_senal = nodo.get('t')
                    amplitud_senal = nodo.get('A')
                    
                    self.lista_dato_temporal = listaSimple()
                    nodos_hijo = nodo.findall('dato') 
                    lista_grupos_temp = lista_grupos()
                    lista_patrones_temp = lista_patrones()
                    
                    for tiempo in range(1, int(tiempo_senal) + 1):
                        found_amps = ""
                        for i in range(1, int(amplitud_senal) + 1):
                        
                            for nodo in nodos_hijo:
                                amp = nodo.get('A')
                                tiempo_en_nodo = nodo.get('t')
                                valor=nodo.text
                                valor_binario=self.convertir_binario(valor)
                                
                                if tiempo_en_nodo == str(tiempo) and amp == str(i):
                                    found_amps += amp
                                    break
                            
                            if str(i) not in found_amps:
                                nodoDato = CDato(tiempo,i,0,0)

                            else:
                                nodoDato = CDato(tiempo,i,valor, valor_binario)

                            self.lista_dato_temporal.insertar(nodoDato)
                    # self.crear_grupo(self.lista_dato_temporal,tiempo_senal)
                    self.lista_senal_temporal.insertar(CSenal(nombre_prueba,tiempo_senal,amplitud_senal,self.lista_dato_temporal,lista_grupos_temp,lista_patrones_temp))
                    self.lista_senal_temporal.imprimir_lista_binaria()
                    self.crear_patrones(nombre_prueba)
                    # self.lista_senal_temporal.calcular_los_patrones(nombre_prueba)
                    
                    # self.crear_grupos(self.lista_dato_temporal,tiempo_senal)
                print("Archivo Cargado!")

        except Exception as err:
            print("Error:", err)
            

    def convertir_binario(self,valor_dato):
        if  valor_dato != "0":
            valorBinario = "1"
            
        else:                        
            valorBinario = valor_dato
        return valorBinario
    
    def imprimir_nodos(self):
        self.lista_senal_temporal.imprimir_lista()
        self.lista_senal_temporal.imprimir_lista_binaria()
    
    def mostrar_grafica(self,nombre):
        self.lista_senal_temporal.buscar_nombre(nombre)
        # self.lista_senal_temporal.grafica_mi_lista_original()
    
    def inicializar_sistema(self):
        self.lista_senal_temporal.eliminar_datos()
        
    def crear_patrones(self,nombre):
        self.lista_senal_temporal.calcular_los_patrones(nombre)
        
    
    # def crear_grupos(self,lista_datos,tiempo_senal):
    #     lista_grupos_handler = lista_grupos()
    #     for tiempo in range(1, int(tiempo_senal) + 1):
    #         grupo_binario = ""
                        
    #         for nodo in lista_datos:
    #             tiempo_en_nodo = nodo.CDato.tiempo
    #             valor_binario=nodo.CDato.valorBinario
                    
    #             if tiempo == int(tiempo_en_nodo):
    #                 grupo_binario += str(valor_binario)

    #         grupo = CGrupo(grupo_binario,tiempo)
    #         lista_grupos_handler.insertar(grupo)
    #         grupo_binario = ""
    #     lista_grupos_handler.imprimir_lista()
        # lista_grupos_handler.agrupar()
            # print(grupo_binario)


    # def evaluar_nodos(self, lista_nodos, amplitud_senal, tiempo_senal):
    #     for tiempo in range(1, tiempo_senal + 1):
    #         found_amps = ""
    #         for i in range(1, amplitud_senal + 1):
            
    #             lista_dato_temporal = listaSimple()
    #             for nodo in lista_nodos:
    #                 amp = nodo.get('A')
    #                 tiempo_en_nodo = nodo.get('t')
    #                 valor=nodo.text
    #                 valor_binario=self.convertir_binario(valor)
                    
    #                 if tiempo_en_nodo == str(tiempo) and amp == str(i):
    #                     found_amps += amp
    #                     break
            
    #             if str(i) not in found_amps:
    #                 nodoDato = CDato(tiempo,i,0,0)

    #             else:
    #                 nodoDato = CDato(tiempo,i,valor, valor_binario)

    #             lista_dato_temporal.insertar(nodoDato)

