numeros = []
multiplos = 0

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 3 == 0:
        multiplos += 1

print("Quantidade de múltiplos de 3:", multiplos)

