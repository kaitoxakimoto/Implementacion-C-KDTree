from lectura import *
from kdtree import *
from math import *
import pandas as pd
import numpy as np
import time


def distanciapunto(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i]-point2[i])**2
    return sqrt(sum)

def myFuncList(e):
    return e[1]
def verToNumber(ver):
    number = int(ver) / pow(10, len(ver)-1)
    return (number)

def k_nearest_list(lista, k, punto):
    cont = 0
    start_time = time.time()
    k_best = list()
    for i in range(len(lista)):
        cont+=1
        if len(k_best) < k:
            k_best.append(
                (lista[i], distanciapunto(lista[i][0], punto)))
            k_best.sort(key=myFuncList)
        elif distanciapunto(lista[i][0],punto) < distanciapunto(k_best[-1][0][0], punto):
            k_best.append(
                (lista[i], distanciapunto(lista[i][0], punto)))
            k_best.pop()
    return k_best , cont , (time.time() - start_time)

def search_from_id(lista,id):
    for i in lista:
        if(str(i[1][1]) == str(id)):
            return i


def search_from_name(lista,name):
    for i in lista:
        if(str(i[1][0]) == str(name)):
            return i


def imprimirDato(dato):
    if dato[0][12]:
        license = "YES"
    else: license = "NO"

    print("\nName: ", dato[1][0],
    " ID: ", dato[1][1],
    " Size: %.03f" % dato[0][0], " Mb",
    " Currency: USD",
    " Price: ", dato[0][1],
    " Rating count total: ", dato[0][2],
    " Rating count version: ", dato[0][3],
    " User rating: ", dato[0][4],
    " User rating ver: ", dato[0][5],
    " Ver: ", dato[0][6],
    " Content Rating: ", dato[0][7],
    " Genre: ", switch_genre(dato[0][8]),
    " Supported Devices (quantity): ", dato[0][9],
    " Screenshots: ", dato[0][10],
    " Supported Languages: ", dato[0][11],
    " License: ", license)

def switch_genre(movie):
    switcher = {
        1: "Book",
        2: "Business",
        3: "Catalogs",
        4: "Entertaiment",
        5: "Finance",
        6: "Food & Drink",
        7: "Games",
        8: "Health & Fitness",
        9: "Lifestyle",
        10: "Medical",
        11: "Music",
        12: "Navigation",
        13: "News",
        14: "Photo & Video",
        15: "Productivity",
        16: "Reference",
        18: "Shopping",
        18: "Social Networking",
        19: "Sports",
        20: "Travel",
        21: "Utilities",
        22: "Weather",
    }
    return (switcher.get(movie, 'AAAAA'))

def switch_genre_index(movie):
    switcher = {
        "Book": 1,
        "Business": 2,
        "Catalogs": 3,
        "Entertaiment": 4,
        "Finance": 5,
        "Food & Drink": 6,
        "Games": 7,
        "Health & Fitness": 8,
        "Lifestyle": 9,
        "Medical": 10,
        "Music": 11,
        "Navigation": 11,
        "News": 13,
        "Photo & Video": 14,
        "Productivity": 15,
        "Reference": 16,
        "Shopping": 17,
        "Social Networking": 18,
        "Sports": 19,
        "Travel": 20,
        "Utilities": 21,
        "Weather": 22,
    }
    return (switcher.get(movie, 0))