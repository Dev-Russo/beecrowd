def getNumbersLeftTwo(number):
    for i in range(1, 10000):
        if i%number == 2:
            print(i)
                
def main():
    x = int(input())
    getNumbersLeftTwo(x)
    
if __name__ == "__main__":
    main()