from lectura import *
from kdtree import *
from lista import *
import pandas as pd
import numpy as np
import time

arbol = kd_from_file("Desafio3.csv")
mejoreskd, iteracionkd,timekd = arbol.knearest(5,(60.3515625, 12.99, 1390, 143, 4.5, 5.0, 7.01, 4, 11, 37, 5, 33, 1))

lista = lista_from_file("Desafio3.csv")
mejoreslista,iteracioneslista,timelista = k_nearest_list(lista,5,(60.3515625, 12.99, 1390, 143, 4.5, 5.0, 7.01, 4, 11, 37, 5, 33, 1))

print("lo mejor en kd:")
print("iteraciones ", iteracionkd," tiempo ",timekd)
for elemento in mejores:
    print ("elemento: ",elemento[0], "distancia: ",elemento[1])

print("lo mejor en lista:")
print("iteraciones ", iteracioneslista," tiempo ",tiempoLista)
for elemento in mejores:
    print ("elemento: ",elemento[0], "distancia: ",elemento[1])

