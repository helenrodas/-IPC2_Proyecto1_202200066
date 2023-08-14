import xml.etree.ElementTree as ET
from listaSimple import listaSimple
from CDato import CDato
from listaSimpleMatriz import listaSimpleMatriz

listaSimple_handler = listaSimple()
listaSimpleMatriz_handler = listaSimpleMatriz()

class readFile():

    def __init__(self) :
        self.contador = 1

    def validar_A(self,A,t):
        if int(A) == self.contador:
            self.contador += 1
        else:
            AFaltante = self.contador
            self.contador = (self.contador % 4) +1
            AFaltanteAsString = str(AFaltante)
            print(f" Falta un dato en t: {t}, A: {AFaltanteAsString}")
            
            

    
    def cargarXml(self):
        try:
            with open('ejemploxml.xml', encoding='utf-8') as xml_file:
                xml_data = ET.fromstring(xml_file.read())
                primeraLinea = xml_data.findall('senal')  

                for data in primeraLinea:
                    nombre = data.get('nombre')  
                    tiempo = data.get('t')
                    amplitud = data.get('A')
                    print(len(primeraLinea))
                    print(f"Nombre Prueba: {nombre}")
                    print(f"# Columnas Tiempo: {tiempo}")
                    print(f"# Filas Amplitud: {amplitud}")

                    listaDatos = data.findall('dato')  
                    
                    for data in listaDatos:
                        t = data.get('t')  
                        A = data.get('A')  
                        valor = data.text

                        self.validar_A(A,t)

                        valorASInt = int(valor)
                        if valorASInt != 0:
                            valorASInt = 1
                            valorBinarioAsString = str(valorASInt)
                        else:
                            valorASInt = 0
                            valorBinarioAsString = str(valorASInt)
                        nodoDato = CDato(nombre,t,A,valor, valorBinarioAsString)
                        listaSimple_handler.insertar(nodoDato)
#                    listaSimpleMatriz_handler.insertarMatrices(listaSimple_handler)
                    listaSimple_handler.recorrer()
                    print("------------Lista Binaria------------")
                    listaSimple_handler.recorrerListaBinaria()
#                   print("------------Lista Matrices------------")
#                    listaSimpleMatriz_handler.recorrerListaMatrices()
        except Exception as err:
            print("Error:", err)


    
        