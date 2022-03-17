
def selection_sort(ar,n):
    for i in range(n):
         min = i
         for j in range(i+1,n):
             if ar[j] < ar[min]:
                 min = j
         ar[i],ar[min] = ar[min],ar[i]
    
    return ar
            

def bubble_sort(ar,n):
    for i in range(n):
        for j in range(n-i-1):
            if ar[j] > ar[j+1]:
                ar[j],ar[j+1] = ar[j+1],ar[j]
    
    return ar 


n = int(input())
ar = list(map(int, input().strip().split()))

#ar1 = selection_sort(ar,n)
ar1 = bubble_sort(ar,n)

print(ar1)