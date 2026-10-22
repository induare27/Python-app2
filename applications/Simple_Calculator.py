def Calculator(opr):
    try:
        a=int(input("Enter 1st digit: "))
        b=int(input("Enter 2nd digit: "))
        if opr=="Addition":
            res=a+b
            print("Addition of a and b: ",res)
        elif opr=="Subtraction":
            res=a-b
            print("Subtraction of a and b: ",res)
        elif opr=="Multiplication":
            res=a*b
            print("Multiplication of a and b: ",res)
        elif opr=="Division":
            res=a/b
            print("Division of a and b: ",res)

    except ValueError:
        print("Enter a valid number")
    except ZeroDivisionError:
        print("division by zero is not possible")

#l=["Addition","Subtration", "Multiplication", "Division"]
opr=input("Addition,Subtration, Multiplication, Division.\nEnter the operation:")
Calculator(opr)