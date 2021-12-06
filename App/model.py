"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def new_analyzer():
    analyzer = {
        "aeropuertos":None,
        "grafo_dirigido":None,
        "rutas_dirigido":None,
        "grafo_nodirigido":None,
        "rutas_nodirigido":None,
        "ciudades":None
    }

    analyzer["aeropuertos"] = mp.newMap(numelements=41011, maptype="CHAINING")
    analyzer["grafo_dirigido"] = gr.newGraph(datastructure="ADJ_LIST",directed=True, size=92623)
    analyzer["rutas_dirigido"] = mp.newMap(numelements=41011, maptype="CHAINING")
    analyzer["grafo_nodirigido"] = gr.newGraph(datastructure="ADJ_LIST",directed=False, size=92623)
    analyzer["rutas_nodirigido"] = mp.newMap(numelements=41011, maptype="CHAINING")
    analyzer["ciudades"] = mp.newMap(numelements=41011, maptype="CHAINING")

    return analyzer
    

# Funciones para agregar informacion al catalogo


def add_aeropuerto(analyzer, airport):
    nombre_iata = airport["IATA"]
    aeropuertos = analyzer["aeropuertos"]
    dirigido = analyzer["grafo_dirigido"]
    nodirigido = analyzer["grafo_nodirigido"]
    gr.insertVertex(dirigido, nombre_iata)
    gr.insertVertex(nodirigido, nombre_iata)
    mp.put(aeropuertos, nombre_iata, airport)
    return analyzer

def add_arcos(analyzer, ruta):

    dirigido = analyzer["grafo_dirigido"]
    nodirigido = analyzer["grafo_nodirigido"]

    rutas_dirigido = analyzer["rutas_dirigido"]
    rutas_nodirigido = analyzer["rutas_nodirigido"]

    origen = ruta["Departure"]
    destino = ruta["Destination"]
    peso = ruta["distance_km"]
    aerolinea = ruta["Airline"]

    nruta = str(aerolinea)+"-"+str(origen)+"-"+str(destino)

    reverso = gr.getEdge(dirigido, destino, origen)

    if reverso != None:
        gr.addEdge(dirigido, origen, destino, peso)
        gr.insertVertex(nodirigido, origen)
        gr.insertVertex(nodirigido, destino)
        gr.addEdge(nodirigido, origen, destino, peso)

        mp.put(rutas_nodirigido, nruta, ruta)
        mp.put(rutas_dirigido, nruta, ruta)
    else:
        gr.addEdge(dirigido, origen, destino, peso)
        mp.put(rutas_dirigido, nruta, ruta)
    
    return analyzer

def add_ciudades(analyzer, ciu):
    ciudades = analyzer["ciudades"]
    name = ciu["city_ascii"]

    existencia = mp.contains(ciudades, name)

    if existencia == True:
        lista = mp.get(ciudades, name)["value"]
        lt.addLast(lista, ciu)
        mp.put(ciudades, name, lista)
    else:
        lista = lt.newList(datastructure="SINGLE_LINKED")
        lt.addLast(lista, ciu)
        mp.put(ciudades, name, lista)
    
    return analyzer


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareIATAS(aero, keyvalueaero):
    aerocode = keyvalueaero['key']
    if (aero == aerocode):
        return 0
    elif (aero > aerocode):
        return 1
    else:
        return -1

# Funciones de ordenamiento
