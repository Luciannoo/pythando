# calculando a hipotenusa
import math
catetoOposto = float(input("comprimento do cateto oposto: "))
catetoAdjacente = float(input("comprimento do cateto adjacente: "))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print("a hipotenusa equivale a {:.2f}".format(hipotenusa))