num1=int(input("Hi. Please tell me your first number. "))
operation=input("Please tell me your operation: add, minus, times, or divide.")
if operation=="add":
    num2=int(input("Please tell me your second number"))
    answer=(num1+num2)
    print(answer)
elif operation=="minus":
    num2=int(input("Please tell me your second number"))
    answer=(num1-num2)
    print(answer)
elif operation==("times"):
    num2=int(input("Please tell me your second number"))
    answer=(num1*num2)
    print(answer)
elif operation=="divide":
    num2=int(input("Please tell me your second number"))
    answer=(num1/num2)
    print(answer)
else:
    print("Please use one of the four operations listed above and restart.")
input()
