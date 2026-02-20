#creating a python utility tool kit having , calculator and temprature converter
def add (a,b):
    return a+b
def multiply(a,b):
    return a*b    
def divide (a,b):
    return a/b          
def sub (a,b):
    return a-b
def temp(a):
    return ((9/5)*a) + 32

if __name__=="__main__":
    print(add(9,5))
    print(multiply(9,5))
    print(sub(9,5))
    print(divide(9,5))
    print(temp(9))

