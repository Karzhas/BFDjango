import math


def power(a, n):
    if n == 0:
        return 1
    result = a
    c = 1
    while c != n:
        result *= a
        c += 1
    return result


l = input().split(' ')
a = float(l[0])
n = int(l[1])
print(power(a, n))
