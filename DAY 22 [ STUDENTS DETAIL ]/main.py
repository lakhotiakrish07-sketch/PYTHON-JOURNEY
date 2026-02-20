class Student :
     name = "krish" 
     age = 19
     roll = 498
     def details(self): 
        print(f"my name is {self.name} my age is {self.age} my roll number is {self.roll} ")
s1 = Student()
s1.name = input("student name:") 
s1.age = int(input("age:")) 
s1.roll = int(input("roll:")) 
s1.details()