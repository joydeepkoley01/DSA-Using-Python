li=[6,5,4,3,2,1,80]
n=len(li)

for i in range(0,n):
    mindx=i
    # select the minimum element in every iteration
    for j in range(i+1,n):
        if li[j]<li[mindx]:
            mindx=j
    # swapping the elements to sort the array
    (li[mindx],li[i])=(li[i],li[mindx])

print(li)