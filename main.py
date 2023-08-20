import os
from readFile import readFile
from listaSimple import listaSimple

readFile_handler = readFile()
lista_Simple = listaSimple()

def clear():
    os.system('cls')


def cargarArchivo():
    clear()
    print("------------Opcion Cargar Archivo------------")
    #ruta = input("Ingrese ruta del archivo: ")
    #clear()
    readFile_handler.cargarXml()
    # readFile_handler.imprimir_lista()
    #readFile_handler.leer_archivo_inv(ruta)
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()


def procesarArchivo():
    clear()
    #readFile_handler.leer_archivo_mov(ruta)
    print("Realizando operaciones")
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()
    


def archivoDeSalida():
    clear()
    ruta = input("Ingrese una ruta especifica: ")
    clear()
    #readFile_handler.crear_archivo_txt(ruta)
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()


def datosEstudiante():
    clear()
    print("---------------------------Datos Estudiante---------------------------")
    print("> Nombre: Helen Janet Rodas Castro")
    print("> Carne: 202200066")
    print("> Curso: Introduccion a la Programacion y Computacion 2 Seccion ""D"" ")
    print("> Carrera: Ingenieria en Ciencias y Sistemas")
    print("> Semestre: 4to. Semestre")
    print("----------------------------------------------------------------------")
    input("Presione enter para continuar...")
    clear()


def generarGrafica():
    clear()
    #readFile_handler.crear_archivo_txt(ruta)
    
    
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()


def inicializarSistema():
    clear()
    #readFile_handler.crear_archivo_txt(ruta)
    print("Iniciar...")
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()


def salir():
    print("Programa finalizado")


def menuInicial():
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
            cargarArchivo()
            menuInicial()
        except:
            clear()
            print("----Error! Archivo no encontrado----")
            menuInicial()
    elif opcion=="2":
        try:
            procesarArchivo()
            menuInicial()
        except:
            clear()
            print("----Error!----")
            menuInicial()
    elif opcion=="3":
        try:
            archivoDeSalida()
            menuInicial()
        except:
            clear()
            print("----Error! Archivo no pudo ser creado----")
            menuInicial()
    elif opcion=="4":
        try:
            datosEstudiante()
            menuInicial()
        except:
            clear()
            print("----Error!----")
            menuInicial()
    elif opcion=="5":
        try:
            generarGrafica()
            menuInicial()
        except:
            clear()
            print("----Error!----")
            menuInicial()
    elif opcion=="6":
        try:
            inicializarSistema()
            menuInicial()
        except:
            clear()
            print("----Error!----")
            menuInicial()
    elif opcion=="7":
        salir()
    else:
        clear()
        print("Indique una opción válida")
        menuInicial()


menuInicial()