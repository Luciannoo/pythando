# lendo um número real e exibindo a parte inteira 
from math import trunc
numero = float(input("digite um número real: "))
print("a parte inteira de {} equivale a: {}".format(numero, trunc(numero)))