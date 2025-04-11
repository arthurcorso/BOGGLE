import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from grille import generer_grille
from dictionnaire import charger_dictionnaire
from moteur import mot_valide_dans_grille, points_mot
import info

dictionnaire = charger_dictionnaire("assets/scrabble.txt")
grille = generer_grille()
mots_trouves = set()
score_total = 0
temps_restant = 180  # 3 minutes

def afficher_grille(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    for i in range(4):
        for j in range(4):
            lettre = grille[i][j]
            lbl = ttk.Label(frame, text=lettre, font=("Helvetica", 20), width=4)
            lbl.grid(row=i, column=j, padx=5, pady=5)

def valider_mot():
    global score_total
    mot = entree_mot.get().strip().upper()
    entree_mot.delete(0, tk.END)
    if mot in mots_trouves:
        messagebox.showinfo("Déjà trouvé", f"Tu as déjà proposé le mot {mot}")
        return
    if mot not in dictionnaire or not mot_valide_dans_grille(grille, mot):
        messagebox.showwarning("Mot invalide", f"{mot} n'est pas valide ou n'est pas dans la grille")
        return
    mots_trouves.add(mot)
    pts = points_mot(mot)
    score_total += pts
    champ_mots.insert(tk.END, f"{mot} ({pts} pts)\n")
    label_score.config(text=f"Score : {score_total} pts")

def decompte():
    global temps_restant
    if temps_restant > 0:
        minutes = temps_restant // 60
        secondes = temps_restant % 60
        label_timer.config(text=f"Temps restant : {minutes:02}:{secondes:02}")
        temps_restant -= 1
        racine.after(1000, decompte)
    else:
        fin_partie()

def fin_partie():
    nom = simpledialog.askstring("Fin de partie", f"Temps écoulé ! Tu as marqué {score_total} points.\nEntre ton nom :")
    if nom:
        with open("classement.txt", "a", encoding="utf-8") as f:
            f.write(f"{nom} : {score_total} pts\n")
    messagebox.showinfo("Terminé", "Merci d'avoir joué !")
    racine.destroy()

# Interface Tkinter
racine = tk.Tk()
racine.title(f"Boggle - Mode Joueur - {info.version}")
racine.configure(bg="#f4f4f4")

cadre_grille = ttk.Frame(racine)
cadre_grille.grid(row=0, column=0, padx=10, pady=10)
afficher_grille(cadre_grille)

entree_mot = ttk.Entry(racine, font=("Helvetica", 16), width=20)
entree_mot.grid(row=1, column=0, pady=10)
entree_mot.focus()

btn_valider = ttk.Button(racine, text="Valider", command=valider_mot)
btn_valider.grid(row=2, column=0)
racine.bind("<Return>", lambda event: valider_mot())

champ_mots = tk.Text(racine, width=40, height=15)
champ_mots.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

label_score = ttk.Label(racine, text="Score : 0 pts", font=("Helvetica", 14))
label_score.grid(row=3, column=0, pady=5)

label_timer = ttk.Label(racine, text="Temps restant : 03:00", font=("Helvetica", 14))
label_timer.grid(row=3, column=1)

decompte()
racine.mainloop()
