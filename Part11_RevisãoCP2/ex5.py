total_salario = 0
total_filhos = 0
contador = 0
maior_salario = 0
baixo_salario = 0

while True:
    salario = float(input("Digite o salário (negativo para sair): "))
    
    if salario < 0:
        break
    
    filhos = int(input("Número de filhos: "))
    
    total_salario += salario
    total_filhos += filhos
    contador += 1
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario < 150:
        baixo_salario += 1

if contador > 0:
    media_salario = total_salario / contador
    media_filhos = total_filhos / contador
    percentual = (baixo_salario / contador) * 100

    print("Média salário:", media_salario)
    print("Média filhos:", media_filhos)
    print("Maior salário:", maior_salario)
    print("Percentual salário < 150:", percentual, "%")
else:
    print("Nenhum dado informado.")

    