def main():
    n = int(input())
   
    for i in range(n+1):
        if i > 0: 
            print(f"{i} {i*i} {i*i*i}")
            print(f"{i} {i*i+1} {i*i*i+1}")

if __name__ == "__main__":
    main()
