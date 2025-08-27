number_case = int(input())
x = 0
resultado = []

while x < number_case:
    a, b, c = [float(x) for x in input().split(" ")]
    resultado.append((a*2+b*3+c*5)/10)
    x += 1

for valor in resultado:
    print(f"{valor:.1f}")