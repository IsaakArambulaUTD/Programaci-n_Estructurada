"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
print("\033c")

#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]

numeros=[23,45,8,24]

varios=["Hola",3.1416,33,True]

vacia=[]


#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacia)
print(paises[1])

#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)

# #2do forma 
for i in range(0,len(paises) ):
    print(paises[i])


#ordenar elementos de una lista
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
paises.sort()  # Ordena la lista en orden ascendente
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)

#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Colombia")
print(paises)
paises.insert(8,"Australia")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma


#2da forma 


#Buscar un elemento dentro de la lista


#Contar el numeros de veces que aparece un elemento dentro de una lista



#Conocer la posicion o indice en el que se encuentra un elemento de la lista



#Unir el contenido de una lista dentro de otra lista


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente




