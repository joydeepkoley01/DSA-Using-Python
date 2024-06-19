def insertion_sort(li):
    n=len(li);
    for i in range(1,n):
        j=i
        while j>=1 and li[j]<li[j-1]:
            (li[j],li[j-1])=(li[j-1],li[j])
            j-=1

my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array is:", my_list)