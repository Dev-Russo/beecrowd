number_cases = int(input())

for _ in range(number_cases):
    n, y = map(int, input().split())
    count = 0
    soma = 0
    
    while count < y:
        if n%2 == 1:
            soma += n
            count += 1
            n += 1
        else:
            n += 1
    print(soma)