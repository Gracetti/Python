total = 0

preco = float(input("Digite o preço do produto (0 para finalizar): "))

while preco != 0:
    quantidade = int(input("Digite a quantidade: "))
    total += preco * quantidade

    preco = float(input("Digite o preço do produto (0 para finalizar): "))

print("Total da compra: R$", total)

