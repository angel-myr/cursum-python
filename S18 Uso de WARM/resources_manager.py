# Uso de with simple
with open('data.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# Uso de with con una clase Manage
class ManejoArchivos:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def __enter__(self):
        print(' ¡Recurso obtenido! '.center(50, '-'))
        self.nombreArchivo = open(self.nombreArchivo, 'r', encoding='utf8')
        return self.nombreArchivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(' ¡Recurso cerrado! '.center(50, '-'))
        if self.nombreArchivo:
            self.nombreArchivo.close()

with ManejoArchivos('data.txt') as archivo:
    print(archivo.read())