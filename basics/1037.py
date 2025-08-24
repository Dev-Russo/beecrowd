val = float(input())

if(val >= 0 and val <= 25):
    print(f"Intervalo [0,25]")
elif(val > 25 and val <= 50):
    print(f"Intervalo (25,50]")
elif(val > 50 and val <= 75):
    print(f"Intervalo (50,75]")
elif(val > 75 and val <= 100):
    print(f"Intervalo (75,100]")
else:
    print("Fora de intervalo")