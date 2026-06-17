"""
 Um novo modelo de carro, super econômico foi lançado. Ele faz 20 km com 1 litro de 
combustível. Cada litro de combustível custa R$ 4,95.
 Faça um Script em linguagem Python que pergunte ao usuário quanto de dinheiro ele 
pretende usar e em seguida o programa informa quantos litros de combustível ele pode 
comprar e quantos quilômetros o carro consegue rodar com esta quantidade de 
combustível.

"""
dinheiro_disponivel = float(input("Olá! Quanto de dinheiro você pretende usar para abastecer? R$ "))

quilometros_por_litro = 20
custo_por_litro = 4.95

litros_comprados = dinheiro_disponivel / custo_por_litro
distancia_km = litros_comprados * quilometros_por_litro

print(f"Com R$ {dinheiro_disponivel:.2f} você pode comprar {litros_comprados:.2f} litros de combustível.")
print(f"Com essa quantidade de litros, seu carro pode rodar aproximadamente {distancia_km:.2f} km.")


