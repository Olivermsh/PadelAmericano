from player import Player
from tournament import Tournament
import tkinter as tk
from PIL import Image, ImageTk

image_path = "Baggrund.png" 

# Gør players til en global variabel
players = []

tournament = None

# Opret hovedvinduet
root = tk.Tk()
root.title("Padel Americano")
root.geometry("958x560")


def create_players():
    global players, tournament  # Gør variablerne tilgængelig uden for funktionen
    players.clear()  # Rens listen, så vi ikke får dubletter ved flere klik
    for i, entry in enumerate(entries):
        name = entry.get().strip()
        if not name:
            name = f"Ukendt spiller {i+1}"
        players.append(Player(name))  # Opret Player-objekt
    
    tournament = Tournament(players) #Opretter en turnering med de givende navne

    skift_scene()

def next_round():
    tournament.nextRound()
    if tournament.current_round < 8:
        skift_scene()
    else:
        ranking_scene()
    
# Funktion til at skifte til billedscenen
def skift_scene():
    global img, photo  # Sørg for, at billedet ikke bliver slettet af garbage collection

    # Fjern alle widgets i vinduet
    for widget in root.winfo_children():
        widget.destroy()

    # Indlæs og vis baggrundsbilledet
    img = Image.open(image_path)
    img = img.resize((958, 560), Image.Resampling.LANCZOS)  # Tilpas størrelse
    photo = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(root, width=958, height=560)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo)

    spillere_i_runden = [spiller for kamp in tournament.rounds[1] for spiller in kamp]
    names = tournament.getPlayers()

    # Spillernes placeringer (x, y koordinater)
    spiller_pos = [
        (55, 45, f"{names[0]}"), (237, 45, f"{names[1]}"),  # Øvre venstre bane
        (55, 530, f"{names[2]}"), (237, 530, f"{names[3]}"),  # Nedre venstre bane
        (653, 45, f"{names[4]}"), (836, 45, f"{names[5]}"),  # Øvre højre bane
        (653, 530, f"{names[6]}"), (836, 530, f"{names[7]}")   # Nedre højre bane
    ]

    # Tegn spillernavne med baggrundsbokse
    for x, y, navn in spiller_pos:
        # Tegn baggrundsboks (firkant)
        canvas.create_rectangle(x - 50, y - 20, x + 117, y + 20, fill="white", outline="black")
        # Tilføj tekst (spillernavn)
        canvas.create_text(x, y, text=navn, font=("Arial", 14, "bold"))

    # Tilføj entry-felter i midten af hver halvdel med tekst "Antal vundende bolde"
    midte_y = 280  # Midten af højden på skærmen
    for x, y in [(146, midte_y - 80), (730, midte_y - 80), (146, midte_y + 115), (730, midte_y + 115)]:
        # Opret en frame til tekst og entry
        frame = tk.Frame(root)
        frame.place(x=x - 50, y=y - 40)

        # Tilføj tekst
        label = tk.Label(frame, text="Antal vundende bolde:", font=("Arial", 12, "bold"))
        label.pack()

        # Tilføj entry-felt
        entry = tk.Entry(frame, font=("Arial", 14), width=10)
        entry.pack(pady=5)

    # Tilføj knap til at skifte til næste scene
    next_button = tk.Button(root, text="Næste kampe", font=("Arial", 16), width=15, height=2, command=next_round)
    next_button.place(relx=0.5, rely=0.5, anchor="center")  # Placer knappen i midten af skærmen

def ranking_scene():
        # Fjern alle widgets i vinduet
    for widget in root.winfo_children():
        widget.destroy()
    
# Opret en frame til layout
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Venstre side - Titeltekst og knap
left_frame = tk.Frame(frame)
left_frame.pack(side="left", expand=True, fill="both")

label_title = tk.Label(left_frame, text="Padel Americano\n8 spillere", font=("Arial", 24, "bold"), anchor="w", justify="center")
label_title.pack(pady=20)

button = tk.Button(left_frame, text="Sæt i gang...", command=create_players, font=("Arial", 16), width=15, height=2)
button.pack()

# Højre side - Spiller input
right_frame = tk.Frame(frame)
right_frame.pack(side="right", expand=True, fill="both", padx=40, pady=30)  # Tilføjet lidt padding i højre side

label_players = tk.Label(right_frame, text="Spillerne:", font=("Arial", 20, "bold"), anchor="w")
label_players.pack(anchor="center", pady=10)  # Centreret på stregen

# Vandret linje
canvas = tk.Canvas(right_frame, height=2, bg="black", width=350, highlightthickness=0)
canvas.pack(pady=5)

# Opret 8 entry felter til navne
entries = []
for i in range(8):
    entry = tk.Entry(right_frame, font=("Arial", 14), width=25)
    entry.pack(pady=5)
    entries.append(entry)

# Start hovedloopet
root.mainloop()
