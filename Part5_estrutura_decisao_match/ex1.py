codigo = int(input("digite o codigo do produto: "))

match codigo:
    case 1:
        print("caneta - R$ 1.20")
    case 2:
        print("lapis - R$ 0.80")
    case 3:
        print("caderno - R$ 4.50")
    case 4:
        print("borracha - R$ 1.00")
    case 5:
        print("regua - R$ 1.50")
    case _:
        print("produto não cadastrado")
    