a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
i = 0

valores = [a, b, c, d, e, f]

for valor in valores:
    if valor >= 0:
        i += 1

print(f"{i} valores positivos")