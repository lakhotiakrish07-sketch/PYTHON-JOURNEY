class students :
    def __init__(self , name, rollnumber , marks ):
        self._name = name
        self._rollnumber = rollnumber
        self.marks=marks# if we want publicly axcess variable we cannot use ._ (for best practice and readiablilty)

    @property
    def marks(self):    
       return self._marks#we have to put _marks in geter and setter other wise it make a recursive loop 
    @property
    def name(self):
        return self._name
    @property
    def rollnumber(self):
        return self._rollnumber
    
    @marks.setter
    def marks(self, marks):
        if 0<=marks<=100:
            self._marks =marks
        else:
            print("invalid marks (it is in range 0 to 100)")        

s1 = students("krish",200 , 0)
print(s1.name)
print(s1.rollnumber)
print(s1.marks)
 
s1.marks = 105
print(s1.marks)
        

