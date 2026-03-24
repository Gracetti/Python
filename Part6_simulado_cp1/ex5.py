nome = input("Digite o nome do funcionario: ")
salario_bruto = float(input("Digite o salario bruto do funcionario: "))
if (salario_bruto <= 1100):
    des_INSS = salario_bruto * 0.075
elif (salario_bruto <= 2203.48):
    des_INSS = salario_bruto * 0.09
elif (salario_bruto <= 3305.22):
    des_INSS = salario_bruto * 0.12
elif (salario_bruto <= 6433.57):
    des_INSS = salario_bruto * 0.14

print(f"O desconto do INSS eh: {des_INSS:.2f}")