eleitores = int(input("Número de eleitores: "))

c1 = 0
c2 = 0
c3 = 0

for i in range(eleitores):
    voto = int(input("Vote (1, 2 ou 3): "))
    
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1

print("Candidato 1:", c1)
print("Candidato 2:", c2)
print("Candidato 3:", c3)

