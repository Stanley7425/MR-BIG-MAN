salesamount=float(input("Enter the amount of money spent in £s?"))

if salesamount>20:
    print("You qualify for a £3 voucher")
elif salesamount>10:
    print("You qualify for a £1 voucher")
else:
    print("Sorry you can't get a voucher today")
