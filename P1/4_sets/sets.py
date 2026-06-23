"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

set1={"python","SQL","Estructurado"}
print(set1)
for i in set1:
    print(i)

set2={"Hola",True,33,3,1416}
print(set2)

set2.respaldo=set2.copy()
set2.clear()


set3={""}
print(set3)
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)



#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
lista_emails=[]
set_emails=set()

opc="5"
while opc=="5":
  lista_emails.append(input("Dame un email: ").lower().strip())
  set_emails.add(input("ingresa un email: ").lower().strip()) 
  opc=input("Deseas ingresar otro?: (S/N)").upper().strip()
print(lista_emails)
print(set_emails)
set_emails=set(lista_emails)
print(set_emails)
lista_emails=list(set_emails)
print(lista_emails)

#Solucion 2 que todos los correos de la lista los guarde al principio y usar otra variable que no sea while 
emails=[]

resp="SI"
while resp=="SI": 
   emails.append(input("Email: ").strip())
   resp=input("Deseas ingresar otro email? (SI/NO)").upper().strip()

emails_set=set(emails)
emails=list(emails_set)