lista_a = []
lista_b = []

for i in range(12):
    valor = int(input("Digite um número: "))
    lista_a.append(valor)

for num in lista_a:
    if num % 2 != 0:
        lista_b.append(num * 2)
    else:
        lista_b.append(num)

print("Lista A:", lista_a)
print("Lista B:", lista_b)

