# calculando o aumento de 15% para saláraios abaixo de R$1250 e de 10% para acima disso
salarioAtual = float(input("qual seu salário atual? R$"))

if salarioAtual <= 1250:
    aumento = salarioAtual + (salarioAtual * 0.15)
    print("parabéns, você passará a ganhar agora: R${}".format(aumento))
else:
    aumento = salarioAtual + (salarioAtual * 0.10)
    print("parabéns, você passará a ganhar agora: R${}".format(aumento))