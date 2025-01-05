arquivo_numeros = open("media.txt", "r")
soma = 0.0
quant_numeros = 0

for num in arquivo_numeros:
    num = float(num)
    soma+= num
    quant_numeros+= 1

arquivo_numeros.close()

Media = soma/quant_numeros
print(Media)

