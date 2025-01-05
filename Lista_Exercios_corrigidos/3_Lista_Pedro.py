def somaImposto(a, b, c):
    return taxa*custo+venda



venda = float(input(f"Digite o valor do produto:"))
custo = float(input(f"Digite o percentual do imposto ex.: "))
taxa = venda*custo
novo_valor = somaImposto(taxa, custo, venda)

print(f"O produto custa R${venda}")
print(f"O imposto é: {custo:.2f}%")
print(f"O valor + imposto é = R${novo_valor}")

