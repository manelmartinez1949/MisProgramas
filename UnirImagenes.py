## Unir dos imágenes
from PIL import Image
final= Image.new("RGB", (500, 500), "black")
imagen1=Image.open("C:/Program Files/Python311/imagen1_500.jpeg")
imagen2=Image.open("C:/Program Files/Python311/imagen2_500.jpeg")
final.paste(imagen1,(0,0))
final.paste(imagen2,(0, 0))
final.show()
final.save("imagenes_unidas.png")


           
