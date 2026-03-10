#quantidades
q_canetas = int(input("quantidade de canetas: "))
q_lapis = int(input("quantidade de lapis: "))
q_cadernos = int(input("quantidade de cadernos: "))

#preços
p_caneta = float(input("preço da caneta: "))
p_lapis = float(input("preço do lapis: "))
p_caderno = float (input("preço do caderno: "))

#descontos
total_canetas = q_canetas * q_canetas * 0.95
total_lapis = q_lapis * p_lapis
total_caderno = q_cadernos * p_caderno * 0.80

total = total_canetas + total_lapis + total_caderno
print("total da compra:", total)
