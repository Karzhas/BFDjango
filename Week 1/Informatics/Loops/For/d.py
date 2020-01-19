import math
b = False
a = int(input())
for i in range(2,int(math.sqrt(a)+1)):
    if a % i == 0:
        print(i)
        b = True
        break
if not b:
    print(a)