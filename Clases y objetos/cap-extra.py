
class Usuario:
    def __init__(este, n, s, *v, **d):
        este.nombre = n
        este.sueldo = s
        este.valores = v
        este.diccionario = d

    def imprimirUser(this):
        print("Nombre: ", this.nombre)
        print("Sueldo: ", this.sueldo)
        print("Valores (Tupla): ", this.valores)
        print("Diccionario: ", this.diccionario)

user01 = Usuario("Angel", 1780)
user01.imprimirUser()
print()

user02 = Usuario("Ethan", 1200.40, 11,9,2004)
user02.imprimirUser()
print()

user03 = Usuario("Dzeko", 3000, 23,11,1998, p="The Godfather II", c="Arroz chaufa", h="Ajedrez")
user03.imprimirUser()
print()

