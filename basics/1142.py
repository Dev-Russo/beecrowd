def linhas_pum(number):
    if number == 1:
        return print("1 2 3 PUM")
    else:
        linhas_pum(number-1)
        a = 4*number
        print(f"{a-3} {a-2} {a-1} PUM")
        

def main():
    numero = int(input())
    linhas_pum(numero)

if __name__ == "__main__":
    main()
