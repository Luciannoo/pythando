# verificando se já pode, se já passou ou se ainda vai se alistar
from datetime import date

anoNascimento = int(input("idade de nascimento: "))
idade = date.today().year - anoNascimento

if idade == 18:
    print("já pode se alistar")
elif idade < 18:
    print("ainda vai se alistar")
    anosFaltam = 18 - idade
    print("faltam ainda {} anos para se alistar".format(anosFaltam))
elif idade > 18:
    print("já passou do tempo de se alistar")
    anosPassou = idade - 18 
    print("passou {} anos do prazo de alistamento".format(anosPassou))


