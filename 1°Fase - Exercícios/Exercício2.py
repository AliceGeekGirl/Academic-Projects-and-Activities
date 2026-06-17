
"""
Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem 
um desconto de 35%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 
centavos para cada exemplar adicional. Qual é o custo total de atacado para X 
cópias? Solicite o valor de X. Crie um Script em linguagem Python para solicitar os 
dados necessários e exibir o custo total da compra.

"""

capaLivro= float(input("Insira o valor do livro (R$): "))
desconto= float(input("Insira o desconto: "))
transporte= float(input("Insira o valor do transporte: "))
adicional= float(input("Insira o valor adicional: "))
copias= float(input("Insira o número de cópias: "))
copiasRestantes= float(input("Insira as cópias restantes: "))


x= (capaLivro*desconto/100*copias)+(transporte+(adicional*copiasRestantes))

print(f"Qual é o custo total de atacado para X cópias: R${x:,.2f}")
