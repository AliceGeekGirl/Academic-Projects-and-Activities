import math

raio= float(input("Insira o valor do raio (cm): "))

if raio <= 0:
    print("Erro: valores negativos não são permitidos, insira um valor positivo")

else:
    area= (math.pi*raio**2)
    print(f"A área do círculo de raio {raio:.2f}cm é {area:.2f}cm²")


