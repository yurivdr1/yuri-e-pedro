nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificar aprovação
if media < 3.0:
    print(f"{nome} foi reprovado com média {media:.2f}.")
elif media <= 5.0:
    print(f"{nome} está em exame com média {media:.2f}.")
else:
    print(f"{nome} foi aprovado com média {media:.2f}.")