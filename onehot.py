import pandas as pd
import numpy as np
from estructuras import kdtree

from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("Desafio3.csv")
  

x = pd.get_dummies(df.currency, prefix='plata')

# np.savetxt("aaaaaaaa.csv", x["genre_Book"] )


# x = x.to_numpy()
print(x.shape)

point_list = [(7, 2,"hola","papa"), (5, 4,"hola","nana"), (9, 6,"hola","abuela"), (4, 7,"chao","tia"), (8, 1,"hola","hijo"), (2, 3,"hola","hermana")]
tree = kdtree(point_list)
print(tree)


