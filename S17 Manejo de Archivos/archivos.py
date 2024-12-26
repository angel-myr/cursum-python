## Escribir en el archivo
def escribirEnArchivo():
    try:
        # Si no existe, lo crea
        archivo = open('data.txt', 'w', encoding='utf8')
        archivo.write('lorem ipsum 01' + '\n')
        archivo.write('lorem ipsum 02' + '\n')
        archivo.write('lorem ipsum 03' + '\n')
    except Exception as e:
        print(e)
    finally:
        archivo.close()

## Leer el archivo
def leerEnArchivo():
    try:
        archivo = open('data.txt', 'r', encoding='utf8')
        #todoElTexto = archivo.read()
        primerosNCaracteres = archivo.read(5)
        #lineaCompleta = archivo.readline()
        print(primerosNCaracteres)
    except Exception as e:
        print(e)
    finally:
        archivo.close()

## Iterar el archivo
def iterarArchivo():
    archivo = open('data.txt', 'r', encoding='utf8')
    for linea in archivo:
        print(linea)
    archivo.close()

def accederLineas():
    archivo = open('data.txt', 'r', encoding='utf8')
    # A líneas
    print(archivo.readlines())
    # A una línea N
    #print(archivo.readlines()[1])
    archivo.close()

def anexarInformacion():
    archivo = open('data.txt', 'a', encoding='utf8')
    archivo.write('\n')
    archivo.write('lorem ipsum 04' + '\n')
    archivo.write('lorem ipsum 05' + '\n')
    archivo.write('lorem ipsum 06' + '\n')
    archivo.write('by Magno')
    archivo.close()
