nome_produto = input("Qual o nome do produto? ")
quantidade_produto = int(input("Qual a quantidade do produto? "))
preço_produto = int(input("Qual o preço do produto? "))
total = quantidade_produto * preço_produto

if quantidade_produto <= 5:
    print("Você recebeu um desconto de 2%")
    desconto = total * 2/100
    total_pagar = total - desconto
    print(f"Total a pagar: {total_pagar}")
if quantidade_produto > 5 and quantidade_produto <= 10:
    print("Você recebeu um desconto de 3%")
    desconto = total * 3/100
    total_pagar = total - desconto
    print(f"Total a pagar: {total_pagar}")
if quantidade_produto >10:
    print("Você recebeu 5% de desconto")
    desconto = total * 5/100
    total_pagar = total - desconto

    print(f"Total a pagar: {total_pagar}")
