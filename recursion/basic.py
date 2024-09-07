
count = 20;
def check():
    global count
    count = count - 1
    while(count > 0):
        print(count)
        check()

check()