nro_horas_mes = int(input("Digite o numero de horas trabalhadas em um mes: "))
valor_hora_regular = float(input("Digite o valor da hora regular: "))

if (nro_horas_mes > 160): # exisye horas extras 
    nro_horas_extras = nro_horas_mes - 160
    valor_hora_extra = valor_hora_regular * 1.50
    salario_total = (160 * valor_hora_regular) + (nro_horas_extras * valor_hora_extra)
else: #nao existe horas extras 
    salario_total = nro_horas_mes * valor_hora_regular

    print("O salario total do funcionario eh")
    print(salario_total)
