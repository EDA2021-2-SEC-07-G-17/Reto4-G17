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
        "conexiones":None,
        "grafo_dirigido":None,
        "grafo_nodirigido":None
    }

    analyzer["aeropuertos"] = mp.newMap(numelements=41011, maptype="CHAINING")
    analyzer["conexiones"] = mp.newMap(numelements=92623, maptype="CHAINING")
    analyzer["grafo_dirigido"] = gr.newGraph(datastructure="ADJ_LIST",directed=True, size=92623)
    analyzer["grafo_nodirigido"] = gr.newGraph(datastructure="ADJ_LIST",directed=False, size=92623)

    return analyzer
    

# Funciones para agregar informacion al catalogo

def add_total(analyzer, airport, ruta):
    add_vertices(analyzer)
    add_arcos(analyzer)


def add_aeropuerto(analyzer, airport):
    nombre_iata = airport["IATA"]
    mp.put(analyzer["aeropuertos"], nombre_iata, airport)
    return analyzer

def add_conexiones(analyzer, ruta):
    conexiones = analyzer["conexiones"]
    origen = ruta["Departure"]
    destino = ruta["Destination"]

    if mp.contains(conexiones, origen):
        mapa = mp.get(conexiones, origen)["value"]
        mp.put(mapa, destino, ruta)
        mp.put(conexiones, origen, mapa)
    else:
        mapa = mp.newMap(numelements=1009, maptype="CHAINING")
        mp.put(mapa, destino, ruta)
        mp.put(conexiones, origen, mapa)
    return analyzer

def add_vertices(analyzer):
    aeropuertos = mp.keySet(analyzer["aeropuertos"])
    dirigido = analyzer["grafo_dirigido"]
    
    for ae in lt.iterator(aeropuertos):
        gr.insertVertex(dirigido, ae)
    
    return analyzer

def add_arcos(analyzer):
    conexiones = analyzer["conexiones"]
    dirigido = analyzer["grafo_dirigido"]
    nodirigido = analyzer["grafo_nodirigido"]
    origenes = mp.keySet(conexiones)

    for ori in lt.iterator(origenes):
        mapa = mp.get(conexiones, ori)["value"]
        bucket = mp.keySet(mapa)
        for des in lt.iterator(bucket):
            nmapa = mp.get(conexiones, des)["value"]
            ruta = mp.get(nmapa, des)["value"]
            if mp.contains(nmapa, ori):
                gr.insertVertex(nodirigido, ori)
                gr.insertVertex(nodirigido, des)
                gr.addEdge(nodirigido, ori, des, float(ruta["distance_km"]))
            
            gr.addEdge(dirigido, ori, des, float(ruta["distance_km"]))
    
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
