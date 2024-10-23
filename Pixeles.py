##Ver foto pixeles

from PIL import Image
import numpy as np
im = Image.open("Japon.jpeg")
pixels= list(im.getdata())

height = 500
weight = 500
channel = 3
img_numpy = np.zeros((height, weight, channel), dtype=np.uint8)
img = Image.fromarray(img_numpy, "RGB")
print(pixels)
image_filename="imagenPixeles.png"
img.save(image_filename)


img.show()
