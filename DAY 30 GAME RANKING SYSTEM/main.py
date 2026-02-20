#making a game ranking system
class game:
    game_rank = "easy"

    def __init__(self,name,level,score):
        self.name =name
        self.level = level
        self.score = score 

    def display(self):
        print(f"name:{self.name}\nlevel:{self.level}\nscore:{self.score}")

    @classmethod
    def level_change(cls , newrank):
        cls.game_rank = newrank


print(f"rank:{game.game_rank}")
p1 = game("krish",10,400)
p1.display()
print("------------------------------------------------------------------------------------------")
game.level_change("medium")
print(f"game changes to {game.game_rank}")
p2 = game("vishesh",50 , 10000)
p2.display()