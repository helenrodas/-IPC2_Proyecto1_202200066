import os
from readFile import readFile
from listaSimple import listaSimple
from lista_senales import lista_senales

readFile_handler = readFile()
lista_Simple = listaSimple()
lista_senal_handler = lista_senales()

class main:
    def __init__(self):
        self.ruta = ""

    def clear(self):
        os.system('cls')


    def cargarArchivo(self):
        self.clear()
        print("------------Opcion Cargar Archivo------------")
        #ruta = input("Ingrese ruta del archivo: ")
        #clear()
        readFile_handler.cargarXml()
        
        
        # readFile_handler.imprimir_lista()
        #readFile_handler.leer_archivo_inv(ruta)
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()


    def procesarArchivo(self):
        self.clear()
        #readFile_handler.leer_archivo_mov(ruta)
        # print("Realizando operaciones")
        print("")
        readFile_handler.imprimir_nodos()
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()
        
        
    def generador_grafi(self):
            print("")
            print("--------------------------------------")
            nombre =  input("ingrese el nombre de la matriz que quiere graficar: ")
            print("--------------------------------------")
            print("1. Grafica normal")
            print("2. Grafica reducida")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                nombre_de_grafica = input("Ingrese el nombre que quiere guarda la matriz: ")
                readFile_handler.generar_grafica(nombre,nombre_de_grafica)
            elif opcion == 2:
                nombre_de_grafica_reducida = input("Ingrese el nombre que quiere guarda la matriz: ")
                readFile_handler.generar_reducida_reducida(nombre,nombre_de_grafica_reducida)
            else:
                print("opcion no valida")
            
            print("")

    def inicializar_sistema(self):
            print("")
            print("--------------------------------------")
            self.ruta = ""
            print("Elimando la lista")
            readFile_handler.eliminar_lista()
            print("")

    def prueba_grafica(self):
        readFile_handler.grafica_sumados()

    def grafica_reducida(self):
        readFile_handler.generar_grafica_reducida()

    def crear_xml(self):
            print("")
            print("--------------------------------------")
            nombre_arhivo = input("ingrese el nombre para su arhivo: ")
            print("Generando archivo...")
            readFile_handler.crear_xml(nombre_arhivo)

    def archivoDeSalida(self):
        self.clear()
        # ruta = input("Ingrese una ruta especifica: ")
        # clear()
        #readFile_handler.crear_archivo_txt(ruta)
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()

    def matriz_recorrer(self):
        print("")
        print("--------------------------------------")
        print("iniciando proceso")
        readFile_handler.listados()

    def datosEstudiante(self):
        self.clear()
        print("---------------------------Datos Estudiante---------------------------")
        print("> Nombre: Helen Janet Rodas Castro")
        print("> Carne: 202200066")
        print("> Curso: Introduccion a la Programacion y Computacion 2 Seccion ""D"" ")
        print("> Carrera: Ingenieria en Ciencias y Sistemas")
        print("> Semestre: 4to. Semestre")
        print("----------------------------------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()


    def generarGrafica(self):
        self.clear()
        #readFile_handler.crear_archivo_txt(ruta)
        nombre_matriz = input("Ingrese nombre de la matriz a graficar: ")
        
        readFile_handler.mostrar_grafica(nombre_matriz)
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()


    def inicializarSistema(self):
        self.clear()
        #readFile_handler.crear_archivo_txt(ruta)
        print("Inicializando Programa...")
        readFile_handler.inicializar_sistema()
        print("-------------------------")
        print("Terminado")
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()

    def pruebaGrupos(self):
        # clear()
        print("------------------------------------")
        # readFile_handler.crear_patrones()
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()

    def salir():
        print("Programa finalizado")


    def menuInicial(self):
        print("")
        print("--------------------------------")
        print("---------Menu Principal---------")
        print("--------------------------------")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Grafica")
        print("6. Inicializar Sistema")
        print("7. Salir")
        print("")
        opcion=input("Ingrese una opción: ")
        if opcion=="1":
            try:
                self.cargarArchivo()
                self.menuInicial()
            except:
                self.clear()
                print("----Error! Archivo no encontrado----")
                self.menuInicial()
        elif opcion=="2":
            try:
                self.procesarArchivo()
                self.menuInicial()
            except:
                self.clear()
                print("----Error!----")
                self.menuInicial()
        elif opcion=="3":
            self.crear_xml()
            # archivoDeSalida()
            self.menuInicial()
            # try:
                
            # except:
            #     self.clear()
            #     print("----Error! Archivo no pudo ser creado----")
            #     self.menuInicial()
        elif opcion=="4":
            try:
                # self.pruebaGrupos()
                # datosEstudiante()
                self.matriz_recorrer()
                self.menuInicial()
            except:
                # clear()
                # print("----Error!----")
                self.menuInicial()
        elif opcion=="5":
            try:
                self.generador_grafi()
                # self.generarGrafica()
                self.menuInicial()
            except:
                # clear()
                print("-------------")
                self.menuInicial()
        elif opcion=="6":
            try:
                self.inicializarSistema()
                self.menuInicial()
            except:
                self.clear()
                print("----Error!----")
                self.menuInicial()
        elif opcion=="7":
            self.salir()
        else:
            self.clear()
            print("Indique una opción válida")
            self.menuInicial()

app_llamar = main()

app_llamar.menuInicial()