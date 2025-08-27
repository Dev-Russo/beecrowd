a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())


valores = [a, b, c, d, e]

##pares impares positivos e negativos
pares = 0
impares = 0
negativos = 0
positivos = 0


for valor in valores:
    if valor > 0:
        positivos += 1
    if valor < 0:
        negativos += 1
    if valor%2 == 0:
        pares += 1
    if valor%2 != 0:
        impares += 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")