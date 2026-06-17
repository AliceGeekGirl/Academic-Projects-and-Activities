i= 0 #iterador
soma= 0
media= 0
contador= 0 #Acumulador
maior= 0
menor = 1000000000000000
numPositivo= []

while i != -1:
    numero= int(input("Digite um número, mas se quiser sair digite -1: "))
    if numero > 0 and numero != -1:
        soma= soma + numero
        contador +=1
        media= soma/contador
        if maior < numero:
            maior=numero                  
        if menor > numero:
            menor=numero
        numPositivo.append(numero)
        
    else:
        i= -1


print(f"A soma de todos os números inseridos é {soma}")
print(f"A média dos números inseridos é {media:.2f}")
print(f"O maior número inserido é {maior}")
print(f"O menor número inserido é {menor}")
print(numPositivo)
        
