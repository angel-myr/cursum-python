# Importación en la misma carpeta
import mod_aritmetica as arit
# Importación en subcarpetas
from mods import mod_geometria as geom
# import mods.mod_geometria as geom

resultado = arit.suma(1200.54, 6000.12, 32.45)
print(resultado)

resultado = geom.areaTriangulo(15.6, 30)
print(resultado)
