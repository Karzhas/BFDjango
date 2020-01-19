n = int(input())
arr = input()
l = list(map(int, arr.split(' ')))
for i in l:
    if i%2==0:
        print(i,end=" ")