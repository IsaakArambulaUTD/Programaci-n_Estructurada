# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")
      
def funcion1():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("Apellidos: ").strip().upper()
    print(f"El Nombre del Alumno es: {nombre} {apellidos}")
def funcion3(NOM, APE):
    nombre= NOM
    apellidos= APE
    print(f"El Nombre del Alumno es: {nombre} {apellidos}")
def funcion2():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("Apellidos: ").strip().upper()
    return nombre,apellidos
def funcion4():
    nombre=nom
    apellidos=ape
    return nombre,apellidos
