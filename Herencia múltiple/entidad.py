class Entidad:
    def __init__(self, altura, ancho):
        self.__altura = altura
        self.__ancho = ancho

    def setAltura(self, new):
        self.__altura = new

    def setAncho(self, new):
        self.__ancho = new

    def getAltura(self):
        return self.__altura
    
    def getAncho(self):
        return self.__ancho
    