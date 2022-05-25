name=input("Whats your name? ")
if name=="DAn":
    print("You are the best creator")
gender=input("man or woman ")
if gender=="man":
    tot=2500
else:
    tot=2000
caltoday=int(input("How many calories have you had today? "))
if caltoday > 250:
    print("TELL ME YOUR ACUAL CALORIE INTAKE OR I WILL KILL YOU!")
else:
    print ("You have",tot - caltoday," calories left")
input()
