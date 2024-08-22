def armstrongNumber(n:int):
    num = n;
    sum = 0
    while(num > 0):
        digit = num % 10;
        num = int(num/10);
        sum = sum + digit * digit * digit
    if(sum == n):
        print("Number is armstrong Number")
    else: print("Number is not armastong Number")
    pass
armstrongNumber(153)