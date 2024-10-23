## ORDENAR LISTAS
from operator import *
import numpy as np

lista1=[1,36,4,5,78,9,52,14,7]
lista1.sort()
print(lista1, end="--\n")
print()

arr=np.array ([[8,2,3,4,7,8,5,84],
        [28,1,8,93,7,1,7,5],
        [1,5,8,4,3,2,6,8]])
print(arr)
lis=arr.tolist()
lista1=sorted(lis,key=itemgetter(0))
print('Ordenados por el primer número ')
print(lista1)


