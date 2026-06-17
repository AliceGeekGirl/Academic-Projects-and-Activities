"""
Desenvolva um script em linguagem Python que peça as quatro 
notas de 10 alunos, calcule e armazene em uma lista a média de cada 
aluno, imprima o número de alunos com média maior ou igual a 7

"""
alunos= []
qtdAlunos= 10
qtdNotas= int(input("Quantas notas são por aluno? ")) 

for aluno in range(qtdAlunos): #Inicia um loop que executa qtdAlunos vezes.
    notas=[]
    for nota in range(qtdNotas): #Inicia um loop interno para pedir e armazenar as notas do aluno atual.
        notas.append(float(input(f"Qual a {nota+1}ª nota do {aluno+1}º aluno: ")))
    alunos.append(sum(notas)/len(notas))

contador= 0

for indice in alunos:
    if indice >= 7:
        contador += 1

print(f"Total de alunos aprovados: {contador}")
