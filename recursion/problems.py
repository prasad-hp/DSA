
def printName(n):
    if(n < 1):
        return
    printName(n-1)
    print(n)

printName(6)