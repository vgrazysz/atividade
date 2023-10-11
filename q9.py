comprinha = float(input("Informe o valor da compra: "))
if comprinha < 200:
    lucrozin = 50
else:
    lucrozin = 30
lucro = (lucrozin / 100) * comprinha
venda = comprinha + lucro
print(f"Valor de venda: R$ {venda:.2f}")