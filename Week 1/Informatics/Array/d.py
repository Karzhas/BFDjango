n = input()
arr = input().split()
c = 0
for i in range(1, int(n)):
    if int(arr[i]) > int(arr[i - 1]):
        c += 1
print(c)
