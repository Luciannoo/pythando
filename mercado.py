# valor dos itens
caneta = 1.3
oleo = 8.9
creme = 10

# quantidade de cada item a ser levado
quantCaneta = int(input("Quantas canetas são: "))
quantOleo = int(input("Quantas óleos são: "))
quantCreme = int(input("Quantas cremes são: "))

# cálculo de todos os produtos 
valorConta = (caneta * quantCaneta) + (oleo * quantOleo) + (creme * quantCreme)

# imprimindo o valor a ser pago
print(f"O valor total da compra é: {valorConta: .2f}")