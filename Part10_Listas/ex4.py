numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

maior = max(numeros)
posicao = numeros.index(maior)

print("Maior número:", maior)
print("Posição:", posicao)

