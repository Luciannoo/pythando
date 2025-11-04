# analise de uma frase (qual o tam, primeira letra ou última, etc...)
frase0 = "Manipulando Texto em Python"
# mostra o tamanho da frase (no caso, a quantidade de caracteres)
print(len(frase0))

print("===============================")

frase1 = "Manipulando Texto em Python"
# contando quantas vezes aparece uma letra na frase
print(frase1.count("o"))

print("===============================")

frase2 = "Manipulando Texto em Python"
# contagem das letras que se repetem com fatiamento do índice 0 até o 17
print(frase2.count("o", 0, 17))

print("===============================")

frase3 = "Manipulando Texto em Python"
# mostra onde começou os caracteres mencionados, ou seja, a sua posição
print(frase3.find("ando"))

print("===============================\n")
