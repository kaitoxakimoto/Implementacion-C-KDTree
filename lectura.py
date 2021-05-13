from kdtree import *
from lista import *
import pandas as pd
import numpy as np

def verToNumber(ver):
    number = int(ver) / pow(10, len(ver)-1)
    return (number)


def lista_from_file(file):
    df = pd.read_csv(file)
    lista_grande = list()
    for i in df.index:
        aux = list()
        aux.append(df['size_bytes'][i]/(1024**2))
        aux.append(df['price'][i])
        aux.append(df['rating_count_tot'][i])
        aux.append(df['rating_count_ver'][i])
        aux.append(df['user_rating'][i])
        aux.append(df['user_rating_ver'][i])
        aux.append(verToNumber(df['ver'][i].replace(' Build ', ',').replace('.','').replace('iOV', '').replace('v','').replace('b', '').replace(',', '').replace('V', '').replace('Update ', '')))
        aux.append(int(df['cont_rating'][i].replace('+','')))
        aux.append(int(np.where(pd.get_dummies(df['prime_genre']).to_numpy()[i] == 1)[0]))
        aux.append(df['sup_devices.num'][i])
        aux.append(df['ipadSc_urls.num'][i])
        aux.append(df['lang.num'][i])
        aux.append(df['vpp_lic'][i])
        aux = tuple(aux)


        game = [(aux),(df['track_name'][i], df['id'][i])]
        lista_grande.append(game)

    return lista_grande

def kd_from_file(file):
    lista_grande = lista_from_file(file) 
    arbol = Kdtree(len(lista_grande[0][0]),None)
    arbol.construct(lista_grande)
    return arbol

def kd_from_list(lista_grande):
    arbol = Kdtree(len(lista_grande[0][0]),None)
    arbol.construct(lista_grande)
    return arbol