##Igualar tamaño fotos

import cv2
from PIL import Image 

image1 = Image.open("C:/Program Files/Python311/imagen1_500.jpeg")
image2 = Image.open("C:/Program Files/Python311/imagen2_500.jpeg")

new_image1 = image1.resize((500, 500))
new_image2 = image2.resize((500, 500))

new_image1.save("Imagen1_500.jpeg")
new_image2.save("Imagen2_500.jpeg")

'''
cv2.imshow( new_image1,"Imagen1_500.jpeg")
cv2.imshow( new_image2,"Imagen2_500.jpeg" )

'''
