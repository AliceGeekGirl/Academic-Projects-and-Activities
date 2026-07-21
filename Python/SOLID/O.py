"""
OCP — Aberto/Fechado
Cenário errado
Crie uma função de desconto que usa if e elif para cada tipo de cliente:

cliente comum;
cliente VIP;
cliente premium.

Sempre que surgir um novo tipo, você vai precisar alterar a função.

Cenário correto
Crie uma classe base Desconto e classes filhas como:

DescontoComum;
DescontoVIP;
DescontoPremium.

O que observar
Na versão correta, você adiciona novos comportamentos sem mexer no código antigo.
"""

"""
MÉTODO ERRADO: 
"""

#Criando uma função rígida que viola o Princípio Aberto/Fechado (OCP)
def desconto(tipo_cliente, valor):

    #Usa uma estrutura de escolhas para decidir a porcentagem do desconto
    if tipo_cliente == "comum":
        return valor * 0.05  #5% de desconto para cliente comum
    elif tipo_cliente == "VIP":
        return valor * 0.10  #10% de desconto para cliente VIP
    elif tipo_cliente == "Premium":
        return valor * 0.15  #15% de desconto para cliente Premium
    
    #Caso o tipo digitado não exista nos 'ifs' acima, avisa e não aplica desconto
    else:
        print(f"Aviso: Tipo de cliente '{tipo_cliente}' não reconhecido.")
        return 0.0

#Recebe o valor total da compra do usuário e converte para número decimal (float)
valor= float(input("Qual o seu valor: "))

#Recebe a categoria do cliente
tipo= input("Que tipo de cliente é você: ")

#Chama a função de desconto e exibe o valor retornado formatado com 2 casas decimais
print(f"Desconto: R$ {desconto(tipo, valor):.2f}")

#O PROBLEMA DESTE MÉTODO (POR QUE ESTÁ "ERRADO"?):

#Se a loja criar um cliente 'estudante' ou 'funcionario', a chamada: desconto('estudante', valor) vai falhar e retornar R$ 0.00 até que você Venha AQUI e ABRA esta função para adicionar um novo 'elif'


