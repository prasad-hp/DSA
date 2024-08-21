def nStarTriange(n:int):
    for i in range(1, n+1):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(n-i)+1):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()
    pass

nStarTriange(3)