inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma = 0

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i

print("Somatório dos números pares:", soma)
