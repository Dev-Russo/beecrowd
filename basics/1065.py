a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

valores = [a, b, c, d, e]

pares = 0

for valor in valores:
    if valor%2 == 0:
        pares += 1

print(f"{pares} valores pares")