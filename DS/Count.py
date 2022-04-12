def count(n):

    if n > 0:
        print(n)
        count(n-1)
        

n = 10
count(n) 