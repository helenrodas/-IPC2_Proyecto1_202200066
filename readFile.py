import xml.etree.ElementTree as ET
from listaSimple import listaSimple
from lista_senales import lista_senales
from CSenal import CSenal
from CDato import CDato
from lista_grupos import lista_grupos
from CGrupo import CGrupo
from lista_patrones import lista_patrones
from lista_datos_suma import lista_datos_suma


class readFile():
    
    def __init__(self):
        self.lista_senal_temporal = lista_senales()
        self.lista_dato_temporal = listaSimple()
    
    def cargarXml(self,ruta):
        try:
            with open(ruta+".xml", encoding='utf-8') as xml_file:
                root = ET.fromstring(xml_file.read())
                NodoPadre = root.findall('senal') 
                self.lista_senal_temporal = lista_senales()
                for nodo in NodoPadre:
                    nombre_prueba = nodo.get('nombre')  
                    tiempo_senal = nodo.get('t')
                    amplitud_senal = nodo.get('A')
                    
                    nodos_hijo = nodo.findall('dato') 
                    self.lista_dato_temporal = listaSimple()
                    lista_grupos_temp = lista_grupos()
                    lista_patrones_temp = lista_patrones()
                    lista_datos_suma_temp = lista_datos_suma()
                    
                    if self.validacion_size(tiempo_senal,amplitud_senal) == True:
                    
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

                        self.lista_senal_temporal.actualizar_matriz(nombre_prueba)
                        self.lista_senal_temporal.insertar(CSenal(nombre_prueba,tiempo_senal,amplitud_senal,self.lista_dato_temporal,lista_grupos_temp,lista_patrones_temp,lista_datos_suma_temp))
                        self.lista_senal_temporal.calcular_patrones(nombre_prueba,lista_datos_suma_temp)
                        self.lista_senal_temporal.actualizar(lista_datos_suma_temp,nombre_prueba)
                        
                        
                    else:
                        print("Archivo no cumple con requerimientos")
                print("Finalizado!")
        except Exception as err:
            print("Error:", err)
            

    def convertir_binario(self,valor_dato):
        if  valor_dato != "0":
            valorBinario = "1"
            
        else:                        
            valorBinario = valor_dato
        return valorBinario
    
    def validacion_size(self,t, A):
        t = int(t)
        A = int(A)
        if t > 0 and t <= 3600 and A > 0 and A <= 130:
            return True
        else:
            return False
    
    def mostrar_proceso(self):
        patrones = lista_patrones()
        if self.lista_senal_temporal.imprimir_lista() == None:
            return
        else:
            print("")
            self.lista_dato_temporal.imprimir_lista_bin()
            print("")
            patrones.imprimir_proceso()
            print("")
            print("-------------------------------")
            print("Proceso Terminado exitosamente")
    
    def inicializar_sistema(self):
        self.lista_senal_temporal.eliminar_datos()
        
    def crear_patrones(self,nombre):
        self.lista_senal_temporal.calcular_patrones(nombre)
    
    def generar_grafica(self,nombre,nombre_de_grafica):
        self.lista_senal_temporal.generar_grafica_normal(nombre,nombre_de_grafica)

    def generar_reducida_reducida(self,nombre,nombre_de_grafica):
        self.lista_senal_temporal.generar_grafica_reducida(nombre,nombre_de_grafica)
    
    def eliminar_lista(self):
        self.lista_senal_temporal.eliminar_lista_nodo()

    def crear_xml(self,nombre):
        self.lista_senal_temporal.generar_archivo_xml(nombre)
        
