from match import *

class Tournament:
    def __init__(self, names):
        self.players = names

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

    def getResult(self, p1, p2, p3, p4):
        while True:
            try:
                team1 = int(input(f"Resultat for {p1} og {p2}: "))
                team2 = int(input(f"Resultat for {p3} og {p4}: "))

                if team1 + team2 > 32:
                    print(f"Fejl! Summen af de to resultater er {team1 + team2}, der spilles kun 32 bolde.")
                elif team1 + team2 <32:
                    print(f"Fejl! Summen af de to resultater er {team1 + team2}, der spilles 32 bolde, i er ikke færdig endnu.")
                else:
                    return team1, team2

            except ValueError:
                print("Ugyldigt input! Indtast venligst et heltal.")  

    def play_rounds(self):
        for round_number, matches in self.rounds.items(): #Opdeller hver item i runder og kampe
            print(f"Runde {round_number}")

            for match_teams in matches: #Opsætter kampen for hver kamp under kampe i det nuværende item
                p1, p2, p3, p4 = [self.players[idx] for idx in match_teams]
                print(f"På banen spiller {p1} og {p2} mod {p3} og {p4}")

                game = match(p1, p2, p3, p4)
                score1, score2 = self.getResult(p1, p2, p3, p4)
                game.result(score1, score2)

            print("----------------------------------------------\n")

    def ranking(self):
        ranked_players = sorted(self.players, key=lambda player: player.point, reverse=True)

        print("\nRangliste:")
        for i, player in enumerate(ranked_players, start=1):
            print(f"{i}. {player.name} med {player.point} point")
