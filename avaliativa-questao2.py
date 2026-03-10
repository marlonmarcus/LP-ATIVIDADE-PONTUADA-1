nome = input("Digite um seu nome: ")
sexo = input("Digite seu sexo (Masculino ou Feminino):")
estado_civil = input("Digite seu estado civil: ")


if sexo == "Feminino" and estado_civil == "Casada":
    anos_casado = input("Você tem quantos anos casada?")


print(f"Seu nome é {nome}, seu sexo é {sexo}, seu estado civil é {estado_civil} e você tem {anos_casado}anos de casada.")
