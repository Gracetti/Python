#formula = preço_final = custo + (custo * 0.28) + (custo * 0.45)

custo = float(input("digite o custo da fabrica e do carro"))

distribuidor = custo * 0.28
imposto = custo * 0.45

preço_final = custo + distribuidor + imposto 
print("preço para o consumidor", preço_final)
