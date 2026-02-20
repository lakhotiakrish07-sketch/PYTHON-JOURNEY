expenses = []
from functools import reduce
while True:
    a=int(input("what do you want 1.addexpense , 2.high_expenses ,3.total_expense ,4.max_expense: "))
    if a==1:
        expense=int(input(f"expense:")) 
        expenses.append(expense)
        print(expenses)
    elif a==2:
        print(list(filter(lambda x : x>5000 , expenses)))  
    elif a==3:
        print("total expense=",reduce(lambda x , y : x+y , expenses))
    elif a==4:
        max_expense =reduce((lambda x,y: x if x>y else y),expenses)
        print(max_expense)
    else:
        print("invalid input!")

        




