salario = float(input("Digite o salario do funcionario: "))
total_vendas = float(input("Digite o total de vendas do funcionario: "))

if (total_vendas <= 5000):
    salario = salario * 1.10
else:
    salario = salario * 1.20

print(f"O salario total do funcionario eh: {salario:.2f}")