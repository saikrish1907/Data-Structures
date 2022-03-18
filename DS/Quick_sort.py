def quicksort(l,u,ar):
    if l < u:
        p = partition(l,u,ar)
        quicksort(l,p-1,ar)
        quicksort(p+1,u,ar)
    
    return ar


def partition(l,u,ar):
    i = l - 1 
    piv = ar[u]
    j = l
    while j <= u-1 :
        if ar[j] <= piv:
            i += 1 
            ar[i],ar[j] = ar[j],ar[i]
        
        j += 1
    ar[i+1],ar[u] = ar[u],ar[i+1]

    return i+1



ar = list(map(int, input().strip().split()))

ar1 = quicksort(0,len(ar)-1, ar)
print(ar1)