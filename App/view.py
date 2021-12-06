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

        print("Cantidad de Aeropuertos Dirigidos: " + str(gr.numVertices(catalog['grafo_dirigido'])))
        print("Cantidad de Vuelos Dirigidos: " + str(gr.numEdges(catalog['grafo_dirigido'])))
        print("---------------------------------------------------------------------------")
        print("Cantidad de Aeropuertos No Dirigidos: " + str(gr.numVertices(catalog['grafo_nodirigido'])))
        print("Cantidad de Vuelos No Dirigidos: " + str(gr.numEdges(catalog['grafo_nodirigido'])))
        print("---------------------------------------------------------------------------")
        print("EL numero de ciudades no repetidas es: "+str(mp.size(catalog["ciudades"])))

    elif int(inputs[0]) == 2:
        print("Requerimiento 1")

    elif int(inputs[0]) == 3:
        print("Requerimiento 2")

    elif int(inputs[0]) == 4:
        print("Requerimiento 3")

    elif int(inputs[0]) == 5:
        print("Requerimiento 4")

    elif int(inputs[0]) == 6:
        print("Requerimiento 5")

    else:
        print("Cerrando el programa . . . .")
        sys.exit(0)
sys.exit(0)