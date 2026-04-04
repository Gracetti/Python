taxa = float(input("Digite a taxa de abatimento (%): "))
prestacoes = int(input("Digite o número de prestações: "))
valor = float(input("Digite o valor da primeira prestação: "))

for i in range(prestacoes):
    print(f"Prestação {i+1}: {valor:.2f}")
    valor = valor - (valor * taxa / 100)
    