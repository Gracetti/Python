quantidade = int(input("qual o numero de maças:"))
if quantidade <= 12:
    preço = 1.30
else:
    preço = 1.00

    total = quantidade * preço
    print("valor total a pagar e: R$", total)
        