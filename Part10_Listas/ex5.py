idades = []

while True:
    idade = int(input("Digite a idade (negativo para sair): "))
    if idade < 0:
        break
    idades.append(idade)

menores = sum(1 for i in idades if i < 18)
media = sum(idades) / len(idades) if len(idades) > 0 else 0

print("Menores de 18:", menores)
print("Média das idades:", media)

