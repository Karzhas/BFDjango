import math

a = int(input())
b = 0
for i in range(1, int(math.sqrt(a)) + 1):
    if a % i == 0:
        b += 2
        if i == a / i:
            b -= 1

print(b)
