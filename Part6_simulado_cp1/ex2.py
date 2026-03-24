nome_pessoa1 = input("Digite o nome: ")
altura_pessoa1 = float(input("Digite a altura: "))
nome_pessoa2 = input("Digite o nome: ")
altura_pessoa2 = float(input("Digite a altura: "))

if (altura_pessoa1 > altura_pessoa2):
    print(f"{nome_pessoa1} eh a pessoa mais alta")
elif (altura_pessoa2 > altura_pessoa1):
    print(f"{nome_pessoa2} eh a pessoa mais alta")
else:
    print("As pessoas tem a mesma altura")