def main():
    x = int(input())

    while True:
        z = int(input())
        if z > x:
            break
        
    soma = x
    count = 1
    
    while soma <= z:
        x += 1
        soma += x
        count += 1
        
    print(count)

if __name__ == "__main__":
    main()