salario = float(input("Digite o seu salario bruto, para o desconto do imposto de renda R$"))

if salario < 1903.98 :
    imposto = 0
if salario > 1903.99 and salario < 2826.65:
    imposto = 7.5
if salario > 2826.66 and salario < 3751.05:
    imposto = 15
if salario > 3751.6 and salario < 4664.68:
    imposto = 22.5
if salario >  4664.68:
    imposto = 27.5

salario_liquido = salario - (salario * (imposto / 100))

print(salario_liquido)