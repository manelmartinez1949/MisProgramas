

##indice=cintura/(altura x Raiz cuadrada de altura) - 18
import math 
p=float(input(" Teclee su peso "))
a=float(input(" Teclee su altura en metros "))
c=float(input(" Teclee perímetro de cintura en centímetros "))
m=float(input(" Teclee perímetro muñeca "))
edad=float(input("Teclee su edad "))
indice=p/(a*a)
print()
print("Indice por altura ", indice)
print("Indice por cintura ", c/a)
##Peso ideal = Altura en cm - 100 + ((edad/10) x 0,9)
Peso_ideal=((a*100 -100) + (edad/10 * 0.09))
print("Peso ideal ", Peso_ideal)
print("Indice por la muñeca ", (a*100) -100 + (4 * m //2))
print(" Indice Van der Vael ", ((a*100) -150 * .75) + 50 )
##circunferencia cadera / (Altura x √Altura) – 18= índice de grasa corporal.
print("Indice de grasa ", c/(a*math.sqrt(a))-18)

input("Pulse enter para salir ")

"""
Fórmula de Monnerot-Dumaine: Esta fórmula considera el tamaño de los huesos y la circunferencia de la muñeca.
La fórmula es:

Peso ideal = Estatura en cm - 100 + (4 x Circunferencia de la muñeca en cm / 2)

Fórmula de Wan der Vael: Basada en la altura y el peso, la fórmula para hombres es:

Peso ideal = Altura en cm - 150 x 0,75 + 50.

Para mujeres, la fórmula es:

Peso ideal = Altura en cm - 150 x 0,6 + 50.
Fórmula de Perrault Dry: Aunque no es ampliamente conocida, es bastante confiable ya que considera factores como la edad. La fórmula es la siguiente:

Peso ideal = Altura en cm - 100 + ((edad/10) x 0,9)

Por ejemplo, para una mujer de 1,75 metros y 28 años, el peso ideal estaría entre 77 y 78 kilos.

Fórmula de Broca: Es un método simple, pero puede no ser preciso para personas muy altas. Se calcula restando 100 a la altura en centímetros. Por lo tanto, si alguien mide 177 cm, el peso ideal sería alrededor de 77 kilos.

Fórmula de Monnerot-Dumaine: Esta fórmula considera el tamaño de los huesos y la circunferencia de la muñeca. La fórmula es:


"""
