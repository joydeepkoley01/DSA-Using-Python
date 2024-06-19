def merge(arr, brr):
    n1 = len(arr)
    n2 = len(brr)
    res = []
    i = 0
    j = 0
    while (i < n1 and j < n2):
        if (arr[i] < brr[j]):
            res.append(arr[i])
            i += 1
        elif (arr[i] > brr[j]):
            res.append(brr[j])
            j += 1

    while (i < n1):
        res.append(arr[i])
        i += 1

    while (j < n2):
        res.append(brr[j])
        j += 1
    print(res)
def merge_sort(array):
    if len(array) <= 1:
        return array  
    middle = len(array) // 2
    left = merge_sort(array[:middle])  
    right = merge_sort(array[middle:]) 

    return merge(left, right)
li2 = [5, 10, 15, 20]
li = [1, 5, 6, 7, 8, 12]
merge(li2, li)
