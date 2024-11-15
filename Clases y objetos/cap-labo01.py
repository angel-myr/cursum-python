""" Laboratorio - Ejercicio del Rectángulo """

class Rectangulo:
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura
        return area

testerRectangulo = Rectangulo()    
print("Ingresa el area: ")
testerRectangulo.base = float(input())
print("Ingresa la altura")
testerRectangulo.altura = float(input())

print("Área calculada: ", testerRectangulo.calcularArea())
