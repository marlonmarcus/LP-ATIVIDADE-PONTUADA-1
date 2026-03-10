cd = input("Digite o cd que você quer em cores (verde azul amarelo vermelho): ")

match cd:
    case "verde":
        print("O preço desse CD é R$10,00")
    case "azul":
        print("O preço desse CD é R$20,00")
    case "amarelo":
        print("O preço desse CD é R$30,00")
    case "vermelho":
        print("O preço desse CD é R$40,00")
    case _:
        print("OPÇÃO INVÁLIDA.")