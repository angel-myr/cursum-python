class Periodista:
    def __init__(self, nombre, edad, seccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__seccion = seccion

    def __str__(self):
        return "Nombre Completo: " + self.__nombre + ", Edad: " + str(self.__edad) + ", Sección de estudio: " + self.__seccion
    