ano = int(input("digite um ano: "))

if ano < 1000 or ano > 2999:
    print("ano invalido")
else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("ano bissexto")
    else:
        print("nao e bissexto")
        