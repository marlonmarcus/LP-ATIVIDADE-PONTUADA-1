valorA = int(input("Digite um número: "))
valorB = int(input("Digite outro número: "))
operadores = input("Digite qual operador deseja usar(+ - * /):")
soma = valorA + valorB
subtracao = valorA - valorB
multiplicacao = valorA * valorB
divisao = valorA / valorB

match operadores:
    case "+":
        print(f"A soma dos números é {soma}")
    case "-":
        print(f"A subtração dos números é {subtracao}")
    case "*":
        print(f"A multiplicação dos números é {multiplicacao}")
    case "/":
        print(f"A divisão dos números é {divisao}")
    case _: print("operador inválido.")