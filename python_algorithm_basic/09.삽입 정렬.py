def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
            #print(a)
        a[j+1] = key
    return a

print(insert_sort([2,3,4,5,1,6,8]))