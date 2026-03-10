# inicio 
#ler peso
# ler altura 
# calcular IMC = peso / (altura x altura)
# mostrar IMC
# fim 

peso_pessoa = float(input("digita o peso:"))
altura_pessoa = float(input("digita a altura:"))
imc = peso_pessoa / altura_pessoa ** 2
print(f"IMC: {imc:.2f}")