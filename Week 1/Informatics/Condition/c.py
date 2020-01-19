a = int(input())
b = int(input())
if a % 10 == a / 1000 and a / 10 % 10 == a / 100 % 10 and b == 1:
    print("YES")
else:
    print("NO")
