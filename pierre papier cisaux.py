#coding:UTF-8

#MasrterLipakumu

import tkinter as tk
import random

class RPSGame:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.window = tk.Tk()
        self.window.title("Master Lipakumu game Pierre-Papier-Ciseaux")

        # Labels
        self.instructions = tk.Label(self.window, text="Choisissez pierre, papier ou ciseaux:")
        self.instructions.pack()

        # Boutons
        self.rock_button = tk.Button(self.window, text="Pierre", command=lambda: self.play("rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Papier", command=lambda: self.play("paper"))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.window, text="Ciseaux", command=lambda: self.play("scissors"))
        self.scissors_button.pack()

        # Score
        self.score = {"user": 0, "ai": 0}
        self.score_label = tk.Label(self.window, text=f"Score: {self.score['user']} (vous) - {self.score['ai']} (ordinateur)")
        self.score_label.pack()

        self.window.mainloop()

    def play(self, user_choice):
        ai_choice = random.choice(self.options)

        # Résultat de la partie
        result = ""
        if user_choice == ai_choice:
            result = "Match nul!"
        elif (user_choice == "rock" and ai_choice == "scissors") or (user_choice == "paper" and ai_choice == "rock") or (user_choice == "scissors" and ai_choice == "paper"):
            result = "Vous avez gagné!"
            self.score["user"] += 1
        else:
            result = "L'ordinateur a gagné!"
            self.score["ai"] += 1

        # Affichage du résultat et du nouveau score
        result_label = tk.Label(self.window, text=result)
        result_label.pack()

        self.score_label.config(text=f"Score: {self.score['user']} (vous) - {self.score['ai']} (ordinateur)")

game = RPSGame()

# merci d'avoir choisi MasterLipakumu