# replicando o jogo de jokenpô 

from random import choice
jogador = str(input("minha vez: "))

probabilidades = ['pedra', 'papel', 'tesoura']
computador = choice(probabilidades)

if jogador == "papel" and computador == "tesoura":
    print("computador: {}".format(computador))
    print("perdi")
elif jogador == "pedra" and computador == "papel":
    print("computador: {}".format(computador))
    print("perdi")
elif jogador == "tesoura" and computador == "pedra":
    print("computador: {}".format(computador))
    print("perdi")
elif jogador == "tesoura" and computador == "papel":
    print("computador: {}".format(computador))
    print("ganhei")
elif jogador == "papel" and computador == "pedra":
    print("computador: {}".format(computador))
    print("ganhei")
elif jogador == "pedra" and computador == "tesoura":
    print("computador: {}".format(computador))
    print("ganhei")
elif jogador == computador:
    print("computador: {}".format(computador))
    print("empate")

