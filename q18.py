nome = input("Informe o nome:")
sexo = input("Informe o sexo (M para masculino, F para feminino ou X para outro):")
estado_civil = input("Digite o estado civil (solteira, casada, viúva, namorando): ")
if sexo.upper() == "F" and estado_civil.upper() == "casada":
    tempo_casada = int(input("Informe o tempo de casamento em anos:"))
    print(f"{nome} está casada há {tempo_casada} anos.")
else:
    print(f"{nome} não está casada.")