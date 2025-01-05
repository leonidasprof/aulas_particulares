nota = 0
cont = 0
soma = 0

while True:
    nota = float(input("Digite a nota:"))
    if nota == -1:
        break
    soma += nota

    cont += 1

media = soma / cont 
print(f"A média é: {media:.2f}")