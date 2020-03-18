def selection_sort(a):
    for i in range(0, len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] #python은 그냥 된다 swap

ls = [1,5,8,3,5,7,3]
selection_sort(ls)
print(ls)