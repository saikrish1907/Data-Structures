#Juggler algorithm

def gcd(n,r):
    while(r):
        n , r = r, n%r

    return n  
        
def left_rot(ar,gc,d):
    n = len(ar)
    d = d % len(ar)
    for i in range(gc):
        t = ar[i]
        j = i
        while 1:
            k = j + d 
            if k >= n:
                k = k - n
            if k == i:
                break
            ar[j] = ar[k]
            j = k
        ar[j] = t
    return ar



def right_rot(ar,gc,d):
    n = len(ar)
    d = d % n
    for i in range(gc):
        t = ar[n-i-1]
        j = n - i - 1
        while 1:
            k = j - d 
            if k < 0:
                k = k + n 
            if k == n-i-1 :
                break

            ar[j] = ar[k]
            j = k
        ar[j] = t
    return ar



n = int(input())
ar = list(map(int, input().strip().split()))
r = int(input())

#find the GCD of the n and rotations r 
gc = gcd(n,r)
#ar1 = left_rot(ar,gc,r)
ar2 = right_rot(ar,gc,r)
#print(ar1)
print(ar2)