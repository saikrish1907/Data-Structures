def mergesort(ar):
    if len(ar) > 1:

        m =  len(ar) // 2

        l = ar[m:]
        r = ar[:m]

        mergesort(l)
        mergesort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                ar[k] = r[j]
                j += 1
            else :
                ar[k] = l[i]
                i += 1
            k += 1 

        while i < len(l):
            ar[k] = l[i]
            i += 1 
            k += 1  
        
        while j < len(r):
            ar[k] = r[j]
            j += 1 
            k += 1  

    return ar 






ar = list(map(int, input().strip().split()))


ar1 = mergesort(ar)
print(ar1)