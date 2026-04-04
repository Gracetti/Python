soma = 0
menor_salario = float('inf')
maior_salario = 0

nome_menor = ""
nome_maior = ""

for i in range(5):
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário: "))

    soma += salario

    if salario < menor_salario:
        menor_salario = salario
        nome_menor = nome

    if salario > maior_salario:
        maior_salario = salario
        nome_maior = nome

media = soma / 5

print(f"A média salarial dos funcionários da empresa XXX é {media:.2f}")
print(f"Funcionário com menor salário: {nome_menor} - {menor_salario:.2f}")
print(f"Funcionário com maior salário: {nome_maior} - {maior_salario:.2f}")
