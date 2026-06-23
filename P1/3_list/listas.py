print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[10,34,25,45]

print(numeros)

lista="["
for i in numeros:
    lista+=f"{i}, "
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]}, "
print(f"{lista}]")

i=0
lista="["
while i<len(numeros):
    lista+=f"{numeros[i]}, "
    i+=1
print(f"{lista}]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabra=input("Ingrese la palabra a buscar: ").strip()

#1ER FORMA
if palabra in palabras:
    print("Encontre la palabra en la lista")
else:
    print("No encontre la palabra en la lista")

#2DA FORMA
encontro=False
for i in palabras:
    if i==palabra:
    encontro=True
if encontro:
    print("Encontre la palabra en la lista")
else:
    print("No encontre la palabra en la lista")


#3er FORMA
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra:
        encontro=True
if encontro:
    print("Encontre la palabra en la lista")
else:
    print("No encontre la palabra en la lista")

#Ejemplo 3 Añadir elementos a la lista

  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

