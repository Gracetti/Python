ingles = []
portugues = []

while True:
    op = int(input("Deseja continuar (1-SIM / 0-NÃO): "))
    if op == 0:
        break

    palavra_en = input("Palavra em inglês: ")
    palavra_pt = input("Tradução em português: ")

    ingles.append(palavra_en)
    portugues.append(palavra_pt)

busca = input("Digite a palavra em inglês para traduzir: ")

if busca in ingles:
    pos = ingles.index(busca)
    print("Tradução:", portugues[pos])
else:
    print("Palavra não encontrada.")

    