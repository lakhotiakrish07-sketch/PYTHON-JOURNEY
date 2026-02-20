class player:
    def __init__(self, name ,level , score ):
        self.name = name 
        self.score = score
        self.level = level

    def display(self):
        print(f"name:{self.name}\nlevel:{self.level}\nscore:{self.score}")

p1 = player("krish",199,5000)
p1.display()
print(p1.__dict__)
print(dir(p1))
print(help(p1))

