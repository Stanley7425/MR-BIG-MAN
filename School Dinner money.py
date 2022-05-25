start=float(input("How much money did you have before lunch (in £)? "))
import time
time.sleep(1)
while True:
    spent=float(input("How much did you spend (in £) ?"))
    if start < spent:
        print("YOU ARE IN DEBT")
    elif start == spent:
        print("EAT LUNCH NOW!")
    else:
        print("You have ",start - spent,"£ left for the rest of time.")
