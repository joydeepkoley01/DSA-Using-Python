def isEmpty(li):
    if (len(li)==0):
        return True
    else:
        return False
def push(li,item):
    li.append(item)
    top=len(li)-1
def s_pop(li):
    if isEmpty(li):
        print("Underflow!")
        return
    else:
        i=li.pop()
        if len(li)==0:
            top=None
        else:
            top-=1
    return i
def peek(li):
    if isEmpty(li):
        print("Underflow")
    else:
        top=len(li)-1
        print(li[top])
def display(li):
    if isEmpty(li):
        print("Underflow!")
    else:
        print(f"{li[-1]} <-- Top")
        for i in range(len(li)-2,-1,-1):
            print(li[i])
def main():
    li=['2','1','+','3','*']
    
if __name__=="__main__":
    main()