"""
Dadas duas listas P1 e P2, ambas com n valores reais que representam as 
notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um 
script em linguagem Python que solicite o valor de n, leia as notas e calcule a 
média da turma nas provas 1 e 2, imprimindo em qual das provas a turma 
obteve a melhor média.

"""

P1= []
P2= []
alunos = int(input("Quantos alunos tem na turma: "))
                  
for aluno in range(alunos):
    P1.append(float(input(f"Qual foi a nota do {aluno+1}ª aluno na 1º prova: ")))
    
for aluno in range(alunos):
    P2.append(float(input(f"Qual foi a nota do {aluno+1}ª aluno na 2º prova: ")))

media_1= sum(P1)/len(P1)
media_2= sum(P2)/len(P2)
print(end="\n\n")
print(f"Quantidade de alunos: {alunos}", end="\n\n") 
print(f"Notas da prova 1: {P1}")
print(f"Notas da prova 2: {P2}",end="\n\n")

print(f"Média da turma na prova 1: {media_1:.2f}")
print(f"Média da turma na prova 2: {media_2:.2f}", end="\n\n")

if media_1 > media_2:
    print("A turma obteve a melhor média na prova 1.")
elif media_2 > media_1:
    print("A turma obteve a melhor média na prova 2.")
elif media_1 == media_2:
    print("A turma teve a média igual nas duas provas.")

