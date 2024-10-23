##Combinar imagenes

import cv2
from PIL import Image

# Abrir las dos imágenes
imagen_origen = Image.open("C:\Program Files\Python311img1_500.jpg")
imagen_fondo = Image.open("C:\Program Files\Python311/img2_500.jpg")

imagen_origen = imagen_origen.resize((500, 500))
imagen_fondo = imagen_fondo.resize((500, 500))

# Asegurarse de que las dos imágenes tengan el mismo tamaño
imagen_fondo = imagen_fondo.resize(imagen_origen.size)

# Crear una máscara para la imagen original (blanco para el objeto que se quiere mantener, negro para el fondo que se quiere reemplazar)
mascara = Image.new("L", imagen_origen.size, 0)
mascara_dibujable = ImageDraw.Draw(mascara)
mascara_dibujable.rectangle((100, 100, 300, 300), fill=255)

# Combinar las dos imágenes usando la máscara
imagen_nueva = Image.composite(imagen_origen, imagen_fondo, mascara)

# Guardar la imagen resultante
imagen_nueva.save("imagen_nueva.jpg")
