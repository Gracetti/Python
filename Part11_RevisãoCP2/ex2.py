n = int(input("Digite o valor de n: "))

soma = 0
denominador = 1

for i in range(1, n + 1):
    soma += i / denominador
    denominador += 2

print("Valor da série:", soma)

