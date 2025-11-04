# sorteando um aluno

from random import choice

aluno1 = str(input("nome do aluno: "))
aluno2 = str(input("nome do aluno: "))
aluno3 = str(input("nome do aluno: "))
aluno4 = str(input("nome do aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = choice(lista)

print("o aluno sorteado foi: {}".format(sorteado))
