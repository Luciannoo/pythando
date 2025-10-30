# verificando os tipos primitivos 
entrada = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(entrada))
print("Ele é somente espaços? ", entrada.isspace())
print("Ele é numérico? ", entrada.isnumeric())
print("Ele tem letras maisuculas? ", entrada.isupper())
print("Ele é alfa númerico? ", entrada.isalnum())