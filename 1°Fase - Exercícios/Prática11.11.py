"""
Elabore um script em linguagem Python que, dados dois inteiros x e y, 
retorna uma lista com todos os valores entre x e y (inclusive), considerando x < 
y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]

"""

x= int(input("Digite o primeiro número: "))
y= int(input("Digite o segundo número: "))

if x < y:
    lista=list(range(x,y+1))
    print(lista)
else:
    print("Escolha um número que seja menor que o segundo número")

