x = float(input("digite um numero: "))
opçao = int(input("escolha (1, 2 ou 3): "))

match opçao:
    case 1:
        print(x + 5)
    case 2:
        print(x - 4)
    case 3:
        print(x * 2)
    case _:
        print("opçao invalida")
        