def main():

#Spillerne skrives op og sættes i en liste
    player1 = Player("Oliver Hansen")
    player2 = Player(2)
    player3 = Player(3)
    player4 = Player(4)
    player5 = Player(5)
    player6 = Player(6)
    player7 = Player(7)
    player8 = Player(8)

    lst = (player1, player2, player3, player4, player5, player6, player7, player8)

#Der testes    
    print(f"{player1.name} har {player1.point} point")
    round1 = match(player1,player2,player3,player4)
    round1.resualt(20,12)
    print(f"{player1.name} har {player1.point} point, og har vundet {player1.won}")
    print(f"{player2.name} har {player2.point} point, og har vundet {player2.won}")
    print(f"{player3.name} har {player3.point} point, og har vundet {player3.won}")
    print(f"{player4.name} har {player4.point} point, og har vundet {player4.won}")

#Klasse til kampene i forhold til resultat og hvem der vandt
class match():
    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def resualt(self,score1: int, score2: int):
        self.p1.addPoint(score1)
        self.p2.addPoint(score1)
        self.p3.addPoint(score2)
        self.p4.addPoint(score2)

        if score1 > score2:
            self.p1.wonMatch()
            self.p2.wonMatch()
        else:
            self.p3.wonMatch()
            self.p4.wonMatch()

#Klasse til spillerne og deres information
class Player():
    def __init__(self,name: str):
        self.name = name
        self.point = 0
        self.won = 0
    
    def addPoint(self, newPoint: int):
        self.point =+ newPoint
    
    def wonMatch(self):
        self.won =+ 1
    


if __name__ == "__main__": #Hvis navnet er lig "__main__" kører den main()
    main()