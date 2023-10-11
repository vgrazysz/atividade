etiqueta = float(input("Informe o preço normal de etiqueta do produto: R$"))
condicao = int(input("Informe o código da condição de pagamento (1, 2, 3 ou 4):"))
if condicao == 1:
    valor_pago = etiqueta - (0.10 * etiqueta)
elif condicao == 2:
    valor_pago = etiqueta - (0.15 * etiqueta)
elif condicao == 3:
    valor_pago = etiqueta
elif condicao == 4:
    valor_pago = etiqueta + (0.10 * etiqueta)
else:
    print("Código de condição de pagamento inválido.")
    valor_pago = None
if valor_pago is not None:
    print(f"O valor a ser pago é: R$ {valor_pago:.2f}")