##Esteganografia
from stegano import lsb
secret=lsb.hide("icono.png", " Esto está oculto")
secret.save("secret_img.png")

print(lsb.reveal("secret_img.png"))
