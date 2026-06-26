"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal

"""
#Lista de cédulas multiplicadas por 100 (Ex: 10000 centavos = R$ 100,00; 200 centavos = R$ 2,00)
#Isso serve para fazer os cálculos usando apenas números inteiros e evitar erros de arredondamento.
notas = (10000, 5000, 2000, 1000, 500, 200)

#Lista de moedas também convertidas para centavos inteiros (Ex: 100 centavos = R$ 1,00; 1 centavo = R$ 0,01)
#Facilita o uso do operador de divisão inteira (//) e do resto (%) sem lidar com números quebrados (float).
moedas = (100, 50, 25, 10, 5, 1)


#Exibe uma mensagem no console e captura o valor monetário digitado, convertendo-o para ponto flutuante (float)
N = float(input("Digite uma valor monetário: "))

#Verifica se o valor digitado está fora dos limites permitidos (menor que zero ou maior que um milhão)
if N < 0 or N > 1000000.00:
    print("Incorreto, digite um valor entre 0.00 e 1000000.00")

#Bloco executado caso o valor inserido passe na validação inicial e esteja correto
else:

    #Transforma o valor total em centavos inteiros
    #Multiplica o valor por 100, arredonda com 'round' para evitar erros de precisão do float e converte para número inteiro com 'int'
    centavos = int(round(N * 100))

print("NOTAS:")

#Inicia um laço de repetição que vai percorrer cada valor contido na tupla 'notas'
for n in notas:
        
    #O operador '//' corta as casas decimais e descobre exatamente quantas notas daquele valor (n) cabem inteiras dentro da quantia atual em centavos.
    nota= centavos//n 

    #O operador '%' funciona como uma triagem: ele joga fora o valor que já foi transformado em notas e guarda apenas os centavos "sobrantes" para serem calculados no próximo loop.
    centavos= centavos%n

    print(f"{nota} nota (s) de R$ {n/100:.2f}\n")

print("MOEDAS:")

#Inicia um laço de repetição que vai percorrer cada valor contido na tupla 'moedas'
for m in moedas:

    #Descobre quantas moedas do valor atual cabem no saldo total de centavos.
    #Ex: Se tivermos 75 centavos e a moeda for de 25, a divisão inteira (//) nos dá exatamente 3 moedas.
    moeda= centavos//m

    #"Guarda o troco": Limpa o saldo de centavos, deixando na variável apenas o resto (o que sobrou).
    #Esse valor que sobrou será usado no próximo ciclo do laço para calcular as moedas menores.
    centavos= centavos%m
    
    print(f"{moeda} moeda (s) de R$ {m/100:.2f}\n")
 