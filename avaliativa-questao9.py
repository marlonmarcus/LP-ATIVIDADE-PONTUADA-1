renda_mensal = float(input("Digite sua renda mensal: R$"))
emprestimo = float(input("Digite o valor do empréstimo que deseja: R$"))
num_parcelas = int(input("Digite o número de parcelas que deseja pagar: "))

parcelas = emprestimo / num_parcelas

if emprestimo <= renda_mensal *10 and parcelas <= renda_mensal *0.30:
    print("O empréstimo pode ser feito.")
else: 
    print("Empréstimo não pode ser feito.")