class Deportista:
    def __init__(self, nombre, edad, deporte, nivel):
        self.__nombre = nombre
        self.__edad = edad
        self.__deporte = deporte
        self.__nivel = nivel

    def __str__(self):
        return "Nombre Completo: " + self.__nombre + ", Edad: " + str(self.__edad) + ", Deporte: " + self.__deporte + ", Nivel de especialidad: " + self.__nivel
    