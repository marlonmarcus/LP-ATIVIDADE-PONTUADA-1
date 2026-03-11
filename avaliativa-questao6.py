primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media >= 6:
    print("PARABÉNS, VOCÊ ESTÁ APROVADO.")
elif media <6 or media == 4:
    print("VOCÊ ESTÁ EM RECUPERAÇÃO.")
else: 
    print("VOCÊ ESTÁ REPROVADO.")
