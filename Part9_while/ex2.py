soma = 0
contador = 0

reprovados = 0
exame = 0
aprovados = 0

nota = float(input("Digite a nota do aluno (negativa para parar): "))

while nota >= 0:
    soma += nota
    contador += 1

    if nota < 3.5:
        reprovados += 1
    elif nota <= 7:
        exame += 1
    else:
        aprovados += 1

    nota = float(input("Digite a nota do aluno (negativa para parar): "))

if contador > 0:
    media = soma / contador
    print("Média da turma:", media)

print("Aprovados:", aprovados)
print("Reprovados:", reprovados)
print("Exame:", exame)
