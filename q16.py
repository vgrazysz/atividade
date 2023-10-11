compra = int(input("Informe o valor da compra: "))
pagamento = int(input("Informe o valor do pagamento: "))
if pagamento < compra:
    print("Negado.")
else:
    troco = pagamento - compra
    notas_100 = troco // 100
    troco %= 100
    notas_10 = troco // 10
    troco %= 10
    notas_1 = troco
    print("Troco =", pagamento - compra)
    print("Notas de R$ 100:", notas_100)
    print("Notas de R$ 10:", notas_10)
    print("Notas de R$ 1:", notas_1)