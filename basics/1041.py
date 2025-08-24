ponto = [float(x) for x in input().split(" ")]

if(ponto[0] > 0 and ponto[1] > 0):
    print("Q1")
elif(ponto[0] < 0 and ponto[1] > 0):
    print("Q2")
elif(ponto[0] < 0 and ponto[1] < 0):
    print("Q3")
elif(ponto[0] > 0 and ponto[1] < 0):
    print("Q4")
elif(ponto[0] == 0 and ponto[1] == 0):
    print("Origem")
elif(ponto[0] == 0):
    print("Eixo Y")
elif(ponto[1] == 0):
    print("Eixo X")
