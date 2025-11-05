# fazendo um dos exercicios que são rituais de passagem 

nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))
nota3 = float(input("terceira nota: "))
nota4 = float(input("quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6:
    print("mandou bem! sua nota foi: {}".format(media))
else:
    print("mandou mal! sua nota foi: {}".format(media))
