numb_int = int(input())
x = dentro = fora = 0

while x < numb_int:
    valor = int(input())
    if valor >= 10 and valor <= 20:
        dentro += 1
    else:
        fora += 1
    x += 1

print(f"{dentro} in")
print(f"{fora} out")