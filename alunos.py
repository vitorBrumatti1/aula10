alunos = [""] * 5
alunos[0] = "Falano de Tal"
alunos[1] = "Ciclano"
for i in range (2, 5): 
    alunos [i] = input("nome do aluno: ")

print("Lista de alunos: ")
valor = 0
while valor < len(alunos) :
    print(f"Aluno {valor}: ", alunos[valor])
    valor = valor + 1