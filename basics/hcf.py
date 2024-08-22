def hcf(n1:int, n2:int):
    ans = 1
    for i in range(1, min(n1+1, n2+1)):
        if(n1 % i == 0 and n2 % i == 0):
            ans = i
    print(ans)
pass
hcf(96, 3)