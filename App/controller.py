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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catalogo
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.new_analyzer()
    return analyzer

# Funciones para la carga de datos
def loadINFO(analyzer, airpfile, routefile, citiesfile):
    loadairports(analyzer, airpfile)
    loadconections(analyzer, routefile)
    loadcities(analyzer, citiesfile)


def loadairports(analyzer, airpfile):
    "Carga la información de los aeropuertos"
    servicesfile = cf.data_dir + airpfile
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")
    for airport in input_file:
        model.add_aeropuerto(analyzer, airport)
    return analyzer


def loadconections(analyzer, routfile):
    "Carga la información de los vuelos"
    servicesfile = cf.data_dir + routfile
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")
    for vuelo in input_file:
        model.add_arcos(analyzer, vuelo)

    return analyzer

def loadcities(analyzer, citiesfile):
    "Carga la información de las ciudades"
    servicesfile = cf.data_dir + citiesfile
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")
    for city in input_file:
        model.add_ciudades(analyzer, city)
    return analyzer

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def mas_conexiones(analyzer):
    lista = model.mas_conexiones(analyzer)
    return lista

def clusteres_trafico(analyzer, iata1, iata2):
    total, conexion = model.clusteres_trafico(analyzer, iata1, iata2)
    return total, conexion

def efecto_aeropuerto(analyzer, iata):
    lista = model.efecto_aeropuerto(analyzer, iata)
    return lista

def encontrar_aeropuerto(analyzer, ciu):
    aeropuerto = model.encontrar_aeropuerto(analyzer,ciu)
    return aeropuerto

def escoger_ciudad(analyzer, name):
    ciudad = model.escoger_ciudad(analyzer, name)
    return ciudad

def camino_minimo(analyzer, iata1, iata2):
    distancia, pila = model.camino_minimo(analyzer, iata1, iata2)
    return distancia, pila
