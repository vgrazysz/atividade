percurso = float(input("Digite o percurso em km:"))
carro = input("Digite o tipo de carro (a, b ou c):")
consumo_a = 8
consumo_b = 9
consumo_c = 12
if carro == "a":
    consumo = percurso / consumo_a
elif carro == "b":
    consumo = percurso / consumo_b
elif carro == "c":
    consumo = percurso / consumo_c
else:
    print("Tipo de carro inválido.")
    consumo = None
if consumo is not None:
    print(f"Consumo: {consumo:.2f} L")