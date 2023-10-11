valor_01 = input("Informe o primeiro valor booleano (True ou False):")
valor_02 = input("Informe o segundo valor booleano (True ou False):")
valor_01 = valor_01.lower() == "true"
valor_02 = valor_02.lower() == "true"
if valor_01 and valor_02:
    print("Os dois valores são VERDADEIROS.")
else:
    print("Um ou dois dos valores são FALSOS.")