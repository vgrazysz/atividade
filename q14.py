municipio = (input("Informe seu município: "))
eleitores = int(input("Digite a quantidade de eleitores: "))
mais_votado = int(input("Digite o número de votos do candidato mais votado: "))
if eleitores > 200000 and mais_votado < (0.5 * eleitores):
    print(f"No município de {municipio} haverá segundo turno.")
else:
    print(f"No município de {municipio} não haverá segundo.")