# calculando o IMC
peso = float(input("seu peso: "))
altura = float(input("sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("você está abaixo do peso!")
elif imc <=18.5 and imc <= 25:
    print("você está no peso ideal")
elif imc <= 20 and imc <= 30:
    print("você está com sobrepeso")
elif imc <= 30 and imc <= 40:
    print("você está com obesidade")
else:
    print("você está com obesidade mórbita")