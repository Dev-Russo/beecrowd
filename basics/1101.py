def getIntervalValuesAndSum(min, max):
    soma = []
    for i in range(min, max + 1):
        soma.append(i)
        
    soma_todos = sum(soma)
    
    print(" ".join(map(str, soma)) + " Sum=" + str(soma_todos))

def main():
    while True:
        m, n = map(int, input().split(" "))
        if m <= 0 or n <= 0: break
        getIntervalValuesAndSum(min(m,n), max(m,n))
        
if __name__ == "__main__":
    main() 