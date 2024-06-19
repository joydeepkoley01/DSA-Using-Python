def threesquares(n):
    if(n<0):
        return False
    while n%4==0:
        n//=4
    print(n)
    if n%8==7:
        return False
    else:
        return True
def main():
    m=int(input("Enter any number you want : "))
    print(m,"can be represented as the sum of three square intergers ? -",threesquares(m))
if __name__ == "__main__":
    main()