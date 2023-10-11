ni = int(input("Informe o número de identificação do aluno: "))
nota_01 = float(input("Informe a nota da primeira verificação: "))
nota_02 = float(input("Informe a nota da segunda verificação: "))
nota_03 = float(input("Informe a nota da terceira verificação: "))
exercicios = float(input("Informe a média dos exercícios: "))
aproveitamento = (nota_01 + nota_02 * 2 + nota_03 * 3 + exercicios) / 7
if aproveitamento >= 90:
    conceito = "A"
elif aproveitamento >= 75:
    conceito = "B"
elif aproveitamento >= 60:
    conceito = "C"
elif aproveitamento >= 40:
    conceito = "D"
else:
    conceito = "E"
if conceito in ["A", "B", "C"]:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"
print(f"Número de identificação: {ni}")
print(f"Notas: {nota_01}, {nota_02}, {nota_03}")
print(f"Média dos exercícios: {exercicios}")
print(f"Média de aproveitamento: {aproveitamento:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")