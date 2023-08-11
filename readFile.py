import xml.etree.ElementTree as ET

class readFile():

    def cargarXml(self):
        try:
            with open('ejemploxml.xml', encoding='utf-8') as xml_file:
                xml_data = ET.fromstring(xml_file.read())
                lst_plants = xml_data.findall('senal')  # Cambié 'PLANT' a 'senal' según tu archivo XML
                for plant in lst_plants:
                    nombre = plant.get('nombre')  # Obtener el valor del atributo 'nombre'
                    tiempo = plant.get('t')
                    amplitud = plant.get('A')
                    print(f"Nombre: {nombre}")
                    print(f"Tiempo: {tiempo}")
                    print(f"Amplitud: {amplitud}")
                    datos = plant.findall('dato')  # Encontrar todos los elementos 'dato'
                    for dato in datos:
                        t = dato.get('t')  # Obtener el valor del atributo 't'
                        A = dato.get('A')  # Obtener el valor del atributo 'A'
                        valor = dato.text  # Obtener el contenido del elemento 'dato'
                        print(f"t: {t}, A: {A}, Valor: {valor}")
                    print("-------------------------------")
        except Exception as err:
            print("Error:", err)

