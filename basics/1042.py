v = [int(x) for x in input().split(" ")]
V = v[:]

V.sort()

for i in range(3):
    print(V[i])
print()
for i in range(3):
    print(v[i])