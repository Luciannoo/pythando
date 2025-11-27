# aplicando várias formas de pagamento de um produto

valorProduto = float(input("valor do produto: "))

print("escolha uma forma de pagamento degitando o número da opção: ")
print("1. dinheiro a vista")
print("2. cartão a vista")
print("3. cartão em duas vezes")
print("4. cartão com três parcelas ou mais\n")

opcaoPagamento = int(input("opção de pagamento: "))

if opcaoPagamento == 1:
    total = valorProduto - (valorProduto - 0.10)
    print("você reberá 10 por cento de desconconto")
    print("valor final do produto: {}".format(total))
elif opcaoPagamento == 2:
    total = valorProduto - (valorProduto - 0.05)
    print("você reberá 5 por cento de desconconto")
    print("valor final do produto: {}".format(total))
elif opcaoPagamento == 3:
    total = valorProduto
    print("valor final do produto: {}".format(valorProduto))
elif opcaoPagamento == 4:
    total = valorProduto + (valorProduto * 0.2)
    totalParcelas = int(input("quantas parcelas: "))
    parcela = total / totalParcelas
    print("você terá 20 por cento de juros")
    print("as parcelas ficarão de {}".format(parcela))
    print("valor final do produto: {}".format(total))
else:
    print("opção inválida!")