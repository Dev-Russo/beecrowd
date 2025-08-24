N = int(input())

print(f"{N//365} ano(s)")
N = N%365
print(f"{N//30} mes(es)")
N = N%30
print(f"{N} dia(s)")