from nodo_senal import nodo_senal
from listaSimple import listaSimple
from CPatron import CPatron
from lista_patrones import lista_patrones
from lista_datos_suma import lista_datos_suma
from CDatosSuma import CDatosSuma
import xml.etree.ElementTree as ET
import os

class lista_senales:
    def __init__(self):
        self.primero=None
        self.Nombre=""
        self.t=""
        self.A=""
        self.grupos = ""
        self.listaSimple=listaSimple
        self.contador_matrices=0
        self.ultimo=None
            
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
    
    
    # def recorrer_e_imprimir_lista(self):
    #     print("Total matrices Almacenadas: ",self.contador_matrices)
    #     print("")
    #     print("")
    #     print("*******************************************************************************************")
    #     actual = self.primero
    #     while actual != None:
    #         print("Nombre:",actual.CSenal.nombre,"Amplitud:",actual.CSenal.amplitud_senal,"Tiempo:",actual.carcel.tiempo_senal)
    #         # actual.carcel.lista_celdas.recorrer_e_imprimir_lista()
    #         actual.CSenal.lista_patrones.recorrer_e_imprimir_lista_patrones()
    #         actual = actual.siguiente
    #     print("")
    #     print("")
    #     print("")
    #     print("*******************************************************************************************")
    #     print("")
        
    
    def imprimir_lista(self):
        if self.contador_matrices <= 0:
            print("-----------------------------")
            print("No hay datos...")
            print("-----------------------------")
            return None
        else:
            print("Realizando operaciones...")
            print("")
            actual = self.primero
            actual.CSenal.listaSimple.imprimir_lista()
            return True

        
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
                actual=actual.siguiente
        else:
            print("Nombre no encontrado!")
            
    
    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.CSenal.listaSimple.generar_grafica(actual.CSenal.nombre,
                                                    str(actual.CSenal.amplitud_senal),
                                                    str(actual.CSenal.tiempo_senal))
            actual=actual.siguiente
    
    
    def eliminar_datos(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
            self.contador_matrices-=1
    
    
    def calcular_patrones(self,nombre,lista_suma):
        actual = self.primero
        while actual != None:
            if actual.CSenal.nombre==nombre:
                actual.CSenal.lista_grupos = actual.CSenal.listaSimple.devolver_patrones_por_nivel(actual.CSenal.lista_grupos)

                lista_grupos_temporal=actual.CSenal.lista_grupos

                grupos_sin_analizar=lista_grupos_temporal.encontrar_coincidencias()

                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.CSenal.listaSimple.devolver_cadena_del_grupo(buffer)
                        
                        actual.CSenal.lista_patrones.insertar_dato(CPatron(buffer,cadena_grupo,actual.CSenal.lista_patrones.get_contador()))
                        
                        self.sumar_grupo(actual.CSenal.listaSimple,actual.CSenal.amplitud_senal,buffer,actual.CSenal.lista_patrones.getSize(),lista_suma)
                        
                        buffer=""
                    else:
                        buffer=""
                return
            actual=actual.siguiente
        print ("No se encontraron datos")
        
        
    def actualizar_matriz(self,nombre):
        data = None
        actual = self.primero
        while actual:
            if actual.CSenal.nombre == nombre:
                if data is None:
                    self.primero = actual.siguiente
                    print("Matriz Actualizada....")
                else:
                    data.siguiente = actual.siguiente 
                    print("Matriz Actualizada....")
                actual = actual.siguiente
            else:
                data = actual   
                actual = actual.siguiente
                
    
    def sumar_grupo(self, lista_datos, amplitud, grupo,cont,lista_suma):
            temp_suma = 0
            contador = 0
            resultadoAsString = ""
            count = grupo.count(',')
            for i in range(1, int(amplitud)+1):
                for datos_lista in lista_datos:
                    if self.control(str(datos_lista.CDato.tiempo),grupo) and int(datos_lista.CDato.amplitud) == i:
                        temp_suma = temp_suma + int(datos_lista.CDato.valor)
                        contador += 1
                        if contador == count:
                            resultadoAsString+=str(temp_suma)+","
                            lista_suma.insertar(CDatosSuma(datos_lista.CDato.amplitud,grupo, temp_suma,cont ))
                contador = 0
                temp_suma = 0
    
    def control(self,tiempo,grupo_tiempos):
        ini = 0
        stop = 0
        while stop <= len(grupo_tiempos):
            if stop == len(grupo_tiempos) or grupo_tiempos[stop] == ',':
                tiempo_actual = grupo_tiempos[ini:stop]
                if tiempo_actual == tiempo:
                    return True
                ini = stop + 1
            stop += 1
        return False
    
    def generar_grafica_normal(self,nombre,nombre_archivo):
        actual = self.primero
        verificar = False

        while actual:
            if actual.CSenal.nombre == nombre:
                verificar = True
                break
            actual = actual.siguiente

        if verificar:
                actual.CSenal.listaSimple.generar_grafica(actual.CSenal.nombre,str(actual.CSenal.amplitud_senal),str(actual.CSenal.tiempo_senal),nombre_archivo)
                actual=actual.siguiente
        else:
            print("no se encontro en la lista")
    
    
    def generar_grafica_reducida(self,nombre,nombre_archivo):
        actual = self.primero
        verificar = False

        while actual:
            if actual.CSenal.nombre == nombre:
                verificar = True
                break
            actual = actual.siguiente

        if verificar:
                actual.CSenal.lista_datos_suma.grafica_sumas(actual.CSenal.nombre,str(actual.CSenal.amplitud_senal),nombre_archivo)
                actual=actual.siguiente
        else:
            print("no se encontro en la lista")
        
    def generar_grafica_bin(self,nombre,nombre_archivo):
        actual = self.primero
        verificar = False

        while actual:
            if actual.CSenal.nombre == nombre:
                verificar = True
                break
            actual = actual.siguiente

        if verificar:
                actual.CSenal.listaSimple.generar_grafica_bin(actual.CSenal.nombre,str(actual.CSenal.amplitud_senal),str(actual.CSenal.tiempo_senal),nombre_archivo)
                
                actual=actual.siguiente
        else:
            print("no se encontro en la lista")
    
    def eliminar_lista_nodo(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
    
    
    
    def actualizar(self,lista_temporal_suma,nombre):
        actual = self.primero
        while actual:
            if actual.CSenal.nombre ==  nombre:
                actual.CSenal.lista_datos_suma = lista_temporal_suma
                return
            actual = actual.siguiente
    
    def generar_archivo_xml(self,nombre):
        senales_reducidas = ET.Element("senalesReducidas")
        actual = self.primero

        while actual:
            senal = ET.SubElement(senales_reducidas, "senal", nombre=f"{actual.CSenal.nombre}", A=f"{actual.CSenal.amplitud_senal}")
            num_grupos = actual.CSenal.lista_patrones

            for grup in num_grupos:
                grupo = ET.SubElement(senal, "grupo",grupo=f"{grup.CPatron.grupo_num}" )
                tiempos = ET.SubElement(grupo, "tiempos"  )
                tiempos.text = grup.CPatron.grupo_tiempos

                datos_gru = ET.SubElement(grupo, "datosGrupo")
                dato_grupos_suma = actual.CSenal.lista_datos_suma
                for data in dato_grupos_suma:
                    if data.CDatosSuma.grupo == grup.CPatron.grupo_num:
                        dato = ET.SubElement(datos_gru, "dato", A=f"{data.CDatosSuma.amplitud}")
                        dato.text = str(data.CDatosSuma.cadena_suma)

            actual = actual.siguiente
            
        self.ajustes_xml(senales_reducidas)
        tree = ET.ElementTree(senales_reducidas)
        print("Proceso terminado correctamente...")
        tree.write(f"{nombre}.xml", encoding="utf-8", xml_declaration=True)

    def ajustes_xml(self,element, indent='    '):
        queue = [(0, element)] 
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1) 
            if queue:
                element.tail = '\n' + indent * queue[0][0]  
            else:
                element.tail = '\n' + indent * (level-1)  
            queue[0:0] = children
        
        
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