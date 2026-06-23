"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
# ''''''
# Crea un programa que calcule e imprima el area de un circulo, repetir el proceso tantas veces lo requieran.
# Al final imprimir el promedio de todas las areas calculadas, asi como la tupla con todas las areas en orden desendente 
# Considere:
# 1.-Area=pi*r^2
# Restricciones: 
# 1.- Con estructura de control 
# 2.- con una funcion que implemente parametros y regrese valor 
# 3.- implemetar una tupla 

import math
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area
areas = []
while True:
    try:
        radio = float(input("Ingrese el radio del círculo (o 'salir' para terminar): "))
        area = calcular_area_circulo(radio)
        areas.append(area)
        print(f"El área del círculo con radio {radio} es: {area:.2f}")
    except ValueError:
        break
if areas:
    promedio_area = sum(areas) / len(areas)
    print(f"El promedio de las áreas calculadas es: {promedio_area:.2f}")
    areas_ordenadas = tuple(sorted(areas, reverse=True))
    print(f"Las áreas en orden descendente son: {areas_ordenadas}")
else:    print("No se calcularon áreas.")