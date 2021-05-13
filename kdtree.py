from lectura import *
from lista import *
import time
from math import *

def distanciapunto(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i]-point2[i])**2
    return sqrt(sum)


def myFunc(e):
    return e[1]


class Node:
    def __init__(self, left_node=None, right_node=None, parent=None, point=list(), data=list(), dim=0):
        self.left_node = left_node
        self.right_node = right_node
        self.parent = parent
        self.point = point  # lista con datos comparables
        self.data = data  # lista con id y nombre
        # Current dimension splitter ej; si son 3 dims, 0-1-2-0-1-2...
        self.dim = dim
    def __eq__(self, other):
        return self.data[0] == other.data[0]

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __repr__(self):
        return str((self.data,self.point))


class Kdtree:
    def __init__(self, dimensiones, treeRoot=None):
        self.NDims = dimensiones
        self.root = treeRoot

    # ejemplo de points de n=2 -> [((1,5,4),('hola','19'),((2,7,5),('chao','69'))] = posicion (1,5), dato=4, posicion (2,7), dato =5
    def construct(self, points=list()):  # points debe ser una lista de tuplas de n+1 dimensiones
        for punto in points:  # n= numero de dimensiones, el ultimo index contiene el dato

            position = self.root  # posicion inicial
            newNode = Node(None, None, None, punto[0], punto[1], 0)

            while position is not None:
                if (punto[0][position.dim] < position.point[position.dim]):
                    
                    if(position.left_node is not None):
                        newNode.dim = (newNode.dim+1) % (self.NDims-1)
                        position = position.left_node
                        
                    else:
                        if (newNode.dim < self.NDims):
                            newNode.dim += 1
                        else:
                            newNode.dim = 0
                        
                        newNode.parent = position                                                        
                        position.left_node = newNode
                        break
                        
                else:
                    if(position.right_node is not None):
                        newNode.dim = (newNode.dim+1) % (self.NDims-1)
                        position = position.right_node

                    else:
                        if (newNode.dim < self.NDims):
                            newNode.dim += 1
                        else:
                            newNode.dim = 0
                        newNode.parent = position
                        position.right_node = newNode
                        break
                        

            else:
                self.root = newNode
                position = self.root


    # knearest 
    def knearest(self, k, point):
        cont = 0
        start_time = time.time()
        knearest = list()  # lista ordenada
        s = list()  # pila
        nodos_explorados = list()
        explorador = self.root
        while explorador is not None:
            s.append(explorador)
            current_dimension = explorador.dim
            if point[current_dimension] < explorador.point[current_dimension]:
                explorador = explorador.left_node
            else:
                explorador = explorador.right_node

        while len(s) > 0:
            explorador = s.pop()
            cont += 1

            nodos_explorados.append(explorador)
            # Chequeamos si el dato cumple con las condiciones
            if len(knearest) < k:
                knearest.append(
                    (explorador, distanciapunto(explorador.point, point)))
                knearest.sort(key=myFunc)
            elif distanciapunto(explorador.point, point) < distanciapunto(knearest[-1][0].point, point):
                knearest.append(
                    (explorador, distanciapunto(explorador.point, point)))
                knearest.sort(key=myFunc)
                knearest.pop()

            # Chuqueamos si el 'otro' subarbol puede contener un candidato
            if(explorador.parent is not None): 
                explorador = explorador.parent

            if(explorador.left_node is not None):
                if (explorador.left_node not in nodos_explorados):
                    if (abs(explorador.point[explorador.dim] - point[explorador.dim]) < knearest[-1][1]):
                        explorador = explorador.left_node
                        while explorador is not None:
                            s.append(explorador)
                            current_dimension = explorador.dim
                            if point[current_dimension] < explorador.point[current_dimension]:
                                explorador = explorador.left_node
                            else:
                                explorador = explorador.right_node

            elif(explorador.right_node is not None):
                if(explorador.right_node not in nodos_explorados):
                    if (abs(explorador.point[explorador.dim] - point[explorador.dim]) < knearest[-1][1]):
                        explorador = explorador.right_node
                        while explorador is not None:
                            s.append(explorador)
                            current_dimension = explorador.dim
                            if point[current_dimension] < explorador.point[current_dimension]:
                                explorador = explorador.left_node
                            else:
                                explorador = explorador.right_node

        return knearest , cont , (time.time() - start_time)
