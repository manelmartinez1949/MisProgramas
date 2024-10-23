from PIL import Image
import numpy as np

color_nuevo=(0,172,193)
color_actual = (33, 150, 243)
img=Image.open("icono.png")
icono = icon.convert("RGBA")
data= np.array(icono)
data[(data ==color_actual.all(axis =-1))] = color_nuevo

icono_nuevo=Image.fromarray(data, "RGBA")
icono_nuevo.save("nuevo_icono.png")
