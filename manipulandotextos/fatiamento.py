# fatiando uma frase

frase0 = "Manipulando Texto em Python"
#identifica o caractere que está na posição 5 da frase
print(frase0[5]) 

print("===============================")

frase1 = "Manipulando Texto em Python"
#vai do índice 12 até o 16 mas o 16 fica de fora
print(frase1[12:16]) 

print("===============================")

frase2 = "Manipulando Texto em Python"
#vai pegar os caractere do índice 12 até o 23 saltando dois índices 
print(frase2[12:23:2]) 

print("===============================")

frase3 = "Manipulando Texto em Python"
# sem indicar um índice antes dos : equivale a dizer que vai começar do 0 até o 5
print(frase3[:5])

print("===============================")

frase4 = "Manipulando Texto em Python"
# sem indicar um índice no final, ele vai pegar do íncide antes dos : até o final 
print(frase4[12:])

print("===============================")

frase5 = "Manipulando Texto em Python"
# ele vai do índice 1 até o final, mas saltando três indíces 
print(frase5[1::3])

print("===============================")
