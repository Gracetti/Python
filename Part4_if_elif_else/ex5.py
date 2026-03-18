morango = float(input("kg de morango:" ))
maça = float(input("kg de maça: "))

#preço
if morango <= 5: 
    preço_morango = morango * 2.50
else:
    preço_morango = morango * 2.20

if maça <= 5:
    preço_maça = maça * 1.80
else:
    preço_maça = maça * 1.50

total = preço_morango + preço_maça

#desconto
if morango + maça > 8 or total > 25:
    total = total * 0.90

print("total a pagar:R$",  total)
