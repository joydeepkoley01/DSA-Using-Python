li=[1,5,8,9,15,19]
target=0
li.append(target)
n=len(li)
print(li)
i=n-1
while i >= 1 and li[i] < li[i-1]:
    li[i], li[i-1] = li[i-1], li[i]
    i -= 1
print(li)