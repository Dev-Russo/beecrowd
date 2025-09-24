valor = int(input())

for i in range(valor):
    if valor%(i+1) == 0:
        print(f"{i+1}")