def verifica_ordem(x, y):
    if x < y:
        print("Crescente")
    elif x > y:
        print("Decrescente")

while True:
    x, y = map(int, input().split())
    if x == y:
        break
    verifica_ordem(x, y)