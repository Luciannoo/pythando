# calculando o custo de uma viagem de acordo com a distância
distancia = float(input("qual a distância da viagem? "))

if distancia <= 200:
    valor = distancia * 0.50
    print("o valor a ser pago é de: R${}".format(valor))
    print("obrigado pela preferência, até a próxima!")
else:
    valor = distancia * 0.45
    print("o valor a ser pago é de: R${}".format(valor))
    print("obrigado pela preferência, até a próxima!")