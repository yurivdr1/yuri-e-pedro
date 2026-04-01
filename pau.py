# Programa para calcular IMC (Índice de Massa Corporal)

# Entrada de dados
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Peso normal"
elif imc <= 29.9:
    classificacao = "Excesso de peso"
elif imc <= 34.9:
    classificacao = "Obesidade 1"
elif imc <= 39.9:
    classificacao = "Obesidade 2"
else:
    classificacao = "Obesidade 3"

# Exibição dos resultados
print("\n" + "="*40)
print(f"Nome: {nome}")
print(f"Altura: {altura} m")
print(f"Peso: {peso} kg")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
print("="*40)
