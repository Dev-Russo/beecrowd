def main():
    fib = [0, 1]
    for i in range(2, 61):
        fib.append(fib[i-1] + fib[i-2])
    
    t = int(input()) 
    
    for _ in range(t):
        n = int(input())
        print(f"Fib({n}) = {fib[n]}")

if __name__ == "__main__":
    main()
