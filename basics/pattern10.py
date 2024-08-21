def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(2*n-1):
        if(i < n):    
            for j in range(i+1):
                print("*", end="")
            print()
        else:
            for j in range(2*n-i, 1, -1):
                print("*", end="")
            print()
            
    pass

nStarTriangle(10)