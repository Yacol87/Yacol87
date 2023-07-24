print ("calculator 2022.10.10")

def calculator():
    num1 = float(input("Insert first number"))
    op = input("your operation, using _ + * /")
    num2 = float(input("Insert second number"))

    if op == "+":
        result=float(num1+num2)
        print (result)
    elif op == "-":
        result=float(num1-num2)
        print (result)
    elif op == "*":
        result=float(num1*num2)
        print (result)
    elif op == "/":
        result=float(num1/num2)
        print (result)
    else:
        print ("Cannot compute that")

wanna_calc = input("Do you want to calculate something? Say Yes or No")

if wanna_calc in ("Yes","yes","y"):
    calculator()
else:
    print ("You don't want to calculate jest")

