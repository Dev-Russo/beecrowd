def isprime(valor):
    if valor <= 1:
        return False
    for i in range(2, int(valor**0.5) + 1):
        if valor%i == 0:
            return False
    return True

count = 0
cases = int(input())

while count < cases:
    valor = int(input())
    if isprime(valor):
        print(f"{valor} eh primo")
    else:
        print(f"{valor} nao eh primo")
    
    count += 1