h = float(input("Digite a altura em metros:"))
genero = input("Digite o genero (M para masculino ou F para feminino):")
if genero.upper() == "M":
    peso_ideal = (72.7 * h) - 58
    print(f"O peso ideal para um homem com altura {h} metros é {peso_ideal:.2f} kg.")
elif genero.upper() == "F":
    peso_ideal = (62.1 * h) - 44.7
    print(f"O peso ideal para uma mulher com altura {h} metros é {peso_ideal:.2f} kg.")
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")
