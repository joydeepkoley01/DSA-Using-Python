li=[1,2,3,4,5,6,7]
sum=0
n=len(li)
for i in range(n):
    sum+=li[i]
avg=sum/len(li)
print(avg)
sum2=0
for i in range(n):
    var=li[i]-avg
    sum2+=var*var
print(sum2)
print("The deviation is : ",(sum2/n)**0.5)