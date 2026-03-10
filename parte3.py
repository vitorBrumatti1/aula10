# EXERCÍCIO 12 - Sistema de boletim escolar

print("=" * 50)
print("EXERCÍCIO 12 - Boletim Escolar")
print("=" * 50)

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

nomes = []
medias = []

for i in range(5):
    print(f"\n--- Aluno {i+1} ---")
    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    media = calcular_media(n1, n2, n3)
    nomes.append(nome)
    medias.append(media)

print("\n" + "=" * 50)
print("BOLETIM FINAL")
print("=" * 50)

for i in range(len(nomes)):
    if medias[i] >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"Aluno: {nomes[i]} | Média: {medias[i]:.2f} | Situação: {situacao}")


# EXERCÍCIO 13 - Faturamento semanal do restaurante

print("\n" + "=" * 50)
print("EXERCÍCIO 13 - Faturamento Semanal")
print("=" * 50)

def total_faturamento(faturamentos):
    total = 0
    for valor in faturamentos:
        total += valor
    return total

def dia_maior_faturamento(faturamentos):
    maior = faturamentos[0]
    for valor in faturamentos:
        if valor > maior:
            maior = valor
    return maior

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
faturamentos = []

for dia in dias:
    while True:
        valor = float(input(f"Faturamento de {dia}: R$ "))
        if valor >= 0:
            faturamentos.append(valor)
            break
        else:
            print("Valor inválido! Digite um valor maior ou igual a zero.")

total = total_faturamento(faturamentos)
media_diaria = total / len(faturamentos)
maior = dia_maior_faturamento(faturamentos)

print("\n--- Relatório Semanal ---")
print(f"Faturamento total da semana: R$ {total:.2f}")
print(f"Média diária de faturamento: R$ {media_diaria:.2f}")
print(f"Maior faturamento registrado: R$ {maior:.2f}")


# EXERCÍCIO 14 - Simulador de estoque agrícola

print("\n" + "=" * 50)
print("EXERCÍCIO 14 - Sistema de Estoque Agrícola")
print("=" * 50)

def aplicar_desconto(lista_precos, percentual):
    for i in range(len(lista_precos)):
        lista_precos[i] = lista_precos[i] * (1 - percentual / 100)

produtos = []
precos = []

opcao = 0
while opcao != 4:
    print("\n--- MENU ---")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Aplicar Desconto")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: R$ "))
        produtos.append(nome)
        precos.append(preco)
        print("Produto cadastrado com sucesso!")

    elif opcao == 2:
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\n--- PRODUTOS CADASTRADOS ---")
            for i in range(len(produtos)):
                print(f"{produtos[i]} - R$ {precos[i]:.2f}")

    elif opcao == 3:
        if len(precos) == 0:
            print("Nenhum produto cadastrado para aplicar desconto.")
        else:
            desconto = float(input("Informe a porcentagem de desconto: "))
            aplicar_desconto(precos, desconto)
            print(f"Desconto de {desconto}% aplicado com sucesso!")

    elif opcao == 4:
        print("Saindo do sistema...")

    else:
        print("Opção inválida! Tente novamente.")


# EXERCÍCIO 15 - Simulador de caixa eletrônico

print("\n" + "=" * 50)
print("EXERCÍCIO 15 - Caixa Eletrônico")
print("=" * 50)

def sacar(saldo, valor):
    if valor > saldo:
        print("Saldo insuficiente!")
        return saldo
    else:
        return saldo - valor

def depositar(saldo, valor):
    return saldo + valor

saldo = 1000.00
historico = []

opcao = 0
while opcao != 4:
    print("\n--- MENU ---")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Informe o valor do saque: R$ "))
        novo_saldo = sacar(saldo, valor)
        if novo_saldo != saldo:
            saldo = novo_saldo
            historico.append(f"Saque realizado no valor de {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        valor = float(input("Informe o valor do depósito: R$ "))
        saldo = depositar(saldo, valor)
        historico.append(f"Depósito realizado no valor de {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {saldo:.2f}")

    elif opcao == 3:
        print("\n--- EXTRATO ---")
        if len(historico) == 0:
            print("Nenhuma transação realizada.")
        else:
            for transacao in historico:
                print(transacao)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 4:
        print("Obrigado por usar nosso caixa eletrônico!")

    else:
        print("Opção inválida! Tente novamente.")