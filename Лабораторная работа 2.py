# -- coding: utf-8 --
def IsPrime(r):
    for y in range(2, int(r ** 0.5) + 1):
        if r % y == 0:
            print("NO")
            return
    print("YES")
o = int(input())
IsPrime(o)