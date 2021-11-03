pin1=3789
acc="savings"

pin = eval(input("Enter your pin:"))

if pin == 3789: 
    acctype=input("Enter your acc type:")
    if acctype=="savings":
        amt=eval(input("Enter your amt:"))
        print(amt,"is successfully debited")
    else:
        print("incorrect acc type")
else:
    print("incorrect pin")

print("Thank you")