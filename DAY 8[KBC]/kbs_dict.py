#i am making a game name kbc uing dictionaries and basics of python 

#making a list of questions 
questions = [["what is the national animal of india","lion","tiger","elephant","cow",2],
             ["what is the capital of india","delhi","lucknow","mumbai","banglore",1],
             ["who is the founder of clanguage ","james gogling","dennis ritchie","guido van","bjarne",2],
             ["who is the founder of  java language ","james gogling","dennis ritchie","guido van","bjarne",1],
             ["who is known as missile man of india ","narender modi","rakhi sawant","deepak kalal","apj abdul kalam ajad",4]
]
#making price amount 
price = [100000, 200000, 400000, 800000, 1600000]

#current balance of our 
current_balance = 0

#defining exit and play as per user  want 
def assurence():
    a = input("do you want to move on next question(yes/no)").strip().lower()
    if a=="yes":
        print("---------------------------------------------------------------")
    elif a=="no":
        print(f"remaining balance = {current_balance}")  
        exit()
    else:
        raise ValueError("invalid input")
      
      
#ask questions using loops , conditions etc .
print("****************ready for the game***************** ")

for i in range(0,len(questions)):

    print(f"question for {price[i]} rupees------------------\n ")
    print(f"question{i+1}:{questions[i]}")
    print(f"1.{questions[i][1]} 2.{questions[i][2]}")
    print(f"3.{questions[i][3]} 4.{questions[i][4]}\n")
    ans = int(input("ans form (1-4):"))
    if(ans==questions[i][5]):
        print("yepp! correct ans\n")
        current_balance = current_balance + price[i]
        print(f"your current balance is {current_balance} rs\n")
        assurence()
    elif(ans!=questions[i][5]):
        print("you loose all the money !")
        exit()
    else:
        raise ValueError("input mistake")  

print("$$$$$$$$$4you are the winner of game kbc$$$$$$$$$$")     
     
     



          
   

