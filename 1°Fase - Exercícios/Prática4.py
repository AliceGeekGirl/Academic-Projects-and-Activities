a= int(input("Insira um valor: "))
b= int(input("Insira outro valor: "))

print("Antes da troca")
print(f"a:{a}, b:{b}")

a, b= b, a

print("Depois da troca")
print(f"a:{a}, b:{b}")
