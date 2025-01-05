carros = []
consumos = []
list0 = list()
menor_consumo = 0
valor_gasolina = 5.59
i = 1
km_viagem = 1000

for i in range(5):
    print("--"*15)
    print("       Digite 5 modelos")
    print("--" * 15)
    modelos = input(f"Digite o {i+1}º modelo:\n ")
    consumo = float(input(f"Quantos km o {i+1}º carro faz com 1litro?\n "))
    carros.append(modelos)
    consumos.append(consumo)

print("--" * 15)
print("           RESULTADOS")
print(f"O modelo mais econÔmico é {carros[i]} ele faz {max(consumos)}km com 1litro.")
print(f"Para percorrer 1000km o modelo: {carros[1]} gastará R${km_viagem/consmu[1]*valor_gasolina} para percorrer 1000km. ")
print(f"Para percorrer 1000km o modelo: {carros[2]} gastará R${km_viagem/consmu[2]*valor_gasolina} para percorrer 1000km. ")
print(f"Para percorrer 1000km o modelo: {carros[3]} gastará R${km_viagem/consmu[3]*valor_gasolina} para percorrer 1000km. ")
print(f"Para percorrer 1000km o modelo: {carros[4]} gastará R${km_viagem/consmu[4]*valor_gasolina} para percorrer 1000km. ")
print(f"Para percorrer 1000km o modelo: {carros[5]} gastará R${km_viagem/consmu[5]*valor_gasolina} para percorrer 1000km. ")
print("--" * 15)