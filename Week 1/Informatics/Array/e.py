import math

n = input()
arr = input()
l = list(map(int, arr.split(' ')))
l.append(l[int(n)-1] * (-1))
b = False
for i in range(1, int(n)):
    if l[i] > 0 and l[i + 1] > 0 or (l[i] > 0 and l[i - 1] > 0) or (l[i] < 0 and l[i + 1] < 0) or (
            l[i] < 0 and l[i - 1] < 0):
        b = True

if b:
    print("YES")
else:
    print("NO")
