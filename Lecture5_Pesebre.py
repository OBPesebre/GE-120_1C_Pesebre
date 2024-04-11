# # OOP
# class Shape:
#     pass

# circleShape = Shape()

# print(type(circleShape))

class NBAPlayer:
    def __init__(self, name, dribbling="20"):
        self.name = "Jayson Brown"
        self.team = "Boston State Nuggets"
        self.dribbling = dribbling
        self.defense = "68"
        self.position = "Power Guard"

    def clutch(self):
        print(self.name + " for the win!!!")
    
    def __str__(self):
        return(self.name + " is a " + self.position)
    
    def __add__(self, other):
        return(self.name + "and")

Wemby = ("Wemby", "The Alien")
Lebron = ("LBJ", "The Cow")
print(Wemby + Lebron)

NBAPlayer = NBAPlayer("Jayson Brown", "BoraCUP Secured")
print(NBAPlayer)