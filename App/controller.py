"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config as cf
from App import model
import csv
import os
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""


def travel_lst(lista, parameter=None):
    return model.travel_lst(lista, parameter)


def travel_map(Map):
    return model.travel_map(Map)


def timer(func):
    from time import process_time

    def inner(*args, **kwargs):
        t1 = process_time()
        ret = func(*args, **kwargs)
        t2 = process_time()
        print(
            f"El tiempo que tardó la funcion {func.__name__} fue de {t2 - t1} segundos.\n")
        return ret
    return inner


@timer
def init():
    return model.init()


@timer
def load(filename, analyzer):
    with open(cf.data_dir + filename, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model.addtaxi(analyzer, row)
            model.addCommunityArea(analyzer, row)
        print("Se han cargado las estructuras de datos.\n"
              + "\t• Se utilizó una HashTable para los taxis.\n"
              + "\t• Se cargó el Grafo para los viajes entre Community Areas.")

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def reqA(analyzer):
    companies = model.reqApart1(analyzer)
    print(
        f"El número de taxis registrados son: {analyzer['taxis']['size']}")
    print(
        f"El número de compañías con al menos un taxi inscrito son: {len(companies)}\n")
    M = int(
        input("Digite el número de compañías del top por taxis afiliados (M):\n>>"))
    N = int(
        input("Digite el número de compañías del top por servicios prestados (N):\n>>"))

    topM, topN = model.reqApart2(companies, M, N)

    print(f"El top {M} de compañías por taxis afiliados son:")
    for num, i in enumerate(travel_lst(topM)):
        print(f"\t• {num+1}) {i} - {companies[i]['taxnum']}")

    print(f"\nEl top {N} de compañías por servicios prestados son:")
    for num, i in enumerate(travel_lst(topN)):
        print(f"\t• {num+1}) {i} - {companies[i]['servnum']}")
