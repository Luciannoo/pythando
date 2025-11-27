# classificando a cateforia de um atleta de acordo com sua idade

from datetime import date

anoNascimento = int(input("idade de nascimento: "))
idade = date.today().year - anoNascimento

if idade <= 9:
    print("Sua categoria é MIRIM!")
elif idade <= 14:
    print("Sua categoria é INFANTIL!")
elif idade <= 19:
    print("Sua categoria é JUNIOR!")
elif idade <= 25:
    print("Sua categoria é SÊNIOR!")
else:
    print("Sua categoria é MASTER!")
