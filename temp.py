# m=6
# n=24
# gcd=1
# for i in range(min(m,n),2,-1):
#     if(m%i==0) and (n%i==0):
#         gcd=i
#         break
# print(gcd)
m=39
n=17
if m<n:
    (m,n)=(n,m)
while(m%n!=0):
    (m,n)=(n,m%n)
print("GCD is: ",n)
fy=open("bubbleSort.py","w");
fy.readlines();
print(fy)