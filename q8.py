bruto = float(input("Digite o salário bruto: "))
if bruto < 2000:
    descontin = 10
else:
    descontin = 20
desconto = (descontin / 100) * bruto
liquido = bruto - descontin
print(f"Salário líquido: R$ {liquido:.2f}")