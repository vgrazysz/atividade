media_01 = float(input("Digite a primeira média"))
media_02 = float(input("Digite a segunda média"))
aprovado = 7
reprovado = 3
media = (media_01 + media_02) / 2
if media >= 7:
    resultado = "Aprovado!"
elif media < 3:
    resultado = "Reprovado!"
else:
    resultado = "Prova Final"
print(f"Média final: {media:.2f}")
print(f"Resultado: {resultado}")