def evaluateExpression(arr):
    stk=[]
    operators=['+','-','*','/']
    for item in arr:
        if item not in operators:
            stk.append(item)
        else:
            fst=int(stk.pop())
            sec=int(stk.pop())

            if(item=='+'):
                stk.append(fst+sec)
            elif(item=='*'):
                stk.append(fst*sec)
            elif(item=='-'):
                stk.append(fst-sec)
            elif(item=='/'):
                stk.append(fst/sec)
    return stk[-1]
def main():
    li=['2','1','+','3','*']
    brr=['3','4','*','5','6','*','+']
    # 3 4 * 5 6 * +
    print(evaluateExpression(brr))
if __name__=="__main__":
    main()

