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
        ruta = input("Ingrese ruta del archivo: ")
        self.clear()
        readFile_handler.cargarXml(ruta)
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()


    def procesarArchivo(self):
        self.clear()
        print("")
        readFile_handler.mostrar_proceso()
        print("----------------------------------------------")
        input("Presione enter para continuar...")
        self.clear()
        
        
    def opcion_graficas(self):
            self.clear()
            print("---------------------------------------------")
            nombre =  input("ingrese el nombre de la matriz a graficar: ")
            print("---------------------------------------------")
            print("1. Grafica Matriz ordinaria")
            print("2. Grafica Matriz reducida")
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                nombre_de_grafica = input("Con que nombre desea guardar la grafica: ")
                readFile_handler.generar_grafica(nombre,nombre_de_grafica)
            elif opcion == 2:
                nombre_de_grafica_reducida = input("Con que nombre desea guardar la grafica: ")
                readFile_handler.grafica_reducida(nombre,nombre_de_grafica_reducida)
            else:
                print("opcion no valida")
            
            print("")

    def generar_xml(self):
            self.clear()
            print("--------------------------------------")
            nombre_arhivo = input("Ingrese nombre para crear arhivo xml: ")
            print("Generando archivo...")
            readFile_handler.crear_xml(nombre_arhivo)

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

    def reiniciarPrograma(self):
        self.clear()
        #readFile_handler.crear_archivo_txt(ruta)
        print("Reiniciando Programa...")
        readFile_handler.inicializar_sistema()
        print("-------------------------")
        print("Terminado!")
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
            try:
                self.generar_xml()
                self.menuInicial()
            except:
                self.clear()
                print("----Error! Archivo no pudo ser creado----")
                self.menuInicial()
        elif opcion=="4":
            try:
                self.datosEstudiante()
                self.menuInicial()
            except:
                self.clear()
                print("----Error!----")
                self.menuInicial()
        elif opcion=="5":
            try:
                self.opcion_graficas()
                self.menuInicial()
            except:
                self.clear()
                print("-------------")
                self.menuInicial()
        elif opcion=="6":
            try:
                self.reiniciarPrograma()
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

iniciar_programa = main()

iniciar_programa.menuInicial()