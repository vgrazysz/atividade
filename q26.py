p = float(input("Informe o peso em quilogramas: "))
h = float(input("Informe a altura em metros: "))
imc = p / (h ** 2)
if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "Peso normal"
elif 25 <= imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"
print(f"O IMC é {imc:.2f}, o que indica: {condicao}.")