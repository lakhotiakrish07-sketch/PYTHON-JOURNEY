class Person:
    def __init__(self, name , rollnumber , year  ):
        self.name=name
        self.rollnumber=rollnumber
        self.year = year

class Books:
    def __init__(self , title , price , catogery):
        self.title = title
        self.price=price
        self.catogery=catogery       
    
class Student(Person,Books):
    def __init__(self , name ,rollnumber , year , title , price , catogery ):
        Person.__init__(self ,name , rollnumber , year)
        Books.__init__( self ,title , price ,catogery)

    def display(self):
        print(f"name:{self.name}\nrollnumber:{self.rollnumber}\nyear{self.year}\ntitle:{self.title}\nprive:{self.price}\ncatogery:{self.catogery}")
    def tax(self):
        if self.price>500:
            print(f"total price = {int(self.price)+ 50}")
        else:
            pass    

s1 = Student("krish",98,2025,"elite codders",550,"skills")    
s1.display()
s1.tax()
    