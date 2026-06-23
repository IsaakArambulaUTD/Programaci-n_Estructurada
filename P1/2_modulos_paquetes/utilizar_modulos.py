# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
# modulos.funcion()
n="Isaak"
a="Arambula"

nombre,apellidos=modulos.funcion4(n,a)
print(f"El Nombre completo es: {nombre} {apellidos}")


#2da formar de utilizar modulos
from modulos import borrarPantalla, funcion3

borrarPantalla()
n="Isaak"
a="Arambula"
funcion3(n,a)

