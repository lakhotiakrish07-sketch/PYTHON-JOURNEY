#as a day 18 i am going to make a utility tool kit i already made it but now i am making it wuth use if opps 
#and static method which i learned today 
class Utility:
    #sum
    @staticmethod
    def add(a,b):
        return a + b
    #substraction
    @staticmethod
    def sub(a,b):
        return a-b
    #multiplication
    @staticmethod
    def multiply(a,b):
        return a*b
    #devision
    @staticmethod
    def div(a,b):
        return a/b
    
    #temprature converter
    @staticmethod
    def celcius(a):
        return (a-32)*(5/9)
    
    #temprature fahrenheit
    @staticmethod
    def fahrenheit(a):
        return ((9/5)*a)+32


print(Utility.add(1,2))
print(Utility.sub(1,2))
print(Utility.multiply(1,2))
print(Utility.div(1,2))
print(Utility.celcius(10))
print(Utility.fahrenheit(10))