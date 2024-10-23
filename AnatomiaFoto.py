##Anatomia de una foto   ver pixeles y abrir la foto
##funciona bien

from PIL import Image

# Abrir la imagen
imagen = Image.open("pelo.jpg")

# Obtener la matriz de píxeles
matriz_pixeles = imagen.load()

# Obtener las dimensiones de la imagen
ancho, alto = imagen.size
print(imagen.size)
# Recorrer la matriz de píxeles e imprimir los valores RGB
for y in range(alto):
    for x in range(ancho):
        r, g, b = matriz_pixeles[x, y]
        print(f"Píxel ({x}, {y}): R={r}, G={g}, B={b}")

# Mostrar la imagen
imagen.show()
