"""
Construa um script em linguagem Python que utilize um dicionário 
cujas chaves são os códigos do produto e os valores são o nome do 
produto, o preço unitário e a quantidade comprada. A partir do 
dicionário, o programa deve imprimir os itens da compra e calcular o 
subtotal de cada um deles, ou seja, quantidade * preço unitário. Por fim, 
o Script deve apresentar o valor total da compra

"""
produtos= {
    100: ("Arroz", 29.99, 2),
    102: ("Feijão", 25.00, 3),
    103: ("Frango", 20.00, 2),
    104: ("Macarrão", 15.90, 4)
}

valor_total= 0

print("Itens da Compra:", end="\n\n")

for codigo, dados_produto in produtos.items():
    nome= dados_produto[0]
    preco_uni= dados_produto[1]
    quantidade= dados_produto[2]

    subtotal= preco_uni*quantidade
    valor_total += subtotal
    print(f"Código: {codigo} | Produto: {dados_produto[0]} | Preço Unitário: {preco_uni} | Subtotal: R$ {subtotal:.2f}", end="\n\n")

print(f"Valor total da compra: {valor_total:.2f}")


