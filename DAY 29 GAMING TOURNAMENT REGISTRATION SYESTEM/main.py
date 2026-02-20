class tournament:
    tournament_name = "spark eye tournament"
    tournament_price = 500
    membernumber = 0
    
    def __init__(self , name , gameid , rank):
        self.name = name
        self.gameid = gameid
        self.rank = rank
        self.join = False

    def jointournament(self):
        if self.rank<20:
            print("you are not ready for the tournament\nimprove your level!")
        else:
            if not self.join:   # Prevent double join
                self.join = True
                tournament.membernumber += 1
                print(f"{self.name} joined successfully!")
            else:
                print(f"{self.name} has already joined.")     
        
    
    def result(self):
        if self.join == True:
            print(f"{tournament.tournament_name}")
            print(f"name:{self.name}\ngameid:{self.gameid}\nrank:{self.rank}\nmembernumber:{tournament.membernumber}")
            
        else:
            print("you are unable to join the tournament")    

obj1 = tournament("krish" , 123 , 50)
obj1.jointournament()
obj1.result()

obj2 = tournament("aman",234 , 12)
obj2.jointournament()
obj2.result() 
obj3 = tournament("lambu",324 , 55)   
obj3.jointournament()
obj3.result()       

obj1.jointournament()





