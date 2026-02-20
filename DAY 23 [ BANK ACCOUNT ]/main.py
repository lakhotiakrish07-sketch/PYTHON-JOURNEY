class Account:
    def __init__(self , acc_number , name , bank_name):
        self.acc_number = acc_number
        self.name = name
        self.bank_name = bank_name
        print(f"account number {self.acc_number} and name is {self.name} and my bank name is {self.bank_name}") 

class Operation:
    def __init__(self , deposite , withdraw ):
        self.deposite = deposite 
        self.withdraw = withdraw
        print(f"available balance is {self.deposite - self.withdraw}")
       

                  

profile  = Account("203847328", "krish","sbi")
accounts = Operation(10000 , 500 )        
