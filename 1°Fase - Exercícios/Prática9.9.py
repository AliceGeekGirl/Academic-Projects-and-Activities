"""
Desenvolva um Script em linguagem Python que adicione em um 
dicionário “d” os seguintes campos: nome, idade, endereço e telefone e 
mostre os dados no final.

"""

d= {'Nome': 0, 'Idade': 0, 'Endereço': 0, 'Telefone': 0}

nome= input("Digite o seu nome: ")
idade= int(input("Digite sua idade: "))
endereco= input("Digite o seu endereço: ")
telefone= int(input("Digite o seu telefone: "))

d.update({'Nome': nome})
d.update({'Idade': idade})
d.update({'Endereço': endereco})
d.update({'Telefone': telefone})

print(d)

