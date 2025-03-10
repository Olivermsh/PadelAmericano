def main():

#Spillerne skrives op og sættes i en liste
    player1 = Player("Oliver Hansen")
    player2 = Player("A2")
    player3 = Player("B3")
    player4 = Player("C4")
    player5 = Player("D5")
    player6 = Player("E6")
    player7 = Player("F7")
    player8 = Player("G8")

    lst = [player1, player2, player3, player4, player5, player6, player7, player8]

#Der testes    
    tournament1 =Tournament(lst)
    tournament1.round1()
    tournament1.round2()
    tournament1.round3()
    tournament1.round4()
    tournament1.round5()
    tournament1.round6()
    tournament1.round7()
    tournament1.ranking()

#Klasse til kampene i forhold til resultat og hvem der vandt
class match():
    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def result(self,score1: int, score2: int):
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
        self.point += newPoint
    
    def wonMatch(self):
        self.won += 1
    
    def __str__(self):
        return self.name



#Klasse til turneringen
class Tournament():
    def __init__(self,names):
        self.players = names
        self.p1 = names[0]
        self.p2 = names[1]
        self.p3 = names[2]
        self.p4 = names[3]
        self.p5 = names[4]
        self.p6 = names[5]
        self.p7 = names[6]
        self.p8 = names[7]

    def getResult(self,p1,p2,p3,p4):
        team1 = int(input(f"Resultat for {p1} og {p2}: "))
        team2 = int(input(f"Resultat for {p3} og {p4}: "))
        return team1, team2

    
    def round1(self):
        round1a = match(self.p1,self.p2,self.p3,self.p4)
        round1b = match(self.p5,self.p6,self.p7,self.p8)
        print("Runde 1")
        print(f"På bane 1 spiller {self.p1} og {self.p2} mod {self.p3} og {self.p4}")
        print(f"På bane 2 spiller {self.p5} og {self.p6} mod {self.p7} og {self.p8}")

        score1, score2=self.getResult(self.p1,self.p2,self.p3,self.p4)
        round1a.result(score1, score2)

        score3, score4=self.getResult(self.p5,self.p6,self.p7,self.p8)
        round1b.result(score3, score4)

        print("----------------------------------------------")
        print("")

    def round2(self):
        round2a = match(self.p1,self.p3,self.p5,self.p7)
        round2b = match(self.p2,self.p4,self.p6,self.p8)
        print("Runde 2")
        print(f"På bane 1 spiller {self.p1} og {self.p3} mod {self.p5} og {self.p7}")
        print(f"På bane 2 spiller {self.p2} og {self.p4} mod {self.p6} og {self.p8}")

        score1, score2=self.getResult(self.p1,self.p3,self.p5,self.p7)
        round2a.result(score1, score2)

        score3, score4=self.getResult(self.p2,self.p4,self.p6,self.p8)
        round2b.result(score3, score4)

        print("----------------------------------------------")
        print("")

    def round3(self):
        round3a = match(self.p2,self.p3,self.p6,self.p7)
        round3b = match(self.p1,self.p4,self.p5,self.p8)
        print("Runde 3")
        print(f"På bane 1 spiller {self.p2} og {self.p3} mod {self.p6} og {self.p7}")
        print(f"På bane 2 spiller {self.p1} og {self.p4} mod {self.p5} og {self.p8}")

        score1, score2=self.getResult(self.p2,self.p3,self.p6,self.p7)
        round3a.result(score1, score2)

        score3, score4=self.getResult(self.p1,self.p4,self.p5,self.p8)
        round3b.result(score3, score4)

        print("----------------------------------------------")
        print("")

    def round4(self):
        round4a = match(self.p1,self.p5,self.p2,self.p6)
        round4b = match(self.p3,self.p7,self.p4,self.p8)
        print("Runde 4")
        print(f"På bane 1 spiller {self.p1} og {self.p5} mod {self.p2} og {self.p6}")
        print(f"På bane 2 spiller {self.p3} og {self.p7} mod {self.p4} og {self.p8}")

        score1, score2=self.getResult(self.p1,self.p5,self.p2,self.p6)
        round4a.result(score1, score2)

        score3, score4=self.getResult(self.p3,self.p7,self.p4,self.p8)
        round4b.result(score3, score4)

        print("----------------------------------------------")
        print("")
    
    def round5(self):
        round5a = match(self.p2,self.p5,self.p4,self.p7)
        round5b = match(self.p1,self.p6,self.p3,self.p8)
        print("Runde 5")
        print(f"På bane 1 spiller {self.p2} og {self.p5} mod {self.p4} og {self.p7}")
        print(f"På bane 2 spiller {self.p1} og {self.p6} mod {self.p3} og {self.p8}")

        score1, score2=self.getResult(self.p2,self.p5,self.p4,self.p7)
        round5a.result(score1, score2)

        score3, score4=self.getResult(self.p1,self.p6,self.p3,self.p8)
        round5b.result(score3, score4)

        print("----------------------------------------------")
        print("")

    def round6(self):
        round6a = match(self.p2,self.p8,self.p3,self.p5)
        round6b = match(self.p1,self.p7,self.p4,self.p6)
        print("Runde 6")
        print(f"På bane 1 spiller {self.p2} og {self.p8} mod {self.p3} og {self.p5}")
        print(f"På bane 2 spiller {self.p1} og {self.p7} mod {self.p4} og {self.p6}")

        score1, score2=self.getResult(self.p2,self.p8,self.p3,self.p5)
        round6a.result(score1, score2)

        score3, score4=self.getResult(self.p1,self.p7,self.p4,self.p6)
        round6b.result(score3, score4)

        print("----------------------------------------------")
        print("")

    def round7(self):
        round7a = match(self.p3,self.p6,self.p4,self.p5)
        round7b = match(self.p1,self.p8,self.p2,self.p7)
        print("Runde 7")
        print(f"På bane 1 spiller {self.p3} og {self.p6} mod {self.p4} og {self.p5}")
        print(f"På bane 2 spiller {self.p1} og {self.p8} mod {self.p2} og {self.p7}")

        score1, score2=self.getResult(self.p3,self.p6,self.p4,self.p5)
        round7a.result(score1, score2)

        score3, score4=self.getResult(self.p1,self.p8,self.p2,self.p7)
        round7b.result(score3, score4)

        print("----------------------------------------------")

    def ranking(self):
        # Sorterer spillerne efter point i faldende rækkefølge
        ranked_players = sorted(self.players, key=lambda player: player.point, reverse=True)

        print("\nRangliste:")
        for i, player in enumerate(ranked_players, start=1):
            print(f"{i}. {player.name} med {player.point} point")
    
    


if __name__ == "__main__": #Hvis navnet er lig "__main__" kører den main()
    main()