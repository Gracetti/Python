n1 = int(input("digite o primeiro numero "))
n2 = int(input("digite o segundo numero "))
opçao = int(input("escolha (1, 2 ou 3): "))

match opçao:
    case 1:
        if n1 > n2:
            print("maior:", n1)
        else:
            print("maior:", n2)

    case 2:
        if n1 % 2 == 0:
            print("primeiro numero e PAR")
        else:
            print("segundo numero e IMPAR")

    case 3:
        if n1 < n2:
            print("menor:", n1)
        else:
            print("menor:", n2)
    case _:
        print("opçao invalida")
        


