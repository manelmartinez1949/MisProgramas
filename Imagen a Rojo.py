import cv2
import numpy as np
import copy
image= cv2.imread('Foto de video.jpg')
cv2.imwrite('Copy of Foto.png', image)
img_red = cv2.cvtColor(image,cv2.COLOR_HSV2BGR)

cv2.imshow('modificado', img_red)
cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
