ini, term = [int(x) for x in input().split(" ")]

if(ini > term):
    print(f"O JOGO DUROU {24 - ini + term} HORA(S)")
elif(ini < term):
    print(f"O JOGO DUROU {term - ini} HORA(S)")
else:
    print(f"O JOGO DUROU 24 HORA(S)")