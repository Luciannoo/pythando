# um joginho de adivinha um número
from random import randint

print("fale um número de 0 a 5 que será dito pelo PC e tente acertar\n")
numDito = randint(0, 5)
numFalado = int(input("qual o número dito pelo computador: "))

if numDito == numFalado:
    print("parabéns, você acertou!")
else:
    print("infelizmente você errou!")
