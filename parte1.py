print("=" * 50)
print("EXERCÍCIO 1 - Lista de 10 zeros com for")
print("=" * 50)

numeros = [0] * 10
for valor in numeros:
    print(valor)


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 2 - While de 1 a 20")
print("=" * 50)

contador = 1
while contador <= 20:
    print(contador)
    contador += 1


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 3 - Função soma_valores")
print("=" * 50)

def soma_valores(a, b):
    return a + b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = soma_valores(num1, num2)
print(f"A soma de {num1} + {num2} = {resultado}")


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 4 - Lista de cidades do Paraná")
print("=" * 50)

cidades = ["Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel"]
for cidade in cidades:
    print(cidade)


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 5 - Função verifica_par")
print("=" * 50)

def verifica_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número inteiro: "))
if verifica_par(num):
    print(f"{num} é PAR")
else:
    print(f"{num} é ÍMPAR")


# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EXERCÍCIO 6 - While até digitar 0")
print("=" * 50)

numero = int(input("Digite um número inteiro (0 para sair): "))
while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))

print("Programa encerrado")