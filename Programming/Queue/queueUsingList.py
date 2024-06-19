r=None
f=0
# To check whether queue is empty or not
def isEmpty(li):
    if f>r:
        return True
    else:
        return False
# Enqueue Operation
def Enqueue(li,ele):
    li.append(ele)
    r=r+1
def Dequeue(li):
    if isEmpty(li):
        print("Queue is Empty ---> Underflow")
    else:
        li.pop(f)
        f=f+1
def peek(li):
    if isEmpty(li):
        print("Underflow ---> Empty List")
    else: 
        print(li[r])
def display(li):
    if isEmpty(li):
        print("Underflow!")
    else:
        print(f"{li[r]} <-- Top")
        for i in range(r-1,f-1,-1):
            print(li[i])