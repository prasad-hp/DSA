def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(1,n+1):
        for j in range (n-i):
            print(" ", end="")
        for j in range(2*i-1):
            print("*", end="")
        for j in range(n-i):
            print(" ",end="")
        print("")
    pass

nStarTriangle(4)