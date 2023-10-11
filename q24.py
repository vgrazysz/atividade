g = int(input("Informe o primeiro valor inteiro:"))
r = int(input("Informe o segundo valor inteiro:"))
a = int(input("Informe o terceiro valor inteiro:"))
maior = max(g, r, a)
menor = min(g, r, a)
meio = (g + r + a) - maior - menor
print("Valores em ordem decrescente:", maior, meio, menor)
