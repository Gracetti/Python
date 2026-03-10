idade_anos = int(input("idade da pessoa:"))
idade_messes = int (input("idade em messes"))
idade_dias = float(input("idade em dias"))
idade_total = idade_anos * 365 + idade_messes * 30 + idade_dias
print (f"idade total em dias: {idade_total:.2f}")
