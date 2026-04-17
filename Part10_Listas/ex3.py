notas = []

while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)

qtd = len(notas)
soma = sum(notas)
media = soma / qtd if qtd > 0 else 0

acima_media = sum(1 for n in notas if n > media)
abaixo_sete = sum(1 for n in notas if n < 7)

print("Quantidade:", qtd)
print("Soma:", soma)
print("Média:", media)
print("Acima da média:", acima_media)
print("Abaixo de 7:", abaixo_sete)

