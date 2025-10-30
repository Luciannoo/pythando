# calculando a área de uma parede para pintar 

# definindo a área que um litro de tinta pinta
areaLitro = 2

# obtendo dados
largura = float(input("Qual a largura da sua parede? "))
altura = float(input("Qual a altura da sua parede? "))

# calculando a área
area = largura * altura

quantTinta = area / areaLitro

print(f"A quantidade de litros para pintar a parede vai ser {quantTinta:.2f}")
