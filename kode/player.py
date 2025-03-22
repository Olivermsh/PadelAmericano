#Klasse til spillerne og deres information
class Player():
    def __init__(self,name: str):
        self.name = name
        self.point = 0
        self.won = 0
    
    def addPoint(self, newPoint: int): #Opdatere antal point
        self.point += newPoint
    
    def wonMatch(self): #Opdatere vundene kampe
        self.won += 1
    
    def __str__(self):
        return self.name



# #Spillerne skrives op og sættes i en liste
# player1 = Player("Oliver Hansen")
# player2 = Player("A2")
# player3 = Player("B3")
# player4 = Player("C4")
# player5 = Player("D5")
# player6 = Player("E6")
# player7 = Player("F7")
# player8 = Player("G8")

# lst = [player1, player2, player3, player4, player5, player6, player7, player8]
