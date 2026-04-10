soma = 0
contador = 0

numero = float(input("Digite um número positivo (0 para parar): "))

while numero != 0:
    soma += numero
    contador += 1
    numero = float(input("Digite um número positivo (0 para parar): "))

if contador > 0:
    media = soma / contador
    print("Média:", media)
else:
    print("Nenhum número foi digitado")
    