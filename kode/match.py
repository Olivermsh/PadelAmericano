#Klasse til kampene i forhold til resultat og hvem der vandt
class match():
    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def result(self,score1: int, score2: int): #Tilføjer point til den enkelte spiller
        self.p1.addPoint(score1)
        self.p2.addPoint(score1)
        self.p3.addPoint(score2)
        self.p4.addPoint(score2)

        #Registrer om man vandt, tabte eller spillede uafgjordt
        if score1 > score2:
            self.p1.wonMatch()
            self.p2.wonMatch()
        elif score1 < score2:
            self.p3.wonMatch()
            self.p4.wonMatch()
        else:
            self.p1.tieMatch()
            self.p2.tieMatch()
            self.p3.tieMatch()
            self.p4.tieMatch()
            