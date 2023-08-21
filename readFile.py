import xml.etree.ElementTree as ET
from listaSimple import listaSimple
from lista_senales import lista_senales
from CSenal import CSenal
from CDato import CDato
from test import test


# lista_Simple = listaSimple()
# lista_senal = lista_senales()
test_handler = test()
# lista_dato_temporal = listaSimple()

class readFile():
    
    def __init__(self):
        self.lista_senal_temporal = lista_senales()
        self.lista_dato_temporal = listaSimple()
    
    def cargarXml(self):
        try:
            with open('ejemploxml.xml', encoding='utf-8') as xml_file:
                root = ET.fromstring(xml_file.read())
                NodoPadre = root.findall('senal') 
                self.lista_senal_temporal = lista_senales()
                for nodo in NodoPadre:
                    nombre_prueba = nodo.get('nombre')  
                    tiempo_senal = nodo.get('t')
                    amplitud_senal = nodo.get('A')
                    
                    self.lista_dato_temporal = listaSimple()
                    nodos_hijo = nodo.findall('dato') 
                    
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

                    self.lista_senal_temporal.insertar(CSenal(nombre_prueba,tiempo_senal,amplitud_senal,self.lista_dato_temporal))
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
    
    def mostrar_grafica(self,nombre):
        self.lista_senal_temporal.buscar_nombre(nombre)
        # self.lista_senal_temporal.grafica_mi_lista_original()
    
    def inicializar_sistema(self):
        self.lista_senal_temporal.eliminar_datos()

    
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

