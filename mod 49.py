import builtins
print("Teclea fecha ddmmaaaa :")
fe = input()
ano=int(fe)
print()
while ano <= 600000000 :
    ano = ano + 100000001
    print (ano % 49)
input("Para salir, pulsa 'Enter'")
