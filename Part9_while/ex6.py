continuar = "S"

while continuar == "S":

    x = int(input("Digite um número: "))

    print("Menu:")
    print("1 - Verificar se o número é divisível por 6")
    print("2 - Calcular o fatorial do número")
    print("3 - Mostrar todos os inteiros de 1 até o número")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if x % 6 == 0:
            print("O número é divisível por 6")
        else:
            print("O número NÃO é divisível por 6")

    elif opcao == 2:
        fatorial = 1
        contador = 1

        while contador <= x:
            fatorial *= contador
            contador += 1

        print("Fatorial:", fatorial)

    elif opcao == 3:
        contador = 1
        while contador <= x:
            print(contador)
            contador += 1

    else:
        print("Opção inválida")

    continuar = input("Deseja continuar? (S/N): ").upper()

print("Programa encerrado")

