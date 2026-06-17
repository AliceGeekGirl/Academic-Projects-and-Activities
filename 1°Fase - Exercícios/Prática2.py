velocidade_max= 9
velocidade_motorista= float(input("Sua velocidade foi (Km/h): "))

if velocidade_motorista == 10:
    print("A sua multa é Leve e vai receber 3 pontos na sua carteira")
    print("O valor da sua multa é R$85,13")
elif 11 <= velocidade_motorista <= 30:
    print("A sua multa é Média e vai receber 5 pontos na sua carteira")
    print("O valor da sua multa é R$127,69")
elif velocidade_motorista >= 31:
    print("A sua multa é Gravíssima e vai receber 7 pontos na sua carteira")
    print("O valor da sua multa é R$574,62")
else:
    print("Velocidade normal")
