print("hi i am here to find odd,even and prime number ")
number = int(input("number:"))
#odd even checker
if(number%2==0):
    print(f"{number} is even")
else:
    print(f"{number} is odd")
#prime checker 
if number < 2:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")

