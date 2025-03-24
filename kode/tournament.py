from match import *

#Oprette klassen
class Tournament:
    def __init__(self, names):
        self.players = names
        self.current_round = 1
        self.players_in_round = []

        # Definer runderne som en dictionary
        self.rounds = {
            1: [(0, 1, 2, 3), (4, 5, 6, 7)], #Runde nummer, kampene
            2: [(0, 2, 4, 6), (1, 3, 5, 7)],
            3: [(1, 2, 5, 6), (0, 3, 4, 7)],
            4: [(0, 4, 1, 5), (2, 6, 3, 7)],
            5: [(1, 4, 3, 6), (0, 5, 2, 7)],
            6: [(1, 7, 2, 4), (0, 6, 3, 5)],
            7: [(2, 5, 3, 4), (0, 7, 1, 6)]
        }
    def getPlayers(self): #Henter indeks fra dictionary og laver en liste med navnene i korrekt rækkefølge
            self.players_in_round = [player for match in self.rounds[self.current_round] for player in match]
            lst = [] #Tom liste til navnene
            for _ in self.players_in_round:
                lst.append(self.players[_])
            return lst #Retunere listen
    
    def nextRound(self): #Holder styr på nuværende runde nummer
        self.current_round += 1