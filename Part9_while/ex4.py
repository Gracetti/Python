senha_correta = 1234
senha = int(input("Digite a senha: "))

while senha != senha_correta:
    print("Senha incorreta")
    senha = int(input("Digite a senha novamente: "))

print("Acesso permitido")

