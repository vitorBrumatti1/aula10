print("=" * 50)
print("EXERCÍCIO 7 - Lista com 5 números do usuário")
print("=" * 50)

lista = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    lista.append(num)

print("Lista completa:", lista)


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 8 - Função maior_valor")
print("=" * 50)

def maior_valor(lista_numeros):
    maior = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior:
            maior = numero
    return maior

minha_lista = [34, 7, 89, 12, 56, 3, 100, 45]
print("Lista:", minha_lista)
print("Maior valor:", maior_valor(minha_lista))


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 9 - Idades e maiores de 18")
print("=" * 50)

def contar_maiores_18(lista_idades):
    contagem = 0
    for idade in lista_idades:
        if idade > 18:
            contagem += 1
    return contagem

idades = []
idade = int(input("Digite uma idade (-1 para parar): "))
while idade >= 0:
    idades.append(idade)
    idade = int(input("Digite uma idade (-1 para parar): "))

print("Idades registradas:", idades)
print("Maiores de 18 anos:", contar_maiores_18(idades))


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 10 - Função calcula_media")
print("=" * 50)

def calcula_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

notas_aluno = [7.5, 8.0, 6.5, 9.0]
print("Notas:", notas_aluno)
print(f"Média: {calcula_media(notas_aluno):.2f}")


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 11 - Filtrar números pares")
print("=" * 50)

def filtrar_pares(lista_numeros):
    pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

lista_pares = filtrar_pares(numeros)
print("Números digitados:", numeros)
print("Apenas os pares:", lista_pares)