n1 = float(input("Digite o seu primeiro número:"))
n2 = float (input("Digite o seu segundo número:"))
n3 = float (input("Digite o seu terceiro número"))
if n1 == n2 == n3: 
    print("Números iguais.")
else: 
    nm = max (n1, n2, n3)
    print (f"O maior número entre os três números dados é: {nm}")