##Primitiva amdor
from collections import Counter
import numpy as np
n=0

num=[]
apuesta=np.array([6, 19, 30, 32, 34, 42])


aciertos=np.array([
[15,	25, 	28,	33,	38,	47],
[1,	5,	14,	23,	30,	41],	
[5,	9,	10,	11,	16,	48],	
[2,	17,	18,     24,	25,	46],	
[1,	10,	13,	26,	33,	43],	
[10,	20,	21,	30,	38,	41],	
[9,	18,	20,	23,	38,	49],	
[1,	9,	15,	17,	39,	42],	
[1,	10,	14,	18,	38,	44],	
[15,	17,	32,	33,	44,	45],	
[7,	16,	20,	43,	48,	49],	
[12,	28,	37,	38,	40,	49],	
[1,	12,	20,	28,	29,	35],	
[1,	8,	9,	24,	29,	32],	
[3,	7,	10,	28,	39,	48],	
[3,	5,	18,	32,	34,	36],	
[5,	32,	35,	41,	42,	45],
[11,	13,	27,	33,	40,	48],	
[8,	16,	20,	39,	45,	46],	
[17,	19,	33,	34,	37,	43],	
[1,	16,	20,	21,	23,	26],	
[11,	16,	26,	30,	43,	44],	
[1,	7,	17,	33,	38,	40],	
[5,	11,	16,	35,	37,	43],	
[2,	14,	32,	33,	35,	46],	
[11,	15,	27,	30,	40,	47],	
[2,	6,	11,	19,	22,	33],	
[5,	13,	15,	23,	29,	35],	
[4,	10,	20,	24,	42,	48],
[16,	23,	26,	33,	40,	41],	
[1,	10,	17,	25,	26,	41],	
[3,	8,	12,	13,	29,	31],	
[4,	5,	8,	11,	20,	40],	
[16,	25,	26,	31,	45,	47],	
[10,	17,	20,	25,	28,	42],	
[12,	13,	15,	28,	40,	42],	
[11,	20,	33,	38,	44,	48], 
[2,	8,	11,	12,	16,	18],	
[2,	3,	12,	26,	31,	42],	
[11,	15,	17,	20,	37,	46],	
[13,	18,	38,	39,	42,	46],	
[7,	10,	21,	28,	30,	33], 
[3,	22,	42,	43,	46,	48],
[12,    17,     28,     32,     41,     45],
[19,    25,     30,     39,     42,     44],             
[19,    23,     28,     37,     41,     46],
[1,     15,     24,     27,     30,     40],
[8,     11,     13,     20,     27,     42],              
[3,     5,      25,     39,     43,     44],
[16,    24,     33,     36,     44,     46],
[5,     10,     12,     13,     32,     33],
[2,     7,      10,     20,     31,     40],
[9,     16,     17,     22,     39,     42],
[20,    21,     26,     37,     42,     49],
[5,     10,     16,     30,     33,     38],     
[1,     14,     23,     32,     39,     47],
[5,     6,      11,     12,     14,     41], 
[2,     3,      7,      21,     34,     39],
[4,     6,      14,     35,     40,     45],
[9,     17,     24,     30,     38,     45],
[5,     7,      11,     28,     36,     39],
[1,     3,      22,     24,     31,     44],
[4,     6,      19,     20,     40,     48],
[4,     5,      8,      10,     27,     36],
[1,     5,      8,      15,     28,     33],
[6,     20,     22,     35,     47,     48],
[6,     15,     17,     32,     33,     49],
[12,    13,     21,     32,     38,     46],
[5,     9,      20,     35,     43,     45],
[7,     18,     21,     40,     45,     49],
[2,     14,     28,     33,     36,     47],
[7,     13,     14,     27,     40,     49],
[4,     23,     26,     31,     35,     47],
[27,     31,     32,     38,    39,      45],
[3,     7,      15,      32,    43,      49],
[5,     12,     15,      36,    41,     43],
[5,     10,     23,     26,     33,       40],
[7,     8,      14,     18,     36,     43]]) 
        


for x in range(6):
        for y in range(53):                
                for z in range(6):
                        if apuesta[x]==aciertos[y][z]:
##                               print(y,end="," )
                                        rep=num.append(y)


print("repetidos número de veces = aciertos por apuesta")
orde=Counter(num)
print(orde)
                






                
