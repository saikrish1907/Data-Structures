def heapify(ar,n,i):
    large = i
    left  = 2 * i + 1
    right = 2 * i + 2 

    if left < n and ar[large] < ar[left]:
        large = left 

    if right < n and ar[large] < ar[right]:
        large = right 

    if large != i :
        ar[i],ar[large] = ar[large], ar[i]
        #unbalance takes place now heapify again passing large 
        heapify(ar,n,large)




def heapsort(ar):
    #process of heapufy starts -  max heap is used here 
    n = len(ar)

    #N//2 - 1 iteration is enough for N elements - Take an example and work it out.
    for i in range(n//2 - 1 , -1 , -1):
        heapify(ar,n,i)
    

    #swap the first element with the last element and remove the first element from heap
    for i in range(n-1, 0 , -1):
        ar[i],ar[0] = ar[0],ar[i]
        #heapify again to for max heap of the unbalanced heap tree
        heapify(ar,i,0) 
    
    return ar 



ar = list(map(int, input().strip().split()))
ar1 = heapsort(ar)

print(ar1)
