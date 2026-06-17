"""
Utilize um script em linguagem Python com uma função que receba 
três notas de um aluno e que retorne a média dessas 3 notas.

"""

def media_notas(a,b,c):
    soma= a + b + c
    media = soma/3

    return media

nota_1= float(input("Digite a primeira nota: "))
nota_2= float(input("Digite a segunda nota: "))
nota_3= float(input("Digite a terceira nota: "))

media_final= media_notas(nota_1, nota_2, nota_3)

print(f"{media_final:.2f}")

"""
Agora, faça uma função de acordo com a média da função anterior 
e informe o status do aluno de acordo com a tabela a seguir:

"""

def status(media_final):
    if media_final > 6:
        return "Aprovado"
    elif media_final >= 4:
        return "Verificação Suplementar"
    else:
        return "Reprovado"
    
print(f"Status do aluno: {status(media_final)}")
