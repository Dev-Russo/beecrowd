import math

x = 1
N = int(input())

while x <= N:
    x += 1
    if x%2 == 0:
        resultado = int(math.pow(x, 2))
        print(f"{x}^2 = {resultado}")