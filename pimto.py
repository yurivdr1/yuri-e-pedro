# Sistema de Fila de Atendimento com cálculo de idade

from collections import deque
from datetime import datetime

def calcular_idade(ano_nascimento):
    """Calcula a idade a partir do ano de nascimento."""
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


def classificar_fila(idade):
    """Retorna a fila correta baseado na idade."""
    if idade < 60:
        return "FILA NORMAL"
    elif 60 <= idade < 80:
        return "FILA ESPECIAL"
    else:
        return "FILA 80+"


def adicionar_pessoa(fila_normal, fila_especial, fila_80_mais):
    """Adiciona uma pessoa à fila apropriada baseado na idade calculada."""
    nome = input("Digite o nome da pessoa: ").strip()
    
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            ano_atual = datetime.now().year
            if ano_nascimento > ano_atual or ano_nascimento < 1900:
                print("Ano inválido! Digite um ano entre 1900 e o ano atual.")
                continue
            break
        except ValueError:
            print("Erro! Digite um número válido para o ano.")
    
    idade = calcular_idade(ano_nascimento)
    fila = classificar_fila(idade)
    
    pessoa = {"nome": nome, "idade": idade, "ano_nascimento": ano_nascimento}
    
    # Exibir informações da pessoa
    print("\n" + "="*50)
    print(f"Nome: {nome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
    print(f"Idade: {idade} anos")
    print(f"Fila: {fila}")
    print("="*50 + "\n")
    
    # Adicionar à fila apropriada
    if fila == "FILA NORMAL":
        fila_normal.append(pessoa)
    elif fila == "FILA ESPECIAL":
        fila_especial.append(pessoa)
    else:
        fila_80_mais.append(pessoa)
    
    print(f"✓ {nome} adicionado(a) com sucesso!\n")


def exibir_filas(fila_normal, fila_especial, fila_80_mais):
    """Exibe as três filas de atendimento."""
    print("\n" + "="*60)
    print(" SISTEMA DE FILA DE ATENDIMENTO")
    print("="*60)
    
    # Exibir fila 80+
    print("\n🔴 FILA 80+ (≥ 80 anos):")
    print("-" * 60)
    if len(fila_80_mais) == 0:
        print("   (Vazia)")
    else:
        for idx, pessoa in enumerate(fila_80_mais, 1):
            print(f"   {idx}. {pessoa['nome']} - {pessoa['idade']} anos")
    
    # Exibir fila especial
    print("\n🟡 FILA ESPECIAL (≥ 60 e < 80 anos):")
    print("-" * 60)
    if len(fila_especial) == 0:
        print("   (Vazia)")
    else:
        for idx, pessoa in enumerate(fila_especial, 1):
            print(f"   {idx}. {pessoa['nome']} - {pessoa['idade']} anos")
    
    # Exibir fila normal
    print("\n🟢 FILA NORMAL (< 60 anos):")
    print("-" * 60)
    if len(fila_normal) == 0:
        print("   (Vazia)")
    else:
        for idx, pessoa in enumerate(fila_normal, 1):
            print(f"   {idx}. {pessoa['nome']} - {pessoa['idade']} anos")
    
    print("\n" + "="*60)


def chamar_proximo(fila_normal, fila_especial, fila_80_mais):
    """Chama o próximo da fila (respeitando prioridades)."""
    if len(fila_80_mais) > 0:
        pessoa = fila_80_mais.popleft()
        print(f"\n🔔 Chamando: {pessoa['nome']} ({pessoa['idade']} anos - Fila 80+)\n")
    elif len(fila_especial) > 0:
        pessoa = fila_especial.popleft()
        print(f"\n🔔 Chamando: {pessoa['nome']} ({pessoa['idade']} anos - Fila Especial)\n")
    elif len(fila_normal) > 0:
        pessoa = fila_normal.popleft()
        print(f"\n🔔 Chamando: {pessoa['nome']} ({pessoa['idade']} anos - Fila Normal)\n")
    else:
        print("\n⚠️  Não há pessoas na fila!\n")


def menu():
    """Exibe o menu principal."""
    fila_normal = deque()
    fila_especial = deque()
    fila_80_mais = deque()
    
    while True:
        print("\n" + "="*60)
        print(" MENU PRINCIPAL")
        print("="*60)
        print("1. Adicionar pessoa à fila")
        print("2. Exibir filas de atendimento")
        print("3. Chamar próximo cliente")
        print("4. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            adicionar_pessoa(fila_normal, fila_especial, fila_80_mais)
        elif opcao == "2":
            exibir_filas(fila_normal, fila_especial, fila_80_mais)
        elif opcao == "3":
            chamar_proximo(fila_normal, fila_especial, fila_80_mais)
        elif opcao == "4":
            print("\n👋 Encerrando o programa. Até logo!\n")
            break
        else:
            print("\n❌ Opção inválida! Digite um número de 1 a 4.\n")


if __name__ == "__main__":
    menu()
