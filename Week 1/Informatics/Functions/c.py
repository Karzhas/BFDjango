def xor(a,b):
    if a == 1 and b == 0 or (a == 0 and b == 1):
        return True
    else:
        return False


l = list(map(int, input().split(' ')))
if xor(l[0],l[1]):
    print("1")
else:
    print("0")
