import time

space = 12
star = 1

for i in range(1, 10):
    print(i,end="\r")
    time.sleep(1)
    print(" " * space , end=" ")
    print(i * " * ")

    
    star += 1
    space -= 1
        

