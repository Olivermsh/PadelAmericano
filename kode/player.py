#Klasse til spillerne og deres information
class Player():
    def __init__(self,name: str):
        self.name = name
        self.point = 0
        self.won = 0
        self.tie = 0
        self.lost = 8
    
    def addPoint(self, newPoint: int): #Opdatere antal point
        self.point += newPoint
    
    def wonMatch(self): #Opdatere vundene kampe
        self.won += 1
        self.lost -= 1
    
    def tieMatch(self): #Opdatere uafgjordte kampe
        self.tie += 1
        self.lost -= 1
    
    def __str__(self): #Retuneren navnet på spilleren
        return self.name
