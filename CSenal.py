class CSenal:
    def __init__(self,nombre,tiempo_senal,amplitud_senal,listaSimple,lista_grupos,lista_patrones,lista_datos_suma):
        self.nombre = nombre
        self.tiempo_senal = tiempo_senal
        self.amplitud_senal = amplitud_senal
        self.listaSimple = listaSimple #Guarda valores normal y binario
        self.lista_grupos = lista_grupos # Guarda los grupos con valor binario
        self.lista_patrones = lista_patrones # Guardar los grupos con valor normal
        self.lista_datos_suma = lista_datos_suma
        