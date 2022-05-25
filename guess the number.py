import random
a=0
name=input("What's your name? ")
for x in range(1,100):   
    guess=int(input("What number are you going to guess? It is between 1 and 10. "))
    real=(random.randint(1,10))
    #print(real)
    if (guess == real):
        print("You won! Well done!")
    else:
        print("Oh no, you lost ", name, " . The real number was ", real," and your guess was", guess," bad luck.")
