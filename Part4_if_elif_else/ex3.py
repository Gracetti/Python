preço = float(input("digite o preço do livro: "))

if preço <= 10:
    desconto = preço * 0.08
elif preço <= 60:
    desconto = preço * 0.10
else:
    desconto = preço * 0.20

print(f"desconto: R$ {desconto:.2f}")