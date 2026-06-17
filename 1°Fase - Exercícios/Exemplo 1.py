vendas_mes= float(input("Qual é valor total das suas vendas do mês? "))
anos_empresa= int(input("Quantos anos de empresa você está? "))
categoria= input("Qual a sua categoria(A,B ou C)? ").upper()

if categoria == "A":
    if anos_empresa > 5:
        bonus_base= (110/100)*vendas_mes
        antiguidade= 500.00
        valor_total= bonus_base + antiguidade
        print(f"O seu bônus base é R${bonus_base:.2f}, e seu bônus de antiguidade é R${antiguidade}, dando um valor total de R${valor_total:.2f}")

    elif anos_empresa < 5 and anos_empresa > 2:
        bonus_base= (110/100)*vendas_mes
        antiguidade= 200.00
        valor_total= bonus_base + antiguidade
        print(f"O seu bônus base é R${bonus_base:.2f}, e seu bônus de antiguidade é R${antiguidade}, dando um valor total de R${valor_total:.2f}")

    else:
        bonus_base= (110/100)*vendas_mes
        print(f"O seu bônus base é R${bonus_base:.2f}")

if categoria == "B":
    if anos_empresa > 5:
        bonus_base= (107/100)*vendas_mes
        antiguidade= 500.00
        valor_total= bonus_base + antiguidade
        print(f"O seu bônus base é R${bonus_base:.2f}, e seu bônus de antiguidade é R${antiguidade}, dando um valor total de R${valor_total:.2f}")
        
    elif anos_empresa < 5 and anos_empresa > 2:
        bonus_base= (107/100)*vendas_mes
        antiguidade= 200.00
        valor_total= bonus_base + antiguidade
        print(f"O seu bônus base é R${bonus_base:.2f}, e seu bônus de antiguidade é R${antiguidade}, dando um valor total de R${valor_total:.2f}")

    else:
        bonus_base= (107/100)*vendas_mes
        print(f"O seu bônus base é R${bonus_base:.2f}")

if categoria == "C":
    if anos_empresa > 5:
        bonus_base= (105/100)*vendas_mes
        antiguidade= 500.00
        valor_total= bonus_base + antiguidade
        print(f"O seu bônus base é R${bonus_base:.2f}, e seu bônus de antiguidade é R${antiguidade}, dando um valor total de R${valor_total:.2f}")
        
    elif anos_empresa < 5 and anos_empresa > 2:
        bonus_base= (105/100)*vendas_mes
        antiguidade= 200.00
        valor_total= bonus_base + antiguidade
        print(f"O seu bônus base é R${bonus_base:.2f}, e seu bônus de antiguidade é R${antiguidade}, dando um valor total de R${valor_total:.2f}")

    else:
        bonus_base= (105/100)*vendas_mes
        print(f"O seu bônus base é R${bonus_base:.2f}")
    

