print("operators are -,+,%,*,/")
num1 = float(input("first number:"))
num2= float(input("secod number:"))
arithmetic_op = input("write down the airthematic operator ")
match arithmetic_op :
    case "*":
        print(f"{num1}x{num2}=",num1*num2)
    case "-":
        print(f"{num1}-{num2}=",num1-num2)
    case "+":
        print(f"{num1}+{num2}=",num1+num2)
    case "%":
        print(f"{num1}%{num2}=",num1%num2)
    case "/":
        if(num2==0):
            print("it is not possible to devide a number by 0")
        else :
            print(f"{num1}/{num2}=",num1/num2)  
# Sample Output:
# operators are -,+,%,*,/
# first number: 10
# secod number: 5
# write down the airthematic operator *
# 10.0x5.0= 50.0
