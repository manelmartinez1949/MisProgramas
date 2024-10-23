##Contar cabezas

import cv2

# Cargar la imagen
img = cv2.imread("C:/Users/manel/AppData/Local/Programs/Python/Puntos 1.jpeg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro Gaussiano para suavizar la imagen
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Aplicar la detección de bordes mediante el operador de Canny
edges = cv2.Canny(blur, 50, 150)

# Buscar los contornos en la imagen
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Contar el número de contornos (cabezas) encontrados
num_heads = len(contours)

# Mostrar el resultado
print("Número de cabezas encontradas:", num_heads)

# Mostrar la imagen con los contornos dibujados
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow('Cabezas contadas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
