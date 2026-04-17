numeros = []
pares = []
impares = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista completa:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)

