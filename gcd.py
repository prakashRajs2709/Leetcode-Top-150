from math import gcd
def gcdoftwonumbers(n):
    a=[0]*n
    a[0]=1
    a[1]=2
    for i in range(1,n):
        a[0] = a[0] + (2*i+1)
        a[1] = a[1] + (2*i+2)
    
    return gcd(a[0],a[1])





print(gcdoftwonumbers(4))