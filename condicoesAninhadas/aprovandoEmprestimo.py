# mais um dos exercicío do Guanabara 
valorCasa = float(input("valor da casa: R$"))
meuSalario = float(input("valor do salário: R$"))
anosQuitacao = float(input("em quantos anos pretende quitar: "))
prestacaoMensal = valorCasa / (anosQuitacao * 12) #verifica o valor da parcela

print("valor da prestação: {}".format(prestacaoMensal))

prestacaoMinima = meuSalario * 0.3 #calcula 30% do salário para pagar a casa

if prestacaoMensal <= prestacaoMinima:
    print("continue firme, logo você pagará")
else:
    print("seu emprestimo foi negado")