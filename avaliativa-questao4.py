morango = int(input("Digite quantos kilos de morango deseja comprar: "))
macas = int(input("Digite quantos kilos de maçãs deseja comprar: "))
frutas_total = morango + macas
kg_morango = 2.50 * morango
kg_macas = 1.80 * macas
valor_total = kg_macas + kg_morango
desconto = valor_total - valor_total * 10 / 100

kg_morango = 2.50 * morango
kg_macas = 1.80 * macas
valor_total = kg_macas + kg_morango

print(f"Você vai pagar R${valor_total}")

if valor_total > 15 or frutas_total >=10:
    print("Você recebeu um desconto de 10%")
    print(f"Você comprou {morango}KG de morango e {macas}KG de maçãs e você vai pagar R${desconto}")
    
else: print(f"Você comprou {morango}KG de morango e {macas}KG de maçãs e você vai pagar R${valor_total}")