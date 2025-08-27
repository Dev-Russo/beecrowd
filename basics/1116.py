DIV_POR_ZERO = "divisao impossivel"

def divisao_prim_seg(n1, n2):
    if n2 != 0:
        return n1/n2
    else:
        return DIV_POR_ZERO
    
def main():
    case = int(input())
    for _ in range(case):
        n1, n2 = map(int, input().split(" "))
        resultado = divisao_prim_seg(n1, n2)
        print(f"{resultado:.1f}")
        x += 1

if __name__ == "__main__":
    main()