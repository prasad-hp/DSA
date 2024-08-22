def countDigits(n: int) -> int:
    num = n;
    count = 0
    while(num > 0):
        digit = num % 10
        num = int(num/10)
        if(n%digit == 0):
            count = count + 1  
    print(count)
    pass

countDigits(35)