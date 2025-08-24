codigo1, quantidade1, preco1 = input().split(' ')
quantidade1 = int(quantidade1)
preco1 = float(preco1)

codigo2, quantidade2, preco2 = input().split(' ')
quantidade2 = int(quantidade2)
preco2 = float(preco2)

valor_total = quantidade1 * preco1 + quantidade2 * preco2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")