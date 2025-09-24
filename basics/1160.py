cases = int(input())
count = 0

while count <  cases:
    pa, pb, ga, gb =  map(float, input().split())
    years = 0
    
    while pa <= pb:
        anual_growtha = int(pa * ga/100)
        pa += anual_growtha
        anual_growthb = int(pb * gb/100)
        pb += anual_growthb
        years += 1
        if years >  100:
            print(f"Mais de 1 seculo.")
            break

    if years <= 100:
        print(f"{years} anos.")
        
    count += 1