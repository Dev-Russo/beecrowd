def getMoney():
    money = float(input())
    return money

def taxas(money):
    devido = 0
    if money > 4500:
        devido += (money - 4500) * 0.28
        money = 4500
    if money > 3000:
        devido += (money - 3000) * 0.18
        money = 3000
    if money > 2000:
        devido += (money - 2000) * 0.08

    return devido

def main():
        value = getMoney()
        total = taxas(value)
        if total == 0:
            print("Isento")
        else:
            print(f"R$ {total:.2f}")
        
if __name__ == "__main__":
    main()