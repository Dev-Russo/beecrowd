while True:
    sequence = int(input())
    
    if sequence == 0:
        break
    for i in range(sequence):
        if sequence == i + 1:
            print(i+1)
        else:
            print(i+1, end=" ")