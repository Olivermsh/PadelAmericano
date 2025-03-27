from player import Player
from tournament import Tournament
from match import Match
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random

#Globale variabler
image_path = "Baggrund.png" 

players = [] #Liste til spillerne

tournament = None

results = [] #Liste til resultater
match1 = None
match2 = None


# Opret hovedvinduet
root = tk.Tk()
root.title("Padel Americano")
root.geometry("958x560")

#Funktion til at oprette start skærmen
def startScreen():
    global entries #Globalisere entries

    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    #Laver en venstre side af skærmen
    left_frame = tk.Frame(frame)
    left_frame.pack(side="left", expand=True, fill="both")

    label_title = tk.Label(left_frame, text="Padel Americano\n8 spillere", font=("Arial", 24, "bold"), anchor="w", justify="center")
    label_title.pack(pady=20)

    #Oprette knappen til at skifte scene og komme igang
    button = tk.Button(left_frame, text="Sæt i gang...", command=createPlayers, font=("Arial", 16), width=15, height=2)
    button.pack()

    #Laver en højre side af skærmen
    right_frame = tk.Frame(frame)
    right_frame.pack(side="right", expand=True, fill="both", padx=40, pady=30)

    label_players = tk.Label(right_frame, text="Spillerne:", font=("Arial", 20, "bold"), anchor="w")
    label_players.pack(anchor="center", pady=10)

    canvas = tk.Canvas(right_frame, height=2, bg="black", width=350, highlightthickness=0)
    canvas.pack(pady=5)

    #Opretter 8 entry fleter og tilføjer dem til entries listen
    entries = []
    for _ in range(8):
        entry = tk.Entry(right_frame, font=("Arial", 14), width=25)
        entry.pack(pady=5)
        entries.append(entry)

#Opretter spillerne og en turnering
def createPlayers():
    global players, tournament # Gør variablerne tilgængelig uden for funktionen

    players.clear() # Renser listen, så det kun er de 8 på listen
    #Opretter hver spiller med det givende navn
    for i, entry in enumerate(entries):
        name = entry.get().strip()
        if not name:                      #Hvis feltet er tomt får de ukendt spiller ...
            name = f"Ukendt spiller {i+1}"
        players.append(Player(name))  # Opret Player-objekt
    
    random.shuffle(players) #Sortere listen med spillerne i en tilfældig rækkefølge
    
    tournament = Tournament(players) #Opretter en turnering med de givende navne

    changeScene() #Skifter scene

#Funktion til at skifte til billedscenen
def changeScene():
    global img, photo, match1, match2  #Globalisere billedet, og kampene

    #Fjerner alle widgets i vinduet
    for widget in root.winfo_children():
        widget.destroy()

    #Indlæser og viser baggrundsbilledet
    img = Image.open(image_path)
    img = img.resize((958, 560), Image.Resampling.LANCZOS)  #Tilpas størrelse
    photo = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(root, width=958, height=560)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo)

    names = tournament.getPlayers()
    match1 = Match(names[0],names[1],names[2],names[3])
    match2 = Match(names[4],names[5],names[6],names[7])

    #Spillernes placeringer (x, y koordinater)
    spiller_pos = [
        (88.5, 45, f"{names[0]}"), (270.5, 45, f"{names[1]}"),      #Øvre venstre bane
        (88.5, 530, f"{names[2]}"), (270.5, 530, f"{names[3]}"),    #Nedre venstre bane
        (686.5, 45, f"{names[4]}"), (869.5, 45, f"{names[5]}"),     #Øvre højre bane
        (686.5, 530, f"{names[6]}"), (869.5, 530, f"{names[7]}")    #Nedre højre bane
    ]

    #Tegner spillernavne med baggrundsbokse
    for x, y, navn in spiller_pos:
        #Tegner baggrundsboks
        canvas.create_rectangle(x - 83.5, y - 20, x + 83.5, y + 20, fill="white", outline="black")
        #Tilføj navnene
        canvas.create_text(x, y, text=navn, font=("Arial", 14, "bold"), anchor="center")



    #Tilføj entry felter i midten af hver halvdel med tekst "Antal vundende bolde"
    midte_y = 280  #Midten af højden på skærmen
    for x, y in [(146, midte_y - 80), (146, midte_y + 115), (730, midte_y - 80), (730, midte_y + 115)]:
        #Opret en frame til tekst og entry
        frame = tk.Frame(root)
        frame.place(x=x - 50, y=y - 40)

        #Tilføj tekst
        label = tk.Label(frame, text="Antal vundende bolde:", font=("Arial", 12, "bold"))
        label.pack()

        #Tilføj entry felt
        entry = tk.Entry(frame, font=("Arial", 14), width=10)
        entry.pack(pady=5)
        results.append(entry)
    

    # Tilføj knap til at skifte til næste scene
    next_button = tk.Button(root, text="Næste kampe", font=("Arial", 16), width=15, height=2, command=checkScore)
    next_button.place(relx=0.5, rely=0.5, anchor="center")  #Placer knappen i midten af skærmen
    
    #Tilføj tekst "Runde: ... ud af 7" centralt under knappen
    round_text = tk.Label(root, text=f"Runde:\n{tournament.current_round} ud af 7", font=("Arial", 16, "bold"), bg="white")
    round_text.place(relx=0.5, rely=0.65, anchor="center")  #Placer teksten under knappen, centralt

#Tjekker om de rigtig antal bolde er indtastet
def checkScore():
    global results #Globalisere resultaterne 

    if int(results[0].get().strip()) + int(results[1].get().strip()) !=32:
        print(f"Runde {tournament.current_round}: Der er en fejl med resultaterne på bane 1")
        #Tilføj tekst på skærmen
        round_text = tk.Label(root, text="Der er fejl i et \n af resultaterne", font=("Arial", 16, "bold"), bg="white")
        round_text.place(relx=0.5, rely=0.8, anchor="center")  #Placer teksten under knappen, centralt

    elif int(results[2].get().strip()) + int(results[3].get().strip()) !=32:
        print(f"Runde {tournament.current_round}: Der er en fejl med resultaterne på bane 2")
        #Tilføj tekst på skærmen
        round_text = tk.Label(root, text="Der er fejl i et \n af resultaterne", font=("Arial", 16, "bold"), bg="white")
        round_text.place(relx=0.5, rely=0.8, anchor="center")  #Placer teksten under knappen, centralt
    
    if int(results[0].get().strip()) + int(results[1].get().strip()) == 32 and int(results[2].get().strip()) + int(results[3].get().strip()) == 32:
        print("")
        nextRound()


#Funktion til næste runde
def nextRound():
    global match1, match2, results #Globalisere kampene og resultaterne 

    #Registrer resultaterne
    match1.result(int(results[0].get().strip()),int(results[1].get().strip()))
    match2.result(int(results[2].get().strip()),int(results[3].get().strip()))

    tournament.nextRound()

    results = [] #Liste til resultater
    match1 = None
    match2 = None

    #Sørger for at skifte til ranglisten når alle 7 runder er spillet
    if tournament.current_round < 8:
        changeScene()
    else:
        rankingScene()


def rankingScene():
    #Fjerner alle widgets i vinduet
    for widget in root.winfo_children():
        widget.destroy()

    #Sortere listen af spillerne i forhold til point
    ranked_players = sorted(tournament.players, key=lambda player: player.point, reverse=True)

    #Opretter en frame til at holde ranglisten
    ranking_frame = tk.Frame(root)
    ranking_frame.place(relx=0.5, rely=0.4, anchor="center")  #Centreret på skærmen

    #Titel på ranglisten
    label_title = tk.Label(ranking_frame, text="🏆 Slutrangliste 🏆", font=("Arial", 24, "bold"))
    label_title.pack(pady=10)

    #Vis spillernes rangering
    for i, player in enumerate(ranked_players, start=1):
        label = tk.Label(
            ranking_frame, 
            text=f"{i}. {player.name} - {player.point} point", 
            font=("Arial", 16)
        )
        label.pack()

    #Opretter knapperne
    button_frame = tk.Frame(root)
    button_frame.place(relx=0.5, rely=0.8, anchor="center")

    quit_button = tk.Button(button_frame, text="Afslut", font=("Arial", 16), width=12, height=2, command=root.quit)
    quit_button.pack(side="left", padx=10)

    new_tournament_button = tk.Button(button_frame, text="Ny Americano", font=("Arial", 16), width=12, height=2, command=confirmRestart)
    new_tournament_button.pack(side="left", padx=10)

    statistik_button = tk.Button(button_frame, text="Statistik", font=("Arial", 16), width=12, height=2, command=statisticsScene)
    statistik_button.pack(side="left", padx=10)

#Funktion til at vise statistik
def statisticsScene():
    #Fjerner alle widgets i vinduet
    for widget in root.winfo_children():
        widget.destroy()

    #Sorter spillerne efter antal vundne kampe)
    ranked_players = sorted(tournament.players, key=lambda player: (player.won), reverse=True)

    #Opretter en frame til at holde statistikken
    statistik_frame = tk.Frame(root)
    statistik_frame.place(relx=0.5, rely=0.4, anchor="center")  # Centreret på skærmen

    #Titel
    label_title = tk.Label(statistik_frame, text="📊 Spillerstatistik 📊", font=("Arial", 24, "bold"))
    label_title.pack(pady=10)

    #Vis statistik for hver spiller
    for i, player in enumerate(ranked_players, start=1):

        label = tk.Label(
            statistik_frame, 
            text=f"{i}. {player.name} | Vundet kampe: {player.won} | Tabte kampe: {player.lost} | Uafgjordte: {player.tie}", 
            font=("Arial", 16)
        )
        label.pack()

    #Tilbage-knap
    back_button = tk.Button(root, text="Tilbage", font=("Arial", 16), width=12, height=2, command=rankingScene)
    back_button.place(relx=0.5, rely=0.8, anchor="center")

def confirmRestart():
    result = messagebox.askyesno("Bekræft ny Americano", "Er du sikker på, at du vil starte en nyt Americano?")
    if result:
        restartProgram()  # Call restart function if user confirms

#Funktion til at genstarte programmet
def restartProgram():
    global players, tournament, results, match1, match2
    
    players = []
    tournament = None
    results = []
    match1 = None
    match2 = None

    # Gå tilbage til startskærmen
    for widget in root.winfo_children():
        widget.destroy()
    startScreen()


startScreen()
# Start hovedloopet
root.mainloop()
