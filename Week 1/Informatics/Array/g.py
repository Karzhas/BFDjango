n = int(input())
l = list(map(int, input().split(' ')))
for i in range(0, int(n/2)):
    l[i] , l[n-1-i] = l[n-1-i], l[i]
for i in l:
    print(i, end=" ")