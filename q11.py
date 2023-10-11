lado_01 = float(input("Digite o comprimento do lado 1:"))
lado_02 = float(input("Digite o comprimento do lado 2:"))
lado_03 = float(input("Digite o comprimento do lado 3:"))
if lado_01 == lado_02 == lado_03:
    tipo = "Equilátero"
elif lado_01 == lado_02 or lado_01 == lado_03 or lado_02 == lado_03:
    tipo = "Isósceles"
else:
    tipo = "Escaleno"
print(f"O seu triângulo é do tipo: {tipo}")