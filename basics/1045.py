A, B, C = [float(x) for x in input().split(" ")]

if (A >= (B + C)):
    print("NAO FORMA TRIANGULO")
    if((A*A) == ((B*B) + (C*C))):
        print("TRIANGULO RETANGULO")
    if((A*A) > ((B*B) + (C*C))):
        print("TRIANGULO OBTUSANGULO")
    if((A*A) < ((B*B) + (C*C))):
        print("TRIANGULO ACTUANGULO")
    if(A == B == C):
        print("TRIANGULO EQUILATERO")
    if(A == C or A == B or B == C):
        print("TRIANGULO ISOSCELES")