##Cambiar fondo.py

import cv2
# Leer la imagen de fondo y la imagen de primer plano
img1 = cv2.imread("C:/Users/manel/AppData/Local/Programs/Python/Python312/img1.jpeg") 
img2 = cv2.imread("C:/Users/manel/AppData/Local/Programs/Python/Python312/Oso2.jpg")

height1, width1, img1
height2, width2, Oso2
if height1 != height2 or width1 !=width2:
    if height1 > height2 or width1 > width2:
        lmg1= cv2.resize(img1,(width2, height2))
    else:
        img2= cv2.resize(img2, (width1, height1))
        
cv2.imwrite("C:/Users/manel/AppData/Local/Programs/Python/Python312/¡img1.jpeg", img1)
cv2.imwrite("C:/Users/manel/AppData/Local/Programs/Python/Python312/img2.jpeg", img2)
background= img2
foreground= img1

# Convertir la imagen de primer plano a escala de grises
gray_foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
# Aplicar umbralización a la imagen de primer plano
_, mask = cv2.threshold(gray_foreground, 100, 255, cv2.THRESH_BINARY)
# Invertir la máscara
mask_inv = cv2.bitwise_not(mask)
# Aplicar la máscara a la imagen de primer plano y la máscara invertida a la imagen de fondo
foreground_masked = cv2.bitwise_and(foreground, foreground, mask=mask)
background_masked = cv2.bitwise_and(background, background, mask=mask_inv)
# Combinar las dos imágenes para obtener la imagen de salida
output = cv2.add(foreground_masked, background_masked)
# Guardar la imagen de salida
cv2.imwrite('output.jpg', output)
