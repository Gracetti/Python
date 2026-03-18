peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("abaixo do peso")
elif imc <= 24.9:
    print("peso ideal")
else:
    print("acima do peso")
