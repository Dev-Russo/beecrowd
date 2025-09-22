n = int(input())

fib_sequence = []
a, b = 0, 1

for _ in range(n):
    fib_sequence.append(a)

    a, b = b, a + b

output_list = [str(num) for num in fib_sequence]

output_string = " ".join(output_list)

print(output_string)