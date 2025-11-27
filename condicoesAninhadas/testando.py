# APENAS UM TESTE SEM MUITA LÓGICA, SÓ QUERIA TREINAR ELIF E LISTA!!

print("diga o nome de um e verá de qual anime é \n")

jujtuso = ['Gojo', 'Itadori']
dragonBall = ['Vegeta', 'Goku']
naruto = ['Sakura', 'Hiddan']

nomePersonagem = str(input("nome de um personagem: "))

if nomePersonagem == "Gojo":
    print(jujtuso[0], "-> ele pertence ao anime Jujutso Kaisen!")
elif nomePersonagem == "Itadori":
    print(jujtuso[1], "-> ele pertence ao anime Jujutso Kaisen!")
elif nomePersonagem == "Vegeta":
    print(dragonBall[0], "-> ele pertence ao anime Dragon Ball!")
elif nomePersonagem == "Goku":
    print(dragonBall[1], "-> ele pertence ao anime Dragon Ball!")
elif nomePersonagem == "Sakura":
    print(naruto[0], "-> ele pertence ao anime Naruto!")
elif nomePersonagem == "Hiddan":
    print(naruto[1],"-> ele pertence ao anime Naruto!")
else:
    print("ATENÇÃO!! VOCÊ PODE TER COLOCADO O NOME ERRADO")
