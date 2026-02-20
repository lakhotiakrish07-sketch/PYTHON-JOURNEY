import time 
balance = 0 
def account():
    global balance
    a = int(input("what do you want: 1.check balance , 2.deposite , 3.withdraw ,4.exit"))
    if a == 1 :
        print(balance)
    elif a== 2:
        deposite = int(input("how much you want to deposite:"))
        b=balance
        balance=balance+ (deposite)
        print("your reciept-------------------------------------------------------------------------")
        t=time.time()
        print(f"initial_balance:{b}\ndepostie:{deposite}\nnew_amount{balance}\ntime:{time.ctime(t)}")
        print("--------------------------------------------------------------------------------")
    elif a==3:
        withdraw = int(input("withdrawl amount:"))
        if balance>=withdraw:
            b=balance
            balance=balance-withdraw
            t=time.time()
            print("your reciept-------------------------------------------------------------------------")
            print(f"initial_balance:{b}\nwithdraw_amount:{withdraw}\nnew_amount{balance}\ntime:{time.ctime(t)}")
            print("---------------------------------------------------------------------------------------")
        else:
            print("insufficient balance")    
    elif a==4:
        print("thanks for visiting the bank")
        exit()
    else:
        return True 
    
#callinf the function 
while True:
    account()   




