"""
De acordo com a tupla Vendas apresentada abaixo. Desenvolva um 
script em linguagem Python que calcule a média, a Variância, o Desvio 
Padrão, o menor valor e o maior Valor deste conjunto.

"""
import math

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)
soma_quadrados_diferencas = 0 #acumulador

media= sum(Vendas)/len(Vendas)

for x in Vendas:
    soma_quadrados_diferencas += (x - media) ** 2

variancia= soma_quadrados_diferencas / len(Vendas)

desvio= math.sqrt(variancia)
maior= max(Vendas)
menor= min(Vendas)

print(f"As vendas foram {Vendas}")
print(f"A média das vendas foi {media:.2f}")
print(f"A variância das vendas foi {variancia:.2f}")
print(f"O desvio padrão das vendas foi {desvio:.2f}")
print(f"A maior venda foi {maior}")
print(f"A menor venda foi {menor}")
