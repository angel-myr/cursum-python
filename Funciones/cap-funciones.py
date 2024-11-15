## Funciones
# Sin parámetros
# Con parámetros
# Con retorno
# Con valores por defecto
def derivada(a = 0, b = 0):
    print("Buscando la derivada de ", a)
    if (b == 1):
        print("La primera derivada es: ", a*2)

derivada(40, 1)
derivada(124, 2)
derivada(120, 1)
derivada()