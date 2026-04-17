medias = []
aprovados = 0

for i in range(10):
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    media = (n1 + n2 + n3) / 3
    medias.append(media)

    if media >= 7:
        aprovados += 1

print("Médias:", medias)
print("Quantidade com média >= 7:", aprovados)

