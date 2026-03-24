qtde_fritas = int(input("Digite a quantidade de dritas: "))
qtde_pasteis = int(input("Digite a quantidade de pasteis: "))
qtde_cervejas = int(input("Digite a quantidde de cervejas: "))

nro_amigos = int(input("Digite a quantidade de amigos na mesa: "))

valor_total = (qtde_fritas * 5) + (qtde_pasteis * 7) + (qtde_cervejas * 10)

print(f"O valor total da conta eh: {valor_total:.2f}")
valor_por_amigo = valor_total / nro_amigos
print(f"O valor por amigo eh: {valor_por_amigo:.2f}")