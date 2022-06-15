import random
a=0
while a<1:
    person=input("Rock paper or scissors?")
    b = random.randint(1,3)
    if b == 1:
        c=1
    elif b == 2:
        c=2
    elif b == 3:
        c=3
    else:
        print("Error - line 12)
    
