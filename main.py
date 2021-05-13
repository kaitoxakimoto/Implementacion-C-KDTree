from lectura import *
from kdtree import *
from lista import *
import time


big_list = lista_from_file("Desafio3.csv")
kd_tree = kd_from_list(big_list)



while True:
    print("Bienvenido al asistente del Desafio 3")
    print("Ingrese la opcion que desea usar:")
    print("1.- Mostrar información de una aplicación específica")
    print("2.- Mostrar información de las 10 aplicaciones más parecidas a una aplicación dada")
    print("3.- Mostrar información de las 10 aplicaciones más parecidas a vector de atributos")
    print("0.- Salir de la aplicación")
    
    #funcion validadora
    def tryInput(string):
        flag = int(input(string))
        while (flag > 4 or flag < 0):
            print("Input invalido, intente denuevo: ")
            flag = input(string)
        return flag

    choice = tryInput("")


    if choice == 1:
        #funcion que busque segun ID
        lookup = input("Ingrese un ID o nombre a buscar: ")

        if(lookup.isnumeric()):
            
            elemento = search_from_id(big_list,lookup)
        else:
            elemento = search_from_name(big_list,lookup)

        if(elemento is not None):
            imprimirDato(elemento)
        else:
            print("El elemento no existe")

        input("Presione Enter para continuar...")



        
    elif choice ==2:
        #mostrar 10 mas comunes segun id

        lookup = input("Ingrese el ID del elemento: ")
        elemento = search_from_id(big_list,lookup)
        point = elemento[0]
        mejores, it,tiemp = kd_tree.knearest(10, point)
        for i in range(len(mejores)):
            print ("Con una distancia de ", mejores[i][1], " el ", i+1, "elemento mas cercano es",mejores[i][0].data[0], " id:" ,mejores[i][0].data[1])

        print ("\ncon un tiempo de ", tiemp, " y ",it, " iteraciones cuando es buscado por KDTree.")
        kdtime = tiemp

        mejores, it, tiemp = k_nearest_list(big_list,10,point)
        print ("con un tiempo de ", tiemp, " y ",it, " iteraciones cuando es buscado por lista.")
        print("KDTree search es más rapido que busqueda por lista en un ", (tiemp*100/kdtime), "%")


        input("Presione Enter para continuar...")


    elif choice ==3:
        point = list()
        lookup = float(input("Ingrese el size_bytes: "))/(1024**2)
        point.append(lookup)
        lookup = float(input("Ingrese el precio: "))
        point.append(lookup)
        lookup = float(input("Ingrese el rating_count_tot: "))
        point.append(lookup)
        lookup = float(input("Ingrese el rating_count_ver: "))
        point.append(lookup)
        lookup = float(input("Ingrese el user_rating: "))
        point.append(lookup)
        lookup = float(input("Ingrese el user_rating_ver: "))
        point.append(lookup)
        lookup = input("Ingrese el ver: ")
        lookup = verToNumber(lookup.replace(' Build ', ',').replace('.','').replace('iOV', '').replace('v','').replace('b', '').replace(',', '').replace('V', '').replace('Update ', ''))
        point.append(lookup)
        lookup = float(input("Ingrese el cont_rating: ").replace('+',''))
        point.append(lookup)
        lookup = switch_genre_index(input("Ingrese el prime_genre: "))
        point.append(lookup)
        lookup = float(input("Ingrese el sup_devices.num: "))
        point.append(lookup)
        lookup = float(input("Ingrese el ipadSc_urls.num: "))
        point.append(lookup)
        lookup = float(input("Ingrese el lang.num: "))
        point.append(lookup)
        lookup = float(input("Ingrese el vpp_lic: "))
        point.append(lookup)

        mejores, it, tiemp = kd_tree.knearest(10, point)
        for i in range(len(mejores)):
            print ("Con una distancia de ", mejores[i][1], " el ", i+1, "elemento mas cercano es",mejores[i][0].data[0], " id:" ,mejores[i][0].data[1])
        print ("\ncon un tiempo de ", tiemp, " y ",it, " iteraciones cuando es buscado por KDTree.")
        kdtime = tiemp

        mejores, it, tiemp = k_nearest_list(big_list,10,point)
        print ("con un tiempo de ", tiemp, " y ",it, " iteraciones cuando es buscado por lista.")

        input("Presione Enter para continuar...")

    elif choice == 0:
        exit()

