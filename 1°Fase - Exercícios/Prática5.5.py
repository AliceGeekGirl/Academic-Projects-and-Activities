"""
Dada uma lista L de n valores inteiros, elabore um Script em linguagem 
Python que remova todos os números ímpares da lista.

"""

L=[]

for i in range(10):
    L.append(int(input("Insira um número inteiro: ")))

numero_par= []

for par in L:
    if par % 2 == 0:
        numero_par.append(par)

print(L)
print(numero_par)

