##Combinar dos imagenes

import cv2

# Leer la imagen de fondo y la imagen de primer plano
background = cv2.imread("C:/users/manel/img1.jpeg")
foreground = cv2.imread("C:/users/manel/img2.jpeg")


# Convertir la imagen de primer plano a escala de grises
gray_foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización a la imagen de primer plano
_, mask = cv2.threshold(gray_foreground, 10, 255, cv2.THRESH_BINARY)

# Invertir la máscara
mask_inv = cv2.bitwise_not(mask)

# Aplicar la máscara a la imagen de primer plano y la máscara invertida a la imagen de fondo
foreground_masked = cv2.bitwise_and(foreground, foreground, mask=mask)
background_masked = cv2.bitwise_and(background, background, mask=mask_inv)

# Combinar las dos imágenes para obtener la imagen de salida
output = cv2.add(foreground_masked, background_masked)

# Guardar la imagen de salida
cv2.imwrite('output.jpeg', output)
