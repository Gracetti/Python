carros = int(input("quantidade de carros vendidios: "))
valor_vendas = float(input("valor total das vendas: "))
salario_fixo = float(input("salario fixo: "))
comissao = float(input("comissao por carro: "))

salario_final = salario_fixo + (carros * comissao) + (valor_vendas * 0.05)
print ("salario final do vendedor eh:", salario_final)
