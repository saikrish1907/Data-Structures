def bin_srch(a, l , u , k):

    if u >= l:
         
        m = (u - 1 + l) // 2

        if a[m] == k:
            return m
        
        elif a[m] > k :
            return bin_srch(a, l , m-1, k)
        
        else:
            return bin_srch(a, m+1, u, k)
        
    else :
         return -1



n = int(input())
ar = list(map(int,input().strip().split()))
k = int(input())

index  = bin_srch(ar, 0 , n-1, k)
print(index+1)
    