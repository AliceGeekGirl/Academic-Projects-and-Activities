ganho_hora= float(input("Quanto você ganha por hora: R$ "))
horas_trabalhadas= float(input("O número de horas trabalhadas no mês de setembro: "))

salario_total= ganho_hora*(horas_trabalhadas*30)

print(f"O total do salário no setembro é R${salario_total:,.2f}")
