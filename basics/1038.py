codigo, qtd = [int(x) for x in input().split(" ")]
precos = [4, 4.5, 5, 2, 1.5]

print(f"Total: R$ {qtd * precos[codigo-1]:.2f}")