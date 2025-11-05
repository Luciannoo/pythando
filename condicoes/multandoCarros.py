# criando um radar que analiza se o carro está na velociade permitida
velociade = float(input("a velocidade atual do carro: "))
multa = (velociade - 80) * 7

if velociade > 80:
    print("você recebeu uma multa no valor de: R${}".format(multa))
else:
    print("não se esqueça de manter a velocidade a 80km ou menos!")