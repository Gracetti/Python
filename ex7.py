# inicio
# ler temperatura fahrenheit
# calcular celsius = 5/9 x (f - 32)
# mostarar valor em celsius
# fim 

temperatura_fahrenheit = float(input("temperatura em fahrenheit:"))
temperatura_celsius = 5/9 * (temperatura_fahrenheit - 32)
print(f"temperatura em celsius: {temperatura_celsius:.2f}")