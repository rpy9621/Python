#we are going to create a calcualotor 
num1=float(input("Enter first operand : "))
num2=float(input("Enter second operand : "))
opera=input("Choose operator like +,-,*,/,% or ** : ")
match opera:
    case '+':
        print("Addition is :",num1+num2)
    case '-':
        print("Substraction is :",num1-num2)
    case '*':
        print("Multiplication is :",num1*num2)
    case '/':
        print("Division is :",num1/num2)
    case '%':
        print("Substraction is :",num1%num2)
    case '**':
        print("Substraction is :",num1**num2)
    case _:
        print("Invalid Operator")