from persona import Persona
from entidad import Entidad

# Definición de clase hija con herencia múltiple
class Empleado(Persona, Entidad):
    def __init__(self, nombre, edad, altura, ancho, cargo, sueldo):
        # Constructor múltiple
        Persona.__init__(self, nombre, edad)
        Entidad.__init__(self, altura, ancho)
        self.__cargo = cargo
        self.__sueldo = sueldo

    def setCargo(self, new):
        self.__cargo = new

    def serSueldo(self, new):
        self.__sueldo = new

    def getCargo(self):
        return self.__cargo
    
    def getSueldo(self):
        return self.__sueldo
    
    def __str__(self):
        return "Nombre: " + self.getNombre() + ", Edad: " + str(self.getEdad()) + ", Altura: " + str(self.getAltura()) + ", Ancho: " + str(self.getAncho()) + ", Cargo: " + self.getCargo() + ", Sueldo: " + str(self.getSueldo())
    
developer = Empleado("Juan Máximo Reynoso", 58, 1.85, 0.45, "Director Deportivo", 4500)
print(developer)