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
import folium
from DISClib.ADT import graph as gr
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
import webbrowser
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def promedio_lat(lista):
    suma = 0
    numero = 0
    for e in lista:
        suma += float(e[0])
        numero += 1
    promedio = suma/numero
    return promedio

def promedio_lng(lista):
    suma = 0
    numero = 0
    for e in lista:
        suma += float(e[1])
        numero += 1
    promedio = suma/numero
    return promedio

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los puntos de Interconexión entre los Aeropuertos->Req 1")
    print("3- Consultar la cantidad de clústeres entre dos aeropuertos->Req 2")
    print("4- Consultar la ruta más corta entre dos ciudades->Req 3")
    print("5- Consultar la mayor cantidad de ciudades que pueden visitarse con Millas de Viajero->Req 4")
    print("6- Consultar el impacto causado por un aeropuerto cerrado->Req 5")

catalog = None
airpfile = "airports-utf8-small.csv"
routefile = "routes-utf8-small.csv"
citiesfile = "worldcities-utf8.csv"

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
        coordenadas = []
        while j <= 5:
            iata = lt.getElement(lista, i)
            lat = iata["Latitude"]
            lng = iata["Longitude"]
            coor = (lat, lng)
            coordenadas.append(coor)
            print("-------------------------------------------------------")
            print("\nIATA: " + iata["IATA"] + "\nName: " + iata["Name"] + "\nciudad: " + iata["City"] + "\nPais: " + iata["Country"] 
            + "\nConexiones: " + str(iata["total"]) + "\nEntrada: " + str(iata["entrada"]) + "\nSalida: " + str(iata["salida"]))
            print("")

            i -= 1
            j += 1

        p_lat = promedio_lat(coordenadas)
        p_lng = promedio_lng(coordenadas)
        
        mapa = folium.Map(location=[p_lat,p_lng], zoom_start=6)

        for e in coordenadas:
            folium.Marker(location= [ float(e[0]) , float(e[1]) ] ,icon=folium.Icon(color='red',icon='info-sign')).add_to(mapa) 
        mapa.save("mapa1.html")
        webbrowser.open("mapa1.html")

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
        print("\n----------------------Inputs----------------------")
        ciudad1 = input("\nEscriba el nombre de la ciudad de salida: ")
        ciu1 = controller.escoger_ciudad(catalog, ciudad1)
        aeropuerto1 = controller.encontrar_aeropuerto(catalog, ciu1)

        ciudad2 = input("\nEscriba el nombre de la ciudad de llegada: ")
        ciu2 = controller.escoger_ciudad(catalog, ciudad2)
        aeropuerto2 = controller.encontrar_aeropuerto(catalog, ciu2)
        print("\n----------------------Outputs----------------------")
        print("\nEl aeropuerto de salida es: ")
        print("\nIATA: " + aeropuerto1["IATA"] + "\nNombre: " + aeropuerto1["Name"] + "\nCiudad: " + aeropuerto1["City"] 
                    + "\nPaís: " + aeropuerto1["Country"])
        print("\nEl aeropuerto de llegada es: ")
        print("\nIATA: " + aeropuerto2["IATA"] + "\nNombre: " + aeropuerto2["Name"] + "\nCiudad: " + aeropuerto2["City"] 
                    + "\nPaís: " + aeropuerto2["Country"])
        print("")

        iata1 = aeropuerto1["IATA"]
        iata2 = aeropuerto2["IATA"]

        distancia, pila = controller.camino_minimo(catalog, iata1, iata2)

        print("La distancia total es: " + str(round(distancia,2)) + " (km)")
        
        for ruta in lt.iterator(pila):
            print("Salida: " + str(ruta["vertexA"]) + " - Llegada: " + str(ruta["vertexB"]) + " - Distancia: " + str(ruta["weight"]))
        

        punto1 = (aeropuerto1["Latitude"], aeropuerto1["Longitude"])
        punto2 = (aeropuerto2["Latitude"], aeropuerto2["Longitude"])

        coordenadas = [punto1, punto2]

        p_lat = promedio_lat(coordenadas)
        p_lng = promedio_lng(coordenadas)
        
        mapa = folium.Map(location=[p_lat,p_lng], zoom_start=6)

        for e in coordenadas:
            folium.Marker(location= [ float(e[0]) , float(e[1]) ] ,icon=folium.Icon(color='red',icon='info-sign')).add_to(mapa) 
        mapa.save("mapa3.html")
        webbrowser.open("mapa3.html")

    elif int(inputs[0]) == 5:
       y=input("ingrese su cantidad de millas")
       controller.millas(y,catalog)

    elif int(inputs[0]) == 6:
        print("\n----------------------Inputs----------------------")
        iata = input("\nEscribe el codigo IATA del aeropuerto fuera de funcionamiento: ")
        print("\n----------------------Outputs----------------------")
        lista = controller.efecto_aeropuerto(catalog, iata)
        tamano = lt.size(lista)
        print("\n Hay "+str(tamano)+" aeropuertos afectados por el cierre del aeropuerto " + str(iata))
        lst = lt.newList("ARRAY_LIST")
        
        coordenadas = []

        for ele in lt.iterator(lista):
            lat = ele["Latitude"]
            lng = ele["Longitude"]
            tupla = (lat, lng)
            coordenadas.append(tupla)
        
        p_lat = promedio_lat(coordenadas)
        p_lng = promedio_lng(coordenadas)
        
        mapa = folium.Map(location=[p_lat,p_lng], zoom_start=6)

        for e in coordenadas:
            folium.Marker(location= [ float(e[0]) , float(e[1]) ] ,icon=folium.Icon(color='red',icon='info-sign')).add_to(mapa) 
        mapa.save("mapa5.html")
        webbrowser.open("mapa5.html")
        
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