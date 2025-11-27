# convertendo números para binário, octal e hexadecimal

numero = int(input("digite um número: "))
binario = bin(numero)
decimal = oct(numero)
hexadecimal = hex(numero)

# crio as opções usando uma lista
bases = [binario, decimal, hexadecimal]

print("para binário, digite 1")
print("para decimal, digite 2")
print("para hexadecimal, digite 3\n")

opcao = int(input("digite uma das opções acima: "))

if opcao == 1:
    print(bases[0])
elif opcao == 2:
    print(bases[1])
elif opcao == 3:
    print(bases[3])


# LITERALMENTE OPTEI ESCREVER MAIS LINHAS DE CÓDIGOS