""" Laboratorio - Ejercicio de la Caja """

class Caja:
    def __init__(self, largo = 0, ancho = 0, alto = 0):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def calcularVolumen(self):
        vol = self.largo * self.ancho * self. alto
        return vol
    
testerCaja = Caja()
print("Ingresa el largo: ")
testerCaja.largo = float(input())
print("Ingresa el ancho: ")
testerCaja.ancho = float(input())
print("Ingresa el alto: ")
testerCaja.alto = float(input())

print("Volumen calculado: ", testerCaja.calcularVolumen())