print("__"*20)
positivo = 0
cont = 0
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0


while True:
    posi = int(input(f"Digite o {cont+1} número inteiro ou (digite -1 para sair):\n "))

    if posi == -1:
        break

    cont+=1

    if posi >= 0 and posi <=25:
        intervalo1 += 1
    elif posi >=26 and posi <=50:
        intervalo2 += 1
    elif posi >=51 and posi <=75:
        intervalo3 += 1
    elif posi >= 76 and posi <=100:
        intervalo4 += 1

print("__"*20)
print("         Resultado    ")
print("__"*20)
print(f"dentro do 1º intervalo (0-25) foi: {intervalo1}")
print(f"dentro do 1º intervalo (26-50) foi: {intervalo2}")
print(f"dentro do 1º intervalo (51-75) foi: {intervalo3}")
print(f"dentro do 1º intervalo (76-100) foi: {intervalo4}")
print("__"*20)
