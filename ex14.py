votos_brancos = int(input("valor votos brancos"))
votos_nulos = int (input("valor dos votos nulos"))
votos_validos = int (input("valor dos votos validos"))

total_votos = votos_brancos + votos_nulos + votos_validos

percentual_brancos = votos_brancos / total_votos *100
percentual_nulos = votos_nulos / total_votos *100
percentual_validos = votos_validos / total_votos *100

print (f"percentual de votos brancos: {percentual_brancos:.2f}%")
print (f"porcentual de votos nulos: {percentual_nulos:.2f}%")
print (f"porcentual de votos validos: {percentual_validos:.2f}%")
