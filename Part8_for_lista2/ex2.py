num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

pares = 0
impares = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
