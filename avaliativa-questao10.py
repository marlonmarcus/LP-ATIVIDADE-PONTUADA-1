litros = float(input("Quantos litros de combustível deseja? "))
tipo_combustivel = input("Qual tipo de combústivel deseja? (G ou A): ")
valor_gasolina = litros * 6.59
valor_alcool = litros * 3.79

if tipo_combustivel == "A" and litros <=25:
    desconto = valor_alcool - 2 /100
    print(f"Valor total com desconto: R${desconto}")
if tipo_combustivel == "A" and litros >25:
    desconto = valor_alcool - 4 /100
    print(f"Valor total com desconto é: R${desconto}")
if tipo_combustivel == "G" and litros <=25:
    desconto = valor_gasolina - 3 /100
    print(f"Valor total com desconto é R${desconto}")
if tipo_combustivel == "G" and litros >25:
    desconto = valor_gasolina - 5 /100
    print(f"O valor total com desconto é: R${desconto}")