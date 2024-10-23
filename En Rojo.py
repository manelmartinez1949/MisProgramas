import cv2 as cv
import numpy as np
import copy
# Carga la imagen en una variable
img = cv.imread('C:/Users/manel/Pictures/Bis.jpg')


img_red = np.copy(img)
# Crea una copia de la imagen original
##img = np.zeros ((300, 300,3), np.uint8)

img_red = np.zeros ((300, 300,3), np.uint8)

# Cambia los valores de los canales BGR de la imagen a rojo (B=0, G=0, R=255)
img_red[:, 0:, ] = 0
img_red[1:, :, 0] = 0
img_red[:, :, 0] = 220
# Con el 2 : Rojo, con el 1, verde

# Muestra la imagen original y la otra imagen en ventanas separadas
cv.imshow('Original', img)
cv.imshow('Azul', img_red)
cv.waitKey(0)
