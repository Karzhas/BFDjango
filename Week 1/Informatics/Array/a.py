n = int(input())
arr = input()
l = list(map(int, arr.split(' ')))
for i in range(0, n, 2):
    print(l[i], end=" ")
