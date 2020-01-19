n = input()
arr = input()
l = list(map(int,arr.split(' ')))
c = 0
for i in range(1,int(n)-1):
    if l[i-1] < l[i] and l[i+1] < l[i]:
        c += 1
print(c)