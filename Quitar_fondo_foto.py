##Quitar fondo foto_NO FUNCIONA

import rembg 
import numpy as np
from PIL import Image
input_image=Image.open('C:/Program Files/Python311/img1.jpeg')
input_array=np.array(input_image)
output_array=rembg.remove(input_array)
output_image=Image.fromarray(output_array)
output_image.save=('C:/Program Files/Python311/img10.jpeg')
