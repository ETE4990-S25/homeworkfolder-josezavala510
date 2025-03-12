class Sage(object):
   # """Wise Healer charecter to help"""
    def __init__(self, name, variety, health, healing=100 ):
       # """Initialize the name, variety, lifesf healer attributes."""
        self.name = name
        self.variety = variety
        self.health = health
        self.healing = healing 
    def heal(self):
        return self.name + " heals " + str(self.healing)
        #"""Heal a certain amount of life."""
    #self.lifes += amount

    
    
sage = Sage("Eagus","Mystical", 150)
print(sage.heal())