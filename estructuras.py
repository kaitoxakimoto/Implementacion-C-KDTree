from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class Node(namedtuple("Node", "location left_child right_child")):
    def __repr__(self):
        return pformat(tuple(self))

def kdtree(point_list, depth: int = 0):
    # Revisa si la lista ingresada esta vacia
    if not point_list:
        return None

    k = len(point_list[0])-2 # En nuestra implementacion, los ultimos 2 valores de cada tupla son reservados para el almacenamiento de informacion
    # la dimension a revisar depende de la profundidad actual del arbol
    axis = depth % k

    # ordenamos la lista a como debe ser ingresada finalmente, elegimos el valor del medio como pivote para partir el arbol
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2

    # Creacion del nodo y el subarbol final
    return Node(
        location=point_list[median],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1 :], depth + 1),
    )

# def nearest_k_neighbours(k,nodo):


        

# point_list = [(7, 2,"hola","papa"), (5, 4,"hola","nana"), (9, 6,"hola","abuela"), (4, 7,"chao","tia"), (8, 1,"hola","hijo"), (2, 3,"hola","hermana")]
# tree = kdtree(point_list)
# print(tree)
