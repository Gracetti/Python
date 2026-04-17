dentro = 0
fora = 0

for i in range(10):
    valor = int(input("Digite um valor: "))
    
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1

print("Dentro do intervalo:", dentro)
print("Fora do intervalo:", fora)

