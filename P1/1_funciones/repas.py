print("\033c")

def area(base, altura):
    resultado = base * altura
    return resultado


b=int(input("Base: "))
a=int(input("Altura: "))
resultado=area(b, a)
print(f"El area del rectangulo es: {resultado}")
