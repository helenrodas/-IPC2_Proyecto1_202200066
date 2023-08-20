import xml.etree.ElementTree as ET
from listaSimple import listaSimple
from lista_senales import lista_senales
from CSenal import CSenal
from CDato import CDato
from test import test


lista_Simple = listaSimple()
lista_senal = lista_senales()
test_handler = test()

class readFile():
    
    def cargarXml(self):
        try:
            with open('ejemploxml.xml', encoding='utf-8') as xml_file:
                root = ET.fromstring(xml_file.read())
                NodoPadre = root.findall('senal')  
                for nodo in NodoPadre:
                    # prueba1= listaSimple()
                    # prueba1.A = nodo.get('A')
                    # prueba1.t=nodo.get('t')
                    # prueba1.Nombre = nodo.get('nombre')  
                    

                    nombre_prueba = nodo.get('nombre')  
                    tiempo_senal = nodo.get('t')
                    amplitud_senal = nodo.get('A')
                    
                    
                    
                    nodos_hijo = nodo.findall('dato') 
                    
                    # print(f"Prueba: {nombre_prueba}")
                    
                    # print("------------------------------")
                    self.evaluar_nodos(nodos_hijo, int(amplitud_senal), int(tiempo_senal))
                    
                    lista_senal.insertar(CSenal(nombre_prueba,tiempo_senal,amplitud_senal,lista_Simple))
                    lista_senal.imprimir_lista()
                    
                    lista_senal.grafica_mi_lista_original()
                    #prueba1.imprimir_lista()
                    # lista_Simple.imprimir_lista()  # Imprimir la lista de la prueba actual
                    print("------------------------------")
                    
                    
        except Exception as err:
            print("Error:", err)
            

    def convertir_binario(self,valor_dato):
        if  valor_dato != "0":
            valorBinario = "1"
            
        else:                        
            valorBinario = valor_dato
        return valorBinario

    
    def evaluar_nodos(self, lista_nodos, amplitud_senal, tiempo_senal):
        for tiempo in range(1, tiempo_senal + 1):
            found_amps = ""
            for i in range(1, amplitud_senal + 1):
            
                for nodo in lista_nodos:
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

                lista_Simple.insertar(nodoDato)

