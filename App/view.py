"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import graph as gr
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los puntos de Interconexión entre los Aeropuertos")
    print("3- Consultar la cantidad de clústeres entre dos aeropuertos")
    print("4- Consultar la ruta más corta entre dos ciudades")
    print("5- Consultar la mayor cantidad de ciudades que pueden visitarse con Millas de Viajero")
    print("6- Consultar el impacto causado por un aeropuerto cerrado")

catalog = None
airpfile = "airports-utf8-small.csv"
routefile = "routes-utf8-small.csv"
citiesfile = "worldcities.csv"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando el analizador ....")
        catalog = controller.init()
        print("\nCargando información de los archivos ....")
        controller.loadINFO(catalog, airpfile, routefile, citiesfile)
        
        aeropuertos = catalog["aeropuertos"]

        print("---------------------------------------------------------------------------")
        print("Cantidad de Aeropuertos Dirigidos: " + str(gr.numVertices(catalog['grafo_dirigido'])))
        print("Cantidad de Vuelos Dirigidos: " + str(gr.numEdges(catalog['grafo_dirigido'])))

        dirigidos = catalog["grafo_dirigido"]
        lista_dirigidos = gr.vertices(dirigidos)

        primero = lt.firstElement(lista_dirigidos)
        ultimo = lt.lastElement(lista_dirigidos)

        prim = mp.get(aeropuertos, primero)['value']
        ult = mp.get(aeropuertos, ultimo)['value']

        print("\nPrimer aeropuerto cargado: ")
        print("IATA: " + prim["IATA"] + "\nName: " + prim["Name"] + "\nciudad: " + prim["City"] + "\nPais: " + prim["Country"] + "\nLatitud: " + str(prim["Latitude"]) + "\nLongitud: " + str(prim["Longitude"]))
        print("\nUltimo aeropuerto cargado: ")
        print("IATA: " + ult["IATA"] + "\nName: " + ult["Name"] + "\nciudad: " + ult["City"] + "\nPais: " + ult["Country"] + "\nLatitud: " + str(ult["Latitude"]) + "\nLongitud: " + str(ult["Longitude"]))

        print("---------------------------------------------------------------------------")
        print("Cantidad de Aeropuertos No Dirigidos: " + str(gr.numVertices(catalog['grafo_nodirigido'])))
        print("Cantidad de Vuelos No Dirigidos: " + str(gr.numEdges(catalog['grafo_nodirigido'])))
        
        nodirigidos = catalog["grafo_nodirigido"]
        lista_nodirigidos = gr.vertices(nodirigidos)

        primero_n = lt.firstElement(lista_nodirigidos)
        ultimo_n = lt.lastElement(lista_nodirigidos)

        prim_n = mp.get(aeropuertos, primero_n)['value']
        ult_n = mp.get(aeropuertos, ultimo_n)['value']

        print("\nPrimer aeropuerto cargado: ")
        print("IATA: " + prim_n["IATA"] + "\nName: " + prim_n["Name"] + "\nciudad: " + prim_n["City"] + "\nPais: " + prim_n["Country"] + "\nLatitud: " + str(prim_n["Latitude"]) + "\nLongitud: " + str(prim_n["Longitude"]))
        print("\nUltimo aeropuerto cargado: ")
        print("IATA: " + ult_n["IATA"] + "\nName: " + ult_n["Name"] + "\nciudad: " + ult_n["City"] + "\nPais: " + ult_n["Country"] + "\nLatitud: " + str(ult_n["Latitude"]) + "\nLongitud: " + str(ult_n["Longitude"]))

        print("---------------------------------------------------------------------------")
        print("El numero de ciudades es: "+str(mp.get(catalog['ciudades'],"cantidad")['value'] ))
        print("El numero de ciudades no repetidas es: "+str(mp.size(catalog['ciudades'])))
        print("---------------------------------------------------------------------------")

    elif int(inputs[0]) == 2:
        lista = controller.mas_conexiones(catalog)
        i = lt.size(lista)
        j = 1

        while j <= 5:
            iata = lt.getElement(lista, i)
            print("-------------------------------------------------------")
            print("\nIATA: " + iata["IATA"] + "\nName: " + iata["Name"] + "\nciudad: " + iata["City"] + "\nPais: " + iata["Country"] 
            + "\nConexiones: " + str(iata["total"]) + "\nEntrada: " + str(iata["entrada"]) + "\nSalida: " + str(iata["salida"]))
            print("")

            i -= 1
            j += 1

    elif int(inputs[0]) == 3:
        print("\n----------------------Inputs----------------------")
        iata1 = input("\nEscriba el codigo IATA del aeropuerto 1: ")
        iata2 = input("Escriba el codigo IATA del aeropuerto 2: ")
        print("\n----------------------Outputs----------------------")
        total, conexion = controller.clusteres_trafico(catalog, iata1, iata2)
        print("El numerode Componentes Fuertemnte conectados es: " + str(total))
        if conexion == True:
            print("Los areropuertos están fuertemente conctados")
            print("")
        else:
            print("Los areropuertos NO están fuertemente conctados")
            print("")


    elif int(inputs[0]) == 4:
        print("Requerimiento 3")

    elif int(inputs[0]) == 5:
        print("Requerimiento 4")

    elif int(inputs[0]) == 6:
        print("\n----------------------Inputs----------------------")
        iata = input("\nEscribe el codigo IATA del aeropuerto fuera de funcionamiento: ")
        print("\n----------------------Outputs----------------------")
        lista = controller.efecto_aeropuerto(catalog, iata)
        tamano = lt.size(lista)
        print("\n Hay "+str(tamano)+" aeropuertos afectados por el cierre del aeropuerto " + str(iata))
        lst = lt.newList("ARRAY_LIST")
        
        if int(tamano) >= 6:
            i = 1
            print("Los primeros 3 aeropuertos afectados son: ")
            while i <= 3:
                aer = lt.getElement(lista, i)
                print("\nIATA: " + aer["IATA"] + "\nNombre: " + aer["Name"] + "\nCiudad: " + aer["City"] 
                    + "\nPaís: " + aer["Country"])
                
                ultimo = lt.lastElement(lista)
                lt.removeLast(lista)
                lt.addFirst(lst, ultimo)
                i+=1
            print("\n")
            print("Los ultimos 3 aeropuertos afectados son: ")
            for h in lt.iterator(lst):
                print("\nIATA: " + h["IATA"] + "\nNombre: " + h["Name"] + "\nCiudad: " + h["City"] 
                    + "\nPaís: " + h["Country"])
            
        elif int(tamano) == 1:
            aer = lt.getElement(lista,1)
            print("\nIATA: " + aer["IATA"] + "\nNombre: " + aer["Name"] + "\nCiudad: " + aer["City"] 
                    + "\nPaís: " + aer["Country"])
        
        elif int(tamano) < 10 and int(tamano) != 1:
            j=1
            mitad = int(tamano/2)
            print("Los primeros "+ str(mitad) +" aeropuertos afectados son: ")  
            while j <= mitad:
                aer = lt.getElement(lista, j)
                print("\nIATA: " + aer["IATA"] + "\nNombre: " + aer["Name"] + "\nCiudad: " + aer["City"] 
                    + "\nPaís: " + aer["Country"])
                ultimo = lt.lastElement(lista)
                lt.removeLast(lista)
                lt.addFirst(lst, ultimo)
                j+=1

            print("\n")
            print("Los ultimos "+ str(mitad) +" aeropuertos afectados son: ")
            for n in lt.iterator(lst):
                print("\nIATA: " + n["IATA"] + "\nNombre: " + n["Name"] + "\nCiudad: " + n["City"] 
                    + "\nPaís: " + n["Country"])

    else:
        print("Cerrando el programa . . . .")
        sys.exit(0)
sys.exit(0)