import math

A, B, C = [float(x) for x in input().split(' ')]

delta = ((B*B) - (4*A*C))

if(A != 0 and delta > -1):
    r1 = (-B + math.sqrt(delta))/(2*A)
    r2 = (-B - math.sqrt(delta))/(2*A)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
else:
    print("Impossivel calcular")