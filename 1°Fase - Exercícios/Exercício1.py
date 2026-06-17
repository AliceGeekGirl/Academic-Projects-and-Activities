a = int(input("Digite um numero QUALQUER: "))
b = int(input("Digite um numero DIFERENTE de 0 (Zero): "))
c= (a/b)
 
try:
  print("%.3f" % c)
except ZeroDivisionError:
  print ("Divisão por zero - invalida!")
