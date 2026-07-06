import funciones
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR CARACTERISTICAS A UNA PELICULA ::::...\n")
    caracteristica=input("Ingresa la caracteristica: ").lower().strip()
    valor=input("Ingresa la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis)>0:
        print("\tCaracteristica\t\tValor")
        for i in pelis:
            print(f"\t{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("... No existe ninguna caracteristica en la pelicula, Verifique ...")
   
def limpiarPeliculas(pelis):
     print("\t\t....:::: BORRRAS TODAS CARACTERISTICAS DE LA PELICULA ::::...\n") 
     if len(pelis)>0:
         opc=""
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las caracteristicas de la peliculas (Si/No)? ").lower().strip()
         if opc=="si":
             pelis.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen caracterisiticas que borrar, verifique! ....")
    
def buscarPeliculas(pelis):
    print("\t\t....:::: BUSCAR CARACTERISTICAS DE LA PELICULA ::::...\n")   
    caracteristica=input("Escribe el nombre de la caracteristica: ").upper().strip()
    NoEncontro=True
    print("\tcaracteristica\t\tValor")
    for i in pelis:
        if caracteristica==i:
            print(f"\t{i}\t\t{pelis[i]}")
            NoEncontro=False
    funciones.espereTecla()
    if NoEncontro:
        input("\n\t...¡No existe la caracteristica que estas buscando!...")

def borrarPeliculas(pelis):
    print("\t\t....:::: BORRAR LA CARACTERISTICA ::::...\n")   
    caracteristica=input("Escribe el nombre de la caracteristica: ").upper().strip()
    NoEncontro=True
    for i in pelis:
        for i in pelis:
            if caracteristica==i:
              opc=""
              while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la caracteristica de la pelicula (Si/No)? ").lower().strip()
              if opc=="si":
                pelis.pop(caracteristica)
                funciones.accionExitosa()
                NoEncontro=False
        if NoEncontro:
            print("\n\t...¡No existe la caracteristica que andas buscando!...")

def modificarPeliculas(pelis):
    print("\t\t....:::: MODIFICAR LA CARACTERISTICA DE UNA PELICULA ::::...\n")   
    caracteristica=input("Escribe la caracteristica de la pelicula: ").upper().strip()
    NoEncontro=True
    for i in pelis:
        if caracteristica==i:
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas mofificar la carcateristica: (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[i]=input("Escribe la nueva caracteristica: ").upper().strip()
                funciones.accionExitosa()
                NoEncontro=False
    if NoEncontro:
        input("\n\t...¡No existe la carcateristica de la pelicula que estas buscando!...")
 

