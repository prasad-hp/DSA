import math
def checkPrime(n:int):
    count = 0
    for i in range(3, int(math.sqrt(n)+1)):
        if(n % i == 0):
            count += 1
    if(count > 0):
        print("Number " + str(n) + " is not prime number")
    else: print("It is prime")
pass

checkPrime(37)