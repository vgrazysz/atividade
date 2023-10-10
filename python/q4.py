nota_01 = float(input("Digite a primeira nota"))
nota_02 = float(input("Digite a segunda nota"))
media = (nota_01 + nota_02) / 2
if media >= 7:
    print("Aprovado! Sua média é", media)
else:
    print("Reprovado! Sua média é", media)