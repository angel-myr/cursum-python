
class Casa:
    def __init__(self, ubicacion, *v):
        # Atributo protegido
        self._ubicacion = ubicacion
        # Atributo privado
        self.__medidas = v

    def imprimirCasa(self):
        print("Ubicada en: ", self._ubicacion)
        print("De medidas: ", self.__medidas)
        print("De precio: ", self.__calcularPrecio())

    # Metodo privado
    def __calcularPrecio(self):
        precio = (self.__medidas[0] * self.__medidas[1] * 956.91) * self.__medidas[2]
        return precio

    # Getters and Setters
    def get_ubicacion(self):
        return self._ubicacion
    
    def set_ubicacion(self, new):
        self._ubicacion = new
    
    def get_medidas(self):
        return self.__medidas
    
    def set_medidas(self, *new):
        self.__medidas = new

basic_house = Casa("Av. La Marina 705")
basic_house.set_medidas(120,60,30)
print(basic_house.get_ubicacion())
print(basic_house.get_medidas())

peruvian_house = Casa("Av. Proceres 1290")
peruvian_house.set_medidas(200,120,65)
print(peruvian_house.get_ubicacion())
print(peruvian_house.get_medidas())

print("---")
basic_house.imprimirCasa()
peruvian_house.imprimirCasa()
