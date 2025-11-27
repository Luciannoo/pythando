# Um exercício clássico para não perder a line 

nota1 = float(input("nota um: "))
nota2 = float(input("nota dois: "))
nota3 = float(input("nota três: "))
nota4 = float(input("nota quatro: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("aluno aprovado!")
    print("sua média foi {} pontos".format(media))
elif media < 5:
    print("aluno reprovado!")
    print("sua média foi {} pontos".format(media))
elif media > 5 or media <= 6.9:
    print("aluno de recuperação!")
    print("sua média foi {} pontos".format(media))

