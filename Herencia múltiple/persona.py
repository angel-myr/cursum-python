class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def setNombre(self, new):
        self.__nombre = new

    def setEdad(self, new):
        self.__edad = new

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
        