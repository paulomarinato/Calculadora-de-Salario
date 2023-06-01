valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
print("Imposto de Renda (11%): R$ {:.2f}".format(imposto_renda))
print("INSS (8%): R$ {:.2f}".format(inss))
print("Sindicato (5%): R$ {:.2f}".format(sindicato))
print("Salário Líquido: R$ {:.2f}".format(salario_liquido))

