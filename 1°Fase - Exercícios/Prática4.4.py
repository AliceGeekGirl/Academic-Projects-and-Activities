"""
Crie um script em linguagem Python que leia duas listas com 5 
elementos cada. Gere uma terceira lista de 10 elementos, cujos 
valores deverão ser compostos pelos elementos intercalados dos dois 
outros vetores. Exibir na tela todas as listas em linhas separadas.

"""

lista_1= []
lista_2= []

for i in range(5):
    lista_1.append(int(input("Digite um número: ")))
for x in range(5):
    lista_2.append(input("Digite alguma coisa: "))

lista_3= lista_1 + lista_2

print(lista_1)
print(lista_2)
print(lista_3)
print(len(lista_3))
